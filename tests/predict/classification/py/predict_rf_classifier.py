import requests
import json
import codecs
from sklearn.datasets import make_classification

# generate prediction data
X, y = make_classification(n_samples=1, n_features=4, n_informative=2, n_redundant=0, random_state=0,
                           shuffle=False)

features = X.tolist()


response = requests.post("http://ml-app/v1.0/predict:5000/", json = features, por)

# print(response.json())