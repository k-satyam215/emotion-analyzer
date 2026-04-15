import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
from src.preprocess import clean_text

# Fix path dynamically 🔥
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(BASE_DIR, "data", "clarity_dataset.csv")

# Load data
df = pd.read_csv(data_path)
df['text'] = df['text'].apply(clean_text)

# Features
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['label']

# Model
model = LogisticRegression(max_iter=500, class_weight="balanced")
model.fit(X, y)

# Save paths
model_path = os.path.join(BASE_DIR, "models", "clarity_model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "models", "vectorizer.pkl")

pickle.dump(model, open(model_path, "wb"))
pickle.dump(vectorizer, open(vectorizer_path, "wb"))

print("Clarity model trained ✅")