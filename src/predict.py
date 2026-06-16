import pickle
from preprocess import preprocess_text

model = pickle.load(open("../models/sentiment_model.pkl","rb"))

vectorizer = pickle.load(open("../models/tfidf_vectorizer.pkl", "rb"))

def predict_sentiment(review):

    review = preprocess_text(review)

    review_vector = vectorizer.transform([review])

    probabilities = model.predict_proba(review_vector)[0]

    confidence = max(probabilities)

    if confidence < 0.6:
         return "Neutral"
    
    prediction = model.predict(review_vector)[0]

    return "Positive" if prediction == 1 else "Negative"


if __name__ == "__main__":
     
   
     print(predict_sentiment("The acting was mediocre but the story was fantastic"))

     print(predict_sentiment("I regret wasting my time on this movie"))

     print(predict_sentiment("It was okay, not the best but not terrible"))



