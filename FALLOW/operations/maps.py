import sys
from osgeo import gdal
import numpy as np
from os import path
import pcraster


def mapopen(filename):
    if not path.isfile(filename):
        return None
    else:
        return gdal.Open(filename)


def map2array(data, masked_value):
    array = data.ReadAsArray().astype(np.float32)
    masked_array = np.ma.masked_where(array <= masked_value, array)
    return masked_array


def array2map(array, filename, prototype):
    data = array.astype(np.float32)
    data = np.ma.filled(data, fill_value=-9999)
    [cols, rows] = array.shape
    outdriver = gdal.GetDriverByName("GTiff")
    outdata = outdriver.Create(filename, rows, cols, 1, gdal.GDT_Float32)
    outdata.SetGeoTransform(prototype.GetGeoTransform())
    outdata.SetProjection(prototype.GetProjection())
    outdata.GetRasterBand(1).WriteArray(data, 0, 0)


def arraystat(array, mean, cv):
    rows, cols = array.shape
    return (mean +
            np.random.normal(0,1, [rows, cols]) * mean * cv)


def arrayuper(array, value):
    arraymax = np.full(array.shape, value, dtype=np.float32)
    return np.ma.maximum(array, arraymax)


def arraylower(array, value):
    arraymin = np.full(array.shape, value, dtype=np.float32)
    return np.ma.minimum(array, arraymin)


def arraytotal(array):
    return np.ma.sum(array)


def boolean2scalar(array):
    return 1.0 * array


def standardize(array):
    max_value = array.max()
    if max_value == 0:
        return 0*array
    else:
        return array/max_value


def stat(mean, cv):
    return mean + np.random.normal(0,1)*mean*cv


def arrayfull(array, value):
    return np.full(array.shape, value, dtype=np.float32)


def arrayfill(array, value):
    return np.ma.filled(array, value)

