import os, sys
sys.path.append(os.path.abspath('./entities/learn'))
print(os.path.abspath('./entities/learn'))
import classification.utils
import classification.model
import pickle
import datetime
import time

######## RF classifier: ########


def train(X, y):

    # generate 2d classification dataset for testing

    # split data
    X_train, X_test, y_train, y_test = classification.utils.train_test_split(X, y)

    # tune model
    grid = classification.model.assemble_param_grid_rfc()

    # train model
    model = classification.model.train_rfc(X_train, y_train, grid, grid_search_type='random')

    model_accuracy = classification.utils.evaluate_classifier(model, X_test, y_test, metric='brier_score')

    print('Model training done. Accuracy: ', model_accuracy)

    return model, model_accuracy



def store(model, model_accuracy, output_path):

    current_time = time.time()
    current_timestamp = datetime.datetime.fromtimestamp(current_time).strftime('%Y-%m-%d %H:%M:%S')

    output = {"model": model,
              "accuracy": model_accuracy,
              "created_datetime": current_timestamp}

    with open("{}.pickle".format(output_path), "wb") as pickle_out:

            pickle.dump(output, pickle_out, protocol = pickle.HIGHEST_PROTOCOL)

    print(model, " stored under", output_path)