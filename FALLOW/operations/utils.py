# Array operation utils
import numpy as np


def total(array):
    masked_data = np.ma.masked_where(array <= -9999, array)
    return  np.ma.sum(masked_data)


def standardize(array):
    masked_data = np.ma.masked_where(array <= -9999, array)
    max_value = masked_data.max()
    if max_value == 0:
        return 0.0 * max_value
    else:
        return masked_data/float(max_value)