import pandas as pd
import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from src.preprocess import clean_text

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(BASE_DIR, "data", "goemotions.csv")

# Load dataset
df = pd.read_csv(data_path)

# Parse labels safely
def parse_labels(label_str):
    label_str = str(label_str).replace("[", "").replace("]", "").strip()
    if label_str == "":
        return []
    return [int(x) for x in label_str.split() if x.isdigit()]

df['labels'] = df['labels'].apply(parse_labels)

# Emotion mapping (0–26 only)
emotion_map = {
    0: "admiration", 1: "amusement", 2: "anger", 3: "annoyance",
    4: "approval", 5: "caring", 6: "confusion", 7: "curiosity",
    8: "desire", 9: "disappointment", 10: "disapproval", 11: "disgust",
    12: "embarrassment", 13: "excitement", 14: "fear", 15: "gratitude",
    16: "grief", 17: "joy", 18: "love", 19: "nervousness",
    20: "optimism", 21: "pride", 22: "realization", 23: "relief",
    24: "remorse", 25: "sadness", 26: "surprise"
}

def get_emotion(label_list):
    for label in label_list:
        if label in emotion_map:
            return emotion_map[label]
    return None

df['emotion'] = df['labels'].apply(get_emotion)

# Simplify
def simplify(emotion):
    if emotion in ["joy", "love", "excitement", "optimism"]:
        return "happy"
    elif emotion in ["sadness", "grief", "disappointment", "remorse"]:
        return "sad"
    elif emotion in ["anger", "annoyance", "disgust"]:
        return "angry"
    elif emotion in ["fear", "nervousness"]:
        return "anxiety"
    else:
        return None

df['label'] = df['emotion'].apply(simplify)

# Drop invalid rows
df = df.dropna(subset=['label'])

# Clean text
df['text'] = df['text'].apply(clean_text)

# Features
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(df['text'])
y = df['label']

# Model
model = LogisticRegression(max_iter=500, class_weight="balanced")
model.fit(X, y)

# Save
model_path = os.path.join(BASE_DIR, "models", "emotion_model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "models", "emotion_vectorizer.pkl")

pickle.dump(model, open(model_path, "wb"))
pickle.dump(vectorizer, open(vectorizer_path, "wb"))

print("✅ Emotion model trained successfully!")
print(f"Training samples: {len(df)}")