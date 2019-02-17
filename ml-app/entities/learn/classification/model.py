import os, sys
sys.path.append(os.path.abspath('../'))
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn import metrics
import numpy as np
import classification.utils


def assemble_param_grid_rfc(nr_trees_min=200, nr_trees_max=2000, nr_trees_options=10,
                           max_features_min=None, max_features_max=None, max_features_options=None,
                           max_depth_min=1, max_depth_max=32, max_depth_options=6,
                           bootstrap_options = [True, False], min_samples_split = [2, 5, 10], min_samples_leaf = [1, 2, 4]):
    '''
    Generates grid with value options for optimal Hyperparameter search of RandomForestClassifier
    :param nr_trees_min: 
    :param nr_trees_max: 
    :param nr_trees_options: 
    :param max_features_min: 
    :param max_features_max: 
    :param max_features_options: 
    :param bootstrap_options: 
    :param min_samples_split: 
    :param min_samples_leaf:     
    :return: grid for optimizing random forest model
    '''

    # Number of trees = size of the ensemble itself
    n_estimators = [int(x) for x in np.linspace(start=nr_trees_min, stop=nr_trees_max, num=nr_trees_options)]

    # Number of features: limit it to increase variance within ensemble
    if max_features_min is None and max_features_max is None and max_features_options is None:
        max_features = ['sqrt', 'log2']     # default value
    else:
        max_features = [int(x) for x in np.linspace(start=max_features_min, stop=max_features_max, num=max_features_options)]

    # Max Depth = controls model complexity
    if max_depth_min is None and max_depth_max is None and max_depth_options is None:
        max_depth = None     # default value
    else:
        max_depth = [int(x) for x in np.linspace(start=max_depth_min, stop=max_depth_max, num=max_depth_options)]


    nr_combos = len(n_estimators) * len(min_samples_split) * len(max_features) * len(max_depth) * len(min_samples_leaf) * len(bootstrap_options)
    print('Grid contains {} possible combinations'.format(nr_combos))

    grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap_options}

    print('Hyperparameter Grid assembled:', grid)

    return grid

# Random Forest
def train_rfc(X_train, y_train, grid, grid_search_type = 'random'):

    rfc = RandomForestClassifier(n_jobs=-1, bootstrap=True)

    if grid_search_type == 'random':
        grid_search = RandomizedSearchCV(estimator=rfc, param_distributions=grid,
                                   n_iter=2, cv=2, verbose=0, random_state=0, n_jobs=1)
    elif grid_search_type == 'all':
        grid_search = GridSearchCV(estimator=rfc, param_grid=grid, cv=2, n_jobs=1, verbose=0)

    grid_search.fit(X_train, y_train)

    print('Best Parameter grid:', grid_search.best_params_)

    model = grid_search.best_estimator_

    return model


def evaluate_classifier(model, X_test, y_test, metric):

    metric_output = {}

    # Assumes binary problem and 1 to be the target value!
    if metric == 'brier_score':
        predictions = model.predict_proba(X_test)[:,1]
        metric_value = round(metrics.brier_score_loss(y_test, predictions), 3)

    metric_output[metric] = metric_value

    return metric_output


######## 1st Use Case: Testing ########
from sklearn.datasets import make_classification

# generate 2d classification dataset for testing
X, y = make_classification(n_samples=1000, n_features=4, n_informative=2, n_redundant=0, random_state=0, shuffle=False)

# split data
X_train, X_test, y_train, y_test = classification.utils.train_test_split(X, y)

# tune model
grid = assemble_param_grid_rfc()

model = train_rfc(X_train, y_train, grid, grid_search_type = 'random')

# evaluate model
model_accuracy = evaluate_classifier(model, X_test, y_test, metric = 'brier_score')
print("Model accuracy:", model_accuracy)
