import pandas as pd

def factorize_feature(feature, na = -1):
    '''
    >>> factorize_feature(np.array(['A','B']))
    array([ 0, 1])
    :param feature: nd-array / categorical pandas variable
    :param na: what to replace missing values with
    :return: nd-array / categorical pandas variable of numeric values 
    '''

    factorized_feature = pd.factorize(feature, na_sentinel = na)[0]

    return factorized_feature


def bin_feature(feature, bins, labels=False):
    '''
    Figures out way to bin contiuous data
    :param feature: nd-array / pandas series
    :param bins: <int> nr of bins
    :param labels: for each bin
    :return: categorical variable
    '''

    binned_feature = pd.cut(feature, bins = bins, labels = labels),

    return binned_feature


def create_dummy_variables(categorical_column, data, exclude_column=False):
    dummies =  pd.get_dummies(data[categorical_column])
    data = pd.concat([data, dummies], axis=1)
    if exclude_column:
        data = data.drop(categorical_column, 1)
    return data