import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
nltk.download('punkt')
nltk.download('stopwords')
def preprocess(text):
    text=text.lower()
    words=word_tokenize(text)
    stop_words=set(stopwords.words('english'))
    filtered_words=[
        word for word in words
        if word not in stop_words and word not in string.punctuation
    ]
    return " ".join(filtered_words)