import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(BASE_DIR, "data", "goemotions.csv")
output_path = os.path.join(BASE_DIR, "data", "clarity_dataset.csv")

df = pd.read_csv(data_path)

def get_clarity(text):
    text = str(text)
    words = text.split()
    length = len(words)

    if length <= 4:
        return "vague"
    elif length <= 8:
        return "moderate"

    keywords = ["exam", "job", "interview", "meeting", "test", "project", "deadline"]
    for word in keywords:
        if word in text.lower():
            return "clear"

    return "clear"

df['label'] = df['text'].apply(get_clarity)
clarity_df = df[['text', 'label']]

clarity_df.to_csv(output_path, index=False)

print("🔥 Improved clarity dataset created!")
print(f"Rows: {len(clarity_df)}")
print(clarity_df['label'].value_counts())