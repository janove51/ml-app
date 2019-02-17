from sklearn import metrics
from sklearn.model_selection import StratifiedShuffleSplit



def train_test_split(X=None, y=None, random_state=None,
                     split_method='StratifiedShuffleSplit', n_splits=2, test_size=0.3):
    '''
    Splits dataframe into train and test set for model evaluation
    :param df: pandas dataframe
    :param features: <list>
    :param dependent_variable: <str>
    :param random_state: <int> fix seed for reproducability, random by default
    :param split_method: <str> which sci-kit method to use for split
    :param n_splits: <int> nr of splits
    :param test_size: <float> percentage points 0.1 = 10% of obs into test -> 90% into train
    :return: nd-arrays of splits for train and test
    '''

    if split_method == 'StratifiedShuffleSplit':
        sss = StratifiedShuffleSplit(n_splits=n_splits, test_size=test_size, random_state=random_state)
        sss.get_n_splits(X, y)
    else:
        raise Exception('Invalid split method {}. Expecting: "StratifiedShuffleSplit"')

    for train_index, test_index in sss.split(X, y):
        X_train, X_test = X[train_index], X[test_index]  # numpy has different index convention than pandas
        y_train, y_test = y[train_index], y[test_index]

    return X_train, X_test, y_train, y_test




def randomly_refit_model(df, features, dependent_variable, estimator, n_iterations=5, metric='recall'):
    '''
    Bootsraps / resamples from df, then fits and predicts on test set n times to assess the variance of the accuracy
    :param df: Dataframe containing both feature and dependent variable
    :param estimator: scikit object of the specified model
    :param n_iterations: <int> how often the model will be re-fit
    :param test_size: <float64> fraction of the test dataset
    :return: <list> all the accuracy scores, one for each iteration
    '''

    #TODO: consider the class sklearn.cross_validation.Bootstrap method

    print("Number of times the model {} will be re-fitted and evaluated:".format(estimator), n_iterations)

    # randomly re-sample:
    stats = list()
    for i in range(n_iterations):

        # randomly split data
        X_train, X_test, y_train, y_test = train_test_split(df, features, dependent_variable)


        # fit model (plug in hyperparameters)
        clf = estimator.fit(X_train, y_train)

        # evaluate model
        predictions = clf.predict(X_test)
        if metric is 'recall':
            score = metrics.recall_score(y_test, predictions)
        elif metric is 'accuracy':
            metrics.accuracy_score(y_test, predictions.round())
        else:
            raise Exception("{} not a valid metric input. Expecting: 'recall' or 'accuracy'.".format(metric))

        stats.append(score)

    return stats