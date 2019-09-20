import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import movie_reviews
from sklearn.feature_extraction.text import CountVectorizer
from Study import study,studies,load_obj
import pickle

def process_data(data):
    ps = PorterStemmer()
    stop_words = set(stopwords.words("english"))
    [stop_words.add(add) for add in [".",",","[","]","the",")","(",";"]]
    data = [word.lower() for word in word_tokenize(data) if word not in stop_words ]

    al_words = nltk.FreqDist(data)
    common = al_words.most_common(50)
    print(common)
    common = [com for com in common if len(com) < 3]
    all_words = [al for al in al_words if al not in common]
    temp = nltk.FreqDist(all_words)
    print(temp.most_common(50))
    matrix = CountVectorizer(max_features=10)
    X = matrix.fit_transform(all_words).toarray()
    print(X)
# ref to let count ratio

med = load_obj("weed")
# process_data(med.all_studies[0].rawcont["Abstract"])
process_data(med.all_studies[0].combine_text())