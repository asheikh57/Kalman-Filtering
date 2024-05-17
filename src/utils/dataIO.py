from numpy import genfromtxt, savetxt

def dataFromCsv(filepath):
    """

    Args:
        filepath (string): location of .csv file with data

    Returns:
        np.array: array with data from .csv
    """
    return genfromtxt(filepath, delimiter=',')

def dataToCsv(data, filepath):
    """
    writes/stores numpy array data to a .csv

    Args:
        data (numpy.array): data to be written
        filepath (string): output file path string 
    """
    savetxt(filepath, data, delimiter=',')

if __name__ == "__main__":
    print(dataFromCsv("src/utils/testout.csv"))
    #dataToCsv((dataFromCsv("src/utils/test.csv")), "src/utils/testout.csv")
    