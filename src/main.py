from filter.hInfinityFilter import DenoiseHInfinityFilter
from utils.processing import *

if __name__ == "__main__":
    data = array([i for i in range(1000)])
    fltr = DenoiseHInfinityFilter(-1,10,10,0)
    d = run_filter(data, fltr)
    print(calculate_rmse(calculate_error(data, d)))