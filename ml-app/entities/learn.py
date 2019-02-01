from sklearn.ensemble import RandomForestClassifier
import numpy as np
### Hyperparameter tuning

# Random Forest
rfc = RandomForestClassifier(n_jobs=-1, oob_score = True)

def assemble_param_grid_rf(nr_trees_min=200, nr_trees_max=2000, nr_trees_options=10,
                           max_features_min=None, max_features_max=None, max_features_options=None,
                           max_depth_min=None, max_depth_max=None, max_depth_options=None,
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
    :return: 
    '''

    # Number of trees = size of the ensemble itself
    n_estimators = [int(x) for x in np.linspace(start=nr_trees_min, stop=nr_trees_max, num=nr_trees_options)]

    # Number of features: limit it to increase variance within ensemble
    if max_features_min==None and max_features_max==None and max_features_options==None:
        max_features = ['sqrt', 'log2']
    else:
        max_features = [int(x) for x in np.linspace(start=max_features_min, stop=max_features_max, num=max_features_options)]

    # Max Depth = controls model complexity
    max_depth = [int(x) for x in np.linspace(start=max_depth_min, stop=max_depth_max, num=max_depth_options)]
    max_depth.append(None)

    nr_combos = len(n_estimators) * len(min_samples_split) * len(max_features) * len(max_depth) * len(min_samples_leaf) * len(bootstrap_options)
    print('Grid contains {} possible combinations'.format(nr_combos))

    grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap_options}

    return grid