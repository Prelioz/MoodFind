# 🎬 MoodFind

MoodFind is a Movie Review Sentiment Analysis application built using Natural Language Processing (NLP) and Machine Learning.

The application analyzes movie reviews and predicts whether the sentiment is:

- 😊 Positive
- 😐 Neutral
- 😠 Negative

---

## 🚀 Features

- Text preprocessing pipeline
  - Lowercasing
  - HTML tag removal
  - Punctuation removal
  - Stopword removal
  - Lemmatization

- TF-IDF Vectorization
- Logistic Regression Classifier
- Confidence Score Prediction
- Neutral Sentiment Detection
- Interactive Streamlit Web Application

---

## 🛠️ Tech Stack

### Languages
- Python

### Libraries
- Streamlit
- Scikit-Learn
- NLTK
- NumPy
- Pandas

### Machine Learning
- TF-IDF Vectorizer
- Logistic Regression

---

## 📂 Project Structure

```text
MoodFind/
│
├── app.py
│
├── models/
│   ├── sentiment_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── src/
│   ├── preprocess.py
│   └── predict.py
│
├── notebooks/
│   └── sentiment_analysis.ipynb
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <repository-url>
cd MoodFind
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

```bash
streamlit run app.py
```

---

## 📸 Example

### Input Review

```text
This movie was absolutely amazing!
```

### Preprocessed Review

```text
movie absolutely amazing
```

### Prediction

```text
😊 Positive (92.21%)
```

---

## 🧠 How It Works

1. User enters a movie review.
2. The review is preprocessed.
3. TF-IDF converts the text into numerical features.
4. Logistic Regression predicts sentiment probabilities.
5. Confidence score is calculated.
6. Reviews with low confidence are classified as Neutral.
7. The prediction is displayed through Streamlit.

---

## 📈 Future Improvements

- True 3-class sentiment classification
- N-gram feature engineering
- Transformer-based models (BERT)
- Deployment on Streamlit Cloud

---

## 👨‍💻 Author

**Bhavya Modi**

B.Tech, Dhirubhai Ambani University