# 🧠 AI Emotion & Intent Analyzer

An advanced AI-powered system that analyzes human text to detect **Emotion, Sentiment, Clarity, Intent, and Confidence** using a hybrid approach (Machine Learning + Rule-based Intelligence).

---

## ✨ Features

- 🎯 **Emotion Detection**: Happy, Sad, Angry, Anxiety, Mixed
- 💬 **Sentiment Analysis**: Positive, Negative, Neutral
- 🧠 **Intent Detection**: Seeking Help, Question, Statement, Gratitude
- 🔍 **Clarity Detection**: Vague, Moderate, Clear
- 📊 **Confidence Score**: Dynamic and realistic confidence
- 🌍 **Multilingual Support**: English + Hinglish
- 🔥 **Mixed Emotion Detection**: Handles complex emotional cases
- 🎨 **Premium UI**: Built using Streamlit

---

## 🧠 How It Works

This system uses a **Hybrid AI Approach**:

### 1. Machine Learning
- Pre-trained models for base emotion prediction
- TF-IDF vectorization

### 2. Rule-Based Intelligence
- Keyword + phrase scoring
- Handles real-world inputs like:
  `"not sure"`, `"kya karu"`, `"tension ho rahi hai"`

### 3. Decision Engine
- Combines ML + rule scores
- Detects **mixed emotions**
- Generates **realistic confidence**

---

## 📁 Project Structure

```
emotion-analyzer/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── clarity_dataset.csv
│   └── goemotions.csv
│
├── models/
│   ├── emotion_model.pkl
│   ├── emotion_vectorizer.pkl
│   ├── clarity_model.pkl
│   └── vectorizer.pkl
│
└── src/
    ├── __init__.py
    ├── download_data.py
    ├── generate_clarity_data.py
    ├── train_clarity.py
    ├── train_emotion.py
    ├── preprocess.py
    └── predict.py
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/emotion-analyzer.git
cd emotion-analyzer
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

**Activate:**

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the Project

```bash
streamlit run app.py
```

👉 **Open in browser:**

```
http://localhost:8501
```

---

## 🧪 Example Inputs

- **I got the job but I feel nervous**  
  → Mixed (happy + anxiety)

- **bhai mujhe samajh nahi aa raha kya karu**  
  → Anxiety + Seeking Help

- **I am really happy with my progress**  
  → Happy + Positive

---

## 📊 Output Includes

- Emotion 😊
- Sentiment 📊
- Clarity 🔍
- Intent 🎯
- Confidence %
- Suggestion 💡

---

## 🔥 Advanced Capabilities

- Handles real-world messy text
- Supports Hinglish input
- Detects uncertainty (not sure, confused)
- Identifies mixed emotions
- Provides context-aware suggestions

---

## 🛠 Tech Stack

- Python 🐍
- Scikit-learn
- Pandas
- Streamlit
- NLP (TF-IDF + Rule Engine)

---

## 🚀 Future Improvements

- LLM integration
- Voice input support
- API deployment

---

## 👨‍💻 Author

Satyam Kumar

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

For questions or support, please open an issue on GitHub.

---

*Built with ❤️ using Python, Scikit-learn, and Streamlit*
Emotion 😊
Sentiment 📊
Clarity 🔍
Intent 🎯
Confidence %
Suggestion 💡
🔥 Advanced Capabilities
Handles real-world messy text
Supports Hinglish input
Detects uncertainty (not sure, confused)
Identifies mixed emotions
Provides context-aware suggestions
🛠 Tech Stack
Python 🐍
Scikit-learn
Pandas
Streamlit
NLP (TF-IDF + Rule Engine)
🚀 Future Improvements
LLM integration (GPT-based reasoning)
Voice input support
Emotion timeline tracking
API deployment
👨‍💻 Author

Satyam Kumar