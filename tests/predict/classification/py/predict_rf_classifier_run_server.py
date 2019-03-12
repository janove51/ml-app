import requests
import json
import codecs
import pandas as pd
import sys, os
sys.path.append(os.path.abspath('../../../../ml-app'))
from interface.prediction_api import server
from sklearn.datasets import make_classification


# generate batch data to post to api in json format:
X, y = make_classification(n_samples=1, n_features=4, n_informative=2, n_redundant=0, random_state=0,
                           shuffle=False)
X = pd.DataFrame(X)
input_data = X.to_json(orient='records')
print('Clients payload:', input_data)


## start the server and pass test model
model_file = '/Users/user/testing/ml-app/models/classifier/RF/test_model_1.pickle'
server.run(model_file)


# post test json to API endpoint
response = requests.post("http://ml-app/v1.0/predict:5000/", json = input_data)
print('Server response:', response.json())