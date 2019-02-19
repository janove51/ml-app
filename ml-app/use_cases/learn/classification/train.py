import os, sys
sys.path.append(os.path.abspath('../../../entities/learn'))
print(os.path.abspath('../../../entities/learn'))
import classification.utils
import classification.model
import pickle
import datetime
import time

######## RF classifier: ########
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=1000, n_features=4, n_informative=2, n_redundant=0, random_state=0, shuffle=False)


def train(X, y):

    # generate 2d classification dataset for testing

    # split data
    X_train, X_test, y_train, y_test = classification.utils.train_test_split(X, y)

    # tune model
    grid = classification.model.assemble_param_grid_rfc()

    # train model
    model = classification.model.train_rfc(X_train, y_train, grid, grid_search_type='random')

    model_accuracy = classification.utils.evaluate_classifier(model, X_test, y_test, metric='brier_score')

    return model, model_accuracy



def store(model, model_accuracy, file_path, model_name):

    current_time = time.time()
    current_timestamp = datetime.datetime.fromtimestamp(current_time).strftime('%Y-%m-%d %H:%M:%S')

    output = {"model":model,
              "accuracy":model_accuracy,
              "created_date": current_timestamp}

    with open("{}{}.pickle".format(file_path, model_name), "wb") as trained_model:

            pickle.dump(trained_model)



