from filter.adaptiveDenoiseKF import *
from filter.denoiseKF import *
from filter.filterbase import *
from filter.hInfinityFilter import *
from utils.processing import *
from utils.graphing import *
from utils.dataIO import *
import matplotlib.pyplot as plt
from tkinter import *


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