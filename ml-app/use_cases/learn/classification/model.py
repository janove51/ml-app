import os, sys
sys.path.append(os.path.abspath('../../../entities/learn'))
print(os.path.abspath('../../../entities/learn'))
import classification.utils
import classification.model
from sklearn.externals import joblib

######## RF classifier: ########
from sklearn.datasets import make_classification


# generate 2d classification dataset for testing
X, y = make_classification(n_samples=1000, n_features=4, n_informative=2, n_redundant=0, random_state=0, shuffle=False)

# split data
X_train, X_test, y_train, y_test = classification.utils.train_test_split(X, y)

# tune model
grid = classification.model.assemble_param_grid_rfc()

# train model
model = classification.model.train_rfc(X_train, y_train, grid, grid_search_type = 'random')

# evaluate model
model_accuracy = classification.utils.evaluate_classifier(model, X_test, y_test, metric = 'brier_score')
print("Model accuracy:", model_accuracy)

# store model
