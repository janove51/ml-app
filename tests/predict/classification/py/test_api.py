import requests
import json
import codecs
import pandas as pd
import sys, os
sys.path.append(os.path.abspath('../../../../ml-app'))
from interface.prediction_api import server
from sklearn.datasets import make_classification


def test_endpoint(endpoint):
    '''
    Generates testing data for classification predctions endpoint for testing purpose
    :param endpoint: string, adress to the endpoint
    :return: flask object, api response
    '''
    # generate batch data to post to api in json format:
    X, y = make_classification(n_samples=2, n_features=4, n_informative=2,
                               n_redundant=0, random_state=0, shuffle=False)
    X = pd.DataFrame(X)
    input_data = X.to_json(orient='records')
    print('Clients payload:', input_data)

    # post test json to API endpoint
    response = requests.post(endpoint, json = input_data)

    #todo: check response is there
    #todo: get accuracy estimate

    print('Test result:', response, response.text)


test_endpoint(endpoint="http://127.0.0.1:5000/ml-app/v1.0/predict/")
