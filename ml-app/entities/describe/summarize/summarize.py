import pandas as pd

def dummy_percentage(feature):
    '''
    >>> dummy_percentage(np.array([0,0,1,1]))
    feature    50.0
    dtype: float64
    :param feature: pandas series
    :return: dataframe
    '''

    percentage = pd.DataFrame(feature.value_counts()).loc[1] * 100 / pd.DataFrame(feature.value_counts()).loc[0]

    return percentage