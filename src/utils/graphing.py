import matplotlib.pyplot as plt
from numpy import array
from .processing import calculate_error

from enum import Enum
class figures(Enum):
    DATA = 1
    DATA_AND_TRUTH = 2
    ERROR = 3

def plot_data(raw_data : array, filtered_data : array):
    """
    Plots plots data and filtered output of data

    Args:
        raw_data (array): raw data fed into filter
        filtered_data (array): filter output of raw_data
    """
    idx = array([i for i in range(len(raw_data))])
    fig_id = figures.DATA
    plt.figure(fig_id.value)
    plt.plot(idx, raw_data, 'g', idx, filtered_data, 'b')
    plt.title("Raw Data and Filtered Data")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.legend(["Raw Data", "Filtered Data"])


def plot_error(reference_data : array, filtered_data : array):
    """
    Creates error plots of data
    
    Args:
        reference_data (array): reference data repreesntative of true values 
        filtered_data (array): filtered output of raw data (raw data is presumed to be noisy)
    """
    error = calculate_error(reference_data, filtered_data)
    idx = array([i for i in range(len(reference_data))])
    
    fig_id = figures.ERROR
    
    plt.figure(fig_id.value)
    plt.plot(idx, error, 'r')
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.legend(["Error"])
    plt.title("Error of Filtered data")

if __name__ == "__main__":
    raw = array([i for i in range(1000)])
    filt = raw + 100
    plot_error(raw, filt)
    plt.show()