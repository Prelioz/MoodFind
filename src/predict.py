import pickle
from .preprocess import preprocess_text

model = pickle.load(open("models/sentiment_model.pkl","rb"))

vectorizer = pickle.load(open("models/tfidf_vectorizer.pkl", "rb"))

def predict_sentiment(review):

    cleaned_review = preprocess_text(review)

    review_vector = vectorizer.transform([cleaned_review])

    probabilities = model.predict_proba(review_vector)[0]

    confidence = max(probabilities)

    if confidence < 0.6:
         return "Neutral", confidence, cleaned_review
    
    prediction = model.predict(review_vector)[0]

    sentiment =  "Positive" if prediction == 1 else "Negative"

    return sentiment, confidence, cleaned_review


if __name__ == "__main__":
     
   
     print(predict_sentiment("The acting was mediocre but the story was fantastic"))

     print(predict_sentiment("I regret wasting my time on this movie"))

     print(predict_sentiment("It was okay, not the best but not terrible"))



