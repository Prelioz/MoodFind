import re
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

stop_words = set(stopwords.words('english'))

def preprocess(review):

    review = review.lower()

    review = re.sub(r'<.*?>', '', review)

    review = ''.join(
    char for char in review
    if char not in string.punctuation
    )

    review = review.split()

    review = [word for word in review if word not in stop_words]

    review = [lemmatizer.lemmatize(word) for word in review]

    review = ' '.join(review)

    return review


print(preprocess("This movie was AMAZING!!! <br /> I loved it."))


  



