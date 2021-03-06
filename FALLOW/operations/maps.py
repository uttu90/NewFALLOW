import sys
from osgeo import gdal
import numpy as np
from os import path
import pcraster

masked_value = -9999


def mapopen(filename):
    if not path.isfile(filename):
        return None
    else:
        return gdal.Open(filename)


def map2array(data, masked_value=masked_value):
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


def scalar2boolean(array):
    return array == 1

# def standardize(array):
#     max_value = array.max()
#     if max_value == 0:
#         return 0*array
#     else:
#         return array/max_value


def stat(mean, cv):
    return mean + np.random.normal(0,1)*mean*cv


def arrayfull(array, value):
    return np.full(array.shape, value, dtype=np.float32)


def arrayfill(array, value):
    return np.ma.filled(array, value)


def total(array):
    masked_data = np.ma.masked_where(array <= -9999, array)
    return  np.ma.sum(masked_data)


def standardize(array):
    masked_data = np.ma.masked_where(array <= -9999, array)
    masked_data = masked_data.astype(np.float32)
    max_value = masked_data.max()
    if max_value == 0:
        return 0.0 * masked_data
    else:
        return masked_data/float(max_value)


def load_map(maps, init_dict):
    map_values = maps.values()[0]
    for map_dict in map_values:
        if 'path' in map_dict:
            init_dict[map_dict['name']] = map2array(mapopen(
                map_dict['path']), -9999
            )
        else:
            key = map_dict.keys()[0].lower()
            init_dict[key] = {}
            sub_dict = init_dict[key]
            load_map(map_dict, sub_dict)


def standardized_maps(maps, init_dict):
    for key in maps.keys():
        if isinstance(maps[key], dict):
            init_dict[key.lower()] = {}
            sub_dict = init_dict[key.lower()]
            standardized_maps(maps[key], sub_dict)
        else:
            init_dict[key] = standardize(maps[key])


def uniform(array, file_map='area.xxx'):
    [x, y] = array.shape
    rm = np.random.uniform(0, 1, (x, y))
    result = boolean2scalar(array) * rm
    result = np.ma.masked_where(result == 0, result)
    return result


def spreadmap(array, prototype):
    elevation = prototype.GetRasterBand(1).ReadAsArray()
    geoTransform = prototype.GetGeoTransform()
    # print band
    # elevation = band.ReadAsArray()
    # pcraster.setclone(file_map)
    pcraster.setclone(elevation.shape[0], elevation.shape[1], geoTransform[1],
                      geoTransform[0], geoTransform[3])
    sarray = 1.0 * array
    farr = np.ma.filled(sarray, -9999)
    n2p = pcraster.numpy2pcr(pcraster.Nominal, farr, -9999)
    n2p = pcraster.spread(n2p, 0, 1)
    p2n = pcraster.pcr2numpy(n2p, -9999)
    temp = np.ma.masked_where(p2n == -9999, p2n)
    return temp
