import numpy as np

def calculate(list):

    mean = np.mean(list)
    variance = np.var(list)
    standard_deviation = np.std(list)
    maximum = np.max(list)
    minimum = np.min(list)

    return calculations