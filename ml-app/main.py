import sys
from interface import task_handler


# for testing:
# config_file = '/Users/user/repos/ml-app/tests/learn/classification/tasks/test_rf_classifier'

task_definition, input_path, output_path, use_case = task_handler.run(sys.argv)

from sklearn.datasets import make_classification

X, y = make_classification(n_samples=1000, n_features=4, n_informative=2, n_redundant=0, random_state=0,
                           shuffle=False)

model, model_accuracy = use_case.train(X, y)

use_case.store(model, model_accuracy, output_path)