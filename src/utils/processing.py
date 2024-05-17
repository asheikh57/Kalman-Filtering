from filter import *
from numpy import array, mean

def run_filter(data : array, filter):
    """
    Runs filter on data
    Args:
        data (list): measurements
        filter (FilterBase): filter being used

    Returns:
        ret (list float): a list of filtered data
    """
    
    ret = []
    for item in data:
        filter.kalman_iteration(item)
        ret.append(filter.state)
        
    return array(ret)

def calculate_error(data : array, filtered_data : array):
    """
    Calculates error at each data point
    Args:
        data (array): numpy array containing input data
        filtered_data (array): numpy array containing filtered data

    Returns:
        (array): numpy array of error at each datapoint
    """
    
    assert(len(filtered_data) == len(data))
    return data - filtered_data
    
def calculate_rmse(error : array):
    """
    Calculates root mean squared error from error time series
    Args:
        error (array): error time series

    Returns:
        (float) : root mean square error
    """
    
    return pow( mean( pow(error, 2) ) , 0.5)

