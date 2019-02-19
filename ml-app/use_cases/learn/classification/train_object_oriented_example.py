import os, sys
sys.path.append(os.path.abspath('../../../entities/learn'))
print(os.path.abspath('../../../entities/learn'))
import classification.utils
import classification.model
import pickle
import datetime
import time
current_time = time.time()
current_timestamp = datetime.datetime.fromtimestamp(current_time).strftime('%Y-%m-%d %H:%M:%S')
######## RF classifier: ########
from sklearn.datasets import make_classification

# generate 2d classification dataset for testing
X, y = make_classification(n_samples=1000, n_features=4, n_informative=2, n_redundant=0, random_state=0, shuffle=False)


class classifier():

    def __init__(self, model_name, file_path, X, y):
        self.model_name = model_name
        self.file_path = file_path
        self.X = X
        self.y = y
        self.current_timestamp = current_timestamp

    def train(self):

        # split data
        X_train, self.X_test, y_train, self.y_test = classification.utils.train_test_split(self.X, self.y)

        # tune model
        grid = classification.model.assemble_param_grid_rfc()

        # train model
        self.model = classification.model.train_rfc(X_train, y_train, grid, grid_search_type = 'random')

    def evaluate(self):
        # evaluate model
        self.model_accuracy = classification.utils.evaluate_classifier(self.model, self.X_test, self.y_test, metric='Brier_score')

    def store(self, model, current_timestamp):
        # store model
        output = {"model":model,
                  "accuracy":self.model_accuracy,
                  "created_date": current_timestamp}

        with open("{}{}.pickle".format(self.file_path, self.model_name), "wb") as trained_model:

            pickle.dump(trained_model)

    def run(self):
        classifier.train()
        classifier.evaluate()
        classifier.store()


classifier = classifier()
classifier.run()