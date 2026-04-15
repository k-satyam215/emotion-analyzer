import re
import nltk
from nltk.corpus import stopwords

try:
    stopwords.words('english')
except:
    nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def clean_text(text):
    if not text:
        return ""

    # Lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)

    # Remove numbers & special chars
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Tokenize
    words = text.split()

    # Remove stopwords + very short words
    words = [word for word in words if word not in stop_words and len(word) > 2]

    return " ".join(words)