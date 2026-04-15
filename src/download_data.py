from datasets import load_dataset
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
output_path = os.path.join(BASE_DIR, "data", "goemotions.csv")

print("Downloading dataset...")

dataset = load_dataset("go_emotions", "simplified")

texts = []
labels = []

for item in dataset["train"]:
    texts.append(item["text"])
    labels.append(item["labels"][0] if len(item["labels"]) > 0 else -1)

df = pd.DataFrame({
    "text": texts,
    "labels": labels
})

df.to_csv(output_path, index=False)

print("✅ Dataset downloaded successfully!")
print(f"Rows: {len(df)}")