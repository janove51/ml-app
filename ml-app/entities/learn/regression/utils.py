import numpy as np

def evaluate_regressor(model, X_test, y_test):
    predictions = model.predict(X_test)
    errors = abs(predictions - y_test)
    mape = 100 * np.mean(errors / y_test)
    accuracy = 100 - mape
    avg_error = np.mean(errors)
    print('Model Performance')
    print('Average Error: {:0.4f} degrees.'.format())
    print('Accuracy = {:0.2f}%.'.format(accuracy))

    return accuracy, avg_error