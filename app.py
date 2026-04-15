import streamlit as st
from src.predict import predict

st.set_page_config(page_title="AI Emotion Analyzer", layout="centered")

# 🔥 PREMIUM UI
st.markdown("""
<style>

/* Background */
[data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at 50% 0%, #1a0000, #000000 60%);
    color: #f8fafc;
}

/* Title */
.title {
    text-align: center;
    font-size: 44px;
    font-weight: 800;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #9ca3af;
    margin-bottom: 30px;
}

/* Text Area */
.stTextArea textarea {
    background: #0a0a0a;
    color: #f8fafc;
    border-radius: 16px;
    border: 1.5px solid rgba(255, 0, 0, 0.35);
    padding: 14px;
}

.stTextArea textarea:focus {
    border: 1.5px solid #ff1e1e;
    box-shadow: 0 0 20px rgba(255,0,0,0.35);
}

/* Button */
.stButton button {
    background: linear-gradient(135deg, #b30000, #ff1e1e);
    border-radius: 14px;
    padding: 12px 28px;
    color: white;
    font-weight: 600;
    box-shadow: 0 8px 25px rgba(255,0,0,0.35);
    transition: all 0.2s ease;
}

.stButton button:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 35px rgba(255,0,0,0.6);
}

/* Result Card */
.result-card {
    background: rgba(20,0,0,0.85);
    padding: 28px;
    border-radius: 18px;
    margin-top: 30px;
    border: 1px solid rgba(255,0,0,0.2);
}

/* Suggestion Box */
.suggestion {
    margin-top: 15px;
    padding: 14px;
    border-radius: 12px;
    background: rgba(30,0,0,0.9);
    border: 1px solid rgba(255,0,0,0.2);
}

/* Progress Bar */
.stProgress > div > div > div {
    background: linear-gradient(90deg, #ff1e1e, #ff4d4d) !important;
}

</style>
""", unsafe_allow_html=True)

# 🔥 HEADER
st.markdown('<div class="title">🧠 AI Emotion & Intent Analyzer</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered emotion & intent insights</div>', unsafe_allow_html=True)

# 🔥 EMOJI MAPPING (FINAL FIX)
emotion_icons = {
    "happy": "😊",
    "sad": "😢",
    "angry": "😡",
    "anxiety": "😰",
    "mixed (happy + anxiety)": "😅"   # 🔥 FIXED
}

# INPUT
text = st.text_area("✍️ Enter your text:", height=140)

# BUTTON
if st.button("🚀 Analyze"):
    result = predict(text)

    if "error" in result:
        st.error(result["error"])
    else:
        emoji = emotion_icons.get(result['emotion'], "🤔")

        # RESULT CARD
        st.markdown(f"""
        <div class="result-card">
            <h3>📊 Results</h3>
            <p><b>Emotion:</b> {emoji} {result['emotion'].capitalize()}</p>
            <p><b>Sentiment:</b> {result['sentiment'].capitalize()}</p>
            <p><b>Clarity:</b> {result['clarity'].capitalize()}</p>
            <p><b>Intent:</b> {result['intent'].replace("_"," ").capitalize()}</p>
            <p><b>Confidence:</b> {result['confidence']}%</p>
        </div>
        """, unsafe_allow_html=True)

        # PROGRESS BAR
        st.progress(result['confidence'] / 100)

        # SUGGESTION
        st.markdown(f"""
        <div class="suggestion">
            💡 <b>Suggestion:</b> {result['suggestion']}
        </div>
        """, unsafe_allow_html=True)