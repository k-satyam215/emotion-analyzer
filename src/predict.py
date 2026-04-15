import pickle
import os
import re
from src.preprocess import clean_text

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load models
emotion_model = pickle.load(open(os.path.join(BASE_DIR, "models", "emotion_model.pkl"), "rb"))
emotion_vectorizer = pickle.load(open(os.path.join(BASE_DIR, "models", "emotion_vectorizer.pkl"), "rb"))

clarity_model = pickle.load(open(os.path.join(BASE_DIR, "models", "clarity_model.pkl"), "rb"))
clarity_vectorizer = pickle.load(open(os.path.join(BASE_DIR, "models", "vectorizer.pkl"), "rb"))


# 🔥 NORMALIZATION
def normalize(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def predict(text):
    if not text or text.strip() == "":
        return {"error": "Please enter valid text"}

    cleaned = clean_text(text)
    text_lower = normalize(text)

    # =========================
    # 🔥 ML BASE
    # =========================
    X_emotion = emotion_vectorizer.transform([cleaned])
    ml_emotion = emotion_model.predict(X_emotion)[0]
    ml_conf = max(emotion_model.predict_proba(X_emotion)[0])

    # =========================
    # 🔥 KEYWORD BANK
    # =========================
    emotion_map = {
        "anxiety": [
            "stress", "stressed", "pressure", "anxious", "tension",
            "nervous", "panic", "dar lag raha",
            "samajh nahi aa raha", "kya karu", "confused",
            "not sure", "unsure", "scared", "worried",
            "cannot handle", "handle it", "doubt", "afraid"
        ],
        "happy": [
            "happy", "excited", "great", "awesome",
            "selected", "success", "achieved", "cleared", "passed",
            "got job", "got the job", "got a job", "job offer",
            "offer letter", "placed", "hired"
        ],
        "sad": [
            "sad", "depressed", "low", "failure", "fail",
            "lost", "not good enough"
        ],
        "angry": [
            "angry", "mad", "frustrated", "hate", "irritated"
        ]
    }

    # =========================
    # 🔥 SCORING
    # =========================
    scores = {k: 0 for k in emotion_map}

    for emo, words in emotion_map.items():
        for w in words:
            if w in text_lower:
                scores[emo] += 1

    # 🔥 SUCCESS BOOST (IMPORTANT)
    if "job" in text_lower and any(w in text_lower for w in ["got", "selected", "placed", "hired"]):
        scores["happy"] += 2

    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top_emotion, top_score = sorted_scores[0]
    second_emotion, second_score = sorted_scores[1]

    confidence_source = "ml"

    # =========================
    # 🔥 FINAL EMOTION
    # =========================
    if top_score > 0 and second_score > 0:
        pair = sorted([top_emotion, second_emotion])

        if pair == ["anxiety", "happy"]:
            emotion = "mixed (happy + anxiety)"
        elif pair == ["sad", "anxiety"]:
            emotion = "mixed (sad + anxiety)"
        elif pair == ["happy", "sad"]:
            emotion = "mixed (happy + sad)"
        else:
            emotion = f"mixed ({pair[0]} + {pair[1]})"

        # 🔥 FIXED CONFIDENCE
        confidence = 0.55 + 0.1 * min(top_score + second_score, 3)
        confidence_source = "rule"

    elif top_score > 0:
        emotion = top_emotion

        # 🔥 FIXED CONFIDENCE
        confidence = 0.5 + 0.1 * min(top_score, 3)
        confidence_source = "rule"

    else:
        # ML fallback
        if ml_conf > 0.4:
            emotion = ml_emotion
            confidence = ml_conf
        else:
            emotion = "neutral"
            confidence = 0.5

    confidence = min(confidence, 0.9)

    # =========================
    # 🔥 SENTIMENT
    # =========================
    if emotion == "happy":
        sentiment = "positive"
    elif emotion in ["sad", "angry", "anxiety"]:
        sentiment = "negative"
    elif "mixed" in emotion:
        sentiment = "neutral"
    else:
        sentiment = "neutral"

    # =========================
    # 🔥 CLARITY
    # =========================
    word_count = len(text.split())

    if word_count <= 4:
        clarity = "vague"
    elif word_count <= 8:
        clarity = "moderate"
    else:
        clarity = "clear"

    # =========================
    # 🔥 INTENT
    # =========================
    if any(w in text_lower for w in ["help", "suggest", "kya karu", "how to"]):
        intent = "seeking_help"

    elif any(w in text_lower for w in ["not sure", "confused", "unsure", "doubt"]):
        intent = "seeking_help"

    elif any(w in text_lower for w in ["why", "what", "how", "kaise"]):
        intent = "question"

    elif any(w in text_lower for w in ["thanks", "thank you"]):
        intent = "gratitude"

    elif "?" in text:
        intent = "question"

    else:
        intent = "statement"

    # =========================
    # 🔥 SUGGESTIONS
    # =========================
    suggestions = {
        "sad": "Talk to someone or take rest",
        "anxiety": "Try breathing exercises or plan your work step-by-step",
        "angry": "Take a short break and calm your mind",
        "happy": "Keep up the positive energy!",
        "mixed (happy + anxiety)": "You're doing well, but it's okay to feel nervous. Prepare step-by-step.",
        "mixed (sad + anxiety)": "It's okay to feel overwhelmed. Take things one step at a time.",
        "mixed (happy + sad)": "Mixed feelings are normal. Reflect on what's causing them."
    }

    suggestion = suggestions.get(emotion, "Stay balanced and mindful")

    return {
        "emotion": emotion,
        "sentiment": sentiment,
        "clarity": clarity,
        "intent": intent,
        "confidence": round(confidence * 100, 2),
        "confidence_source": confidence_source,
        "suggestion": suggestion
    }