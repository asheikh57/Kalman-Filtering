from filter.hInfinityFilter import DenoiseHInfinityFilter
from utils.processing import *
from utils.graphing import plot_error, plot_data
import matplotlib.pyplot as plt

if __name__ == "__main__":
    data = array([i for i in range(1000)])
    fltr = DenoiseHInfinityFilter(-1,10,10,0)
    d = run_filter(data, fltr)
    print(calculate_rmse(calculate_error(data, d)))
    raw = array([i for i in range(1000)])
    filt = raw + 100
    plot_error(raw, filt)
    plot_data(raw, filt)
    plt.show()