import requests
import json
import codecs
import pandas as pd
import sys, os
sys.path.append(os.path.abspath('../../../../ml-app'))
from interface.prediction_api import server
from sklearn.datasets import make_classification



## start the server and pass test model
model_file = '/Users/user/testing/ml-app/models/classifier/RF/test_model_1.pickle'
server.run(model_file, endpoint = '/ml-app/v1.0/predict/', probability = False)
