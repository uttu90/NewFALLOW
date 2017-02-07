import xlrd as wb

from FALLOW import constants

import json
import re

file_path = "Book1.xls"

book = wb.open_workbook(file_path)

sheet = book.sheet_by_name('Sheet1')

def read_multicol(sheet, start_col, col_num, start_row, end_row):
    data_list =  [sheet.col_values(i, start_rowx=start_row, end_rowx=end_row)
               for i in range(start_col, start_col + col_num)]
    return zip(*data_list)


def make_dict_from_list(keys, values):
    result = dict()
    if len(keys) != len(values):
        raise ValueError("keys and values should be same in length")
    else:
        for i in range(len(keys)):
            result[keys[i].lower()] = values[i]
    return result


def make_dict_from_list_extension(key_list, extensions, values):
    if len(extensions) != 0:
        if len(key_list) != len(values) or len(extensions) != len(values[0]):
            raise ValueError('keylist and values must be same in length or'
                             'extension and values[0] must be same in length ')
        else:
            result = {}
            index = 0
            for key in key_list:
                result[key.lower()] = {
                    extensions[i].lower(): values[index][i] for i in
                    range(len(extensions))
                    }
                index += 1
            return result
    else:
        result = make_dict_from_list(key_list, values)
        return result


def make_dict_from_keys_map(keys_map, values):
    result = {}
    index = 0
    for key in keys_map:
        try:
            if isinstance(key, dict):
                sub_dict = dict()
                index += 1
                for sub_key in key.values()[0]:
                    sub_dict[sub_key.lower()] = values[index]
                    index += 1
                result[key.keys()[0].lower()] = sub_dict
            else:
                result[key.lower()] = values[index]
                index += 1

        except IndexError:
            print index
    return result


def make_dict_from_keys_map_extension(keys_map, extensions, values):
    """

    :param keys_map:
    :param extensions:
    :param values:
    :return:
    """
    if len(extensions) != 0:
        if len(extensions) != len(values[0]):
            raise ValueError("extensions and values[0] must be same in"
                             "length")
        else:
            index = 0
            result = dict()
            for key in keys_map:
                try:
                    if isinstance(key, dict):
                        sub_dict = dict()
                        index += 1
                        for sub_key in key.values()[0]:
                            sub_dict[sub_key.lower()] = {
                                extensions[i].lower(): values[index][i]
                                for i in range(len(extensions))
                                }
                            index += 1
                        result[key.keys()[0].lower()] = sub_dict
                    else:
                        result[key.lower()] = {
                            extensions[i].lower(): values[index][i]
                            for i in range(len(extensions))
                            }
                        index += 1

                except IndexError:
                    print index
            return result
    else:
        result = make_dict_from_keys_map(keys_map, values)
        return result


def _make_key(key):
    return re.split(r'.?\(', key)[0].strip().lower()


def read_table(sheet, key_maps, start_col, end_col,
               start_row, middle_row, end_row):
    d = {}
    for col in range(start_col, end_col):
        current_dict = d
        keys = sheet.col_values(col, start_row, middle_row)
        values = sheet.col_values(col, middle_row, end_row)
        for index, key in enumerate(keys):
            if key:
                pretty_key = _make_key(key)
                if pretty_key not in current_dict:
                    if index == len(keys) - 1 or not keys[index+1]:
                        current_dict[pretty_key] = \
                            make_dict_from_keys_map(key_maps, values)
                        break
                    else:
                        current_dict[pretty_key] = {}
                current_dict = current_dict[pretty_key]

    return d


x = read_table(sheet, constants.landuse, 3, 5, 4, 5, 20)

# print json.dumps(x, indent=2)

biophysic1 = read_table(sheet, constants.landcover, 1, 16, 24, 27, 77)

initial_landcover_age = biophysic1['landcover age']['initial landcover age']

biophysic2 = read_table(sheet, constants.livelihood, 1, 13, 81, 83, 98)
print biophysic2.keys()

econimic1 = read_table(sheet, constants.livelihood, 1, 17, 102, 105, 120)
print econimic1.keys()

economic2 = read_table(sheet, constants.livelihood_age, 3, 5, 122, 124, 175)

social = read_table(sheet, constants.livelihood, 3, 6, 178, 180, 195)

demography = read_table(sheet, constants.demography_para, 4, 5, 199, 200, 206)


farmer_property1 = read_table(sheet, constants.farmer_property_para,
                             4, 6, 209, 210, 214)

social2 = read_table(sheet, constants.social_disaster_para,
                              3, 4,215, 216, 224)

yieldstat = biophysic1['landcover property']['yield']

print json.dumps(yieldstat, indent=2)