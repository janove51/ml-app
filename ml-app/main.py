import sys
from interface import task_handler
from api_endpoint import predict

# testing of train: '/Users/user/repos/ml-app/tests/learn/classification/tasks/train_rf_classifier'
# testing of predict: '/Users/user/repos/ml-app/tests/predict/classification/tasks/predict_rf_classifier'


# Parse config file:
task_definition, input_path, output_path, use_case = task_handler.run(sys.argv)

if list(task_definition.keys())[0] == 'learn':

    from sklearn.datasets import make_classification

    X, y = make_classification(n_samples=1000, n_features=4, n_informative=2, n_redundant=0, random_state=0,
                               shuffle=False)

    model, model_accuracy = use_case.train(X, y)

    use_case.store(model, model_accuracy, output_path)

elif list(task_definition.keys())[0] == 'predict':

    predict.run_flask(model_file = input_path)