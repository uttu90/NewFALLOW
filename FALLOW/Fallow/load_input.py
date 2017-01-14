import xlrd as wb
import json

file_path = "C:\\Python27\\FALLOW - Input parameters.xls"

book = wb.open_workbook(file_path)

sheet = book.sheet_by_name('Summary')

land_use_options = sheet.col_values(0, start_rowx=6, end_rowx=20)
systems2 = sheet.col_values(0, start_rowx=102, end_rowx=117)
land_use = {}
# land_use['rotation'] = sheet.col_values(3, start_rowx=6, end_rowx=20)
# land_use['allow change'] = sheet.col_values(4, start_rowx=6, end_rowx=20)




# land_use['rotation'] = make_dict_value(land_use_options, sheet.col_values(3, start_rowx=5, end_rowx=19))
# land_use['allow change'] = make_dict_value(land_use_options, sheet.col_values(4, start_rowx=5, end_rowx=19))

bio_parameters = dict()

keys_map = ['settlement', {'forest': ['pioneer', 'young secondary', 'old secondary', 'primary']},
           'annual crop 1', 'annual crop 2', 'annual crop 3', 'annual crop 4',
           {'tree-based system 1': ('pioneer', 'early production', 'peak production', 'post production')},
           {'tree-based system 2': ['pioneer', 'early production', 'peak production', 'post production']},
           {'tree-based system 3': ['pioneer', 'early production', 'peak production', 'post production']},
           {'tree-based system 4': ['pioneer', 'early production', 'peak production', 'post production']},
           {'tree-based system 5': ['pioneer', 'early production', 'peak production', 'post production']},
           {'tree-based system 6': ['pioneer', 'early production', 'peak production', 'post production']},
           {'tree-based system 7': ['pioneer', 'early production', 'peak production', 'post production']},
           {'tree-based system 8': ['pioneer', 'early production', 'peak production', 'post production']}]

keys_map2 = ['off-/Non-farm', 'non-timber forest product',
             {'timber': ['pioneer', 'young secondary', 'old secondary', 'primary']},
           'annual crop 1', 'annual crop 2', 'annual crop 3', 'annual crop 4',
           {'tree-based system 1': ('pioneer', 'early production', 'peak production', 'post production')},
           {'tree-based system 2': ['pioneer', 'early production', 'peak production', 'post production']},
           {'tree-based system 3': ['pioneer', 'early production', 'peak production', 'post production']},
           {'tree-based system 4': ['pioneer', 'early production', 'peak production', 'post production']},
           {'tree-based system 5': ['pioneer', 'early production', 'peak production', 'post production']},
           {'tree-based system 6': ['pioneer', 'early production', 'peak production', 'post production']},
           {'tree-based system 7': ['pioneer', 'early production', 'peak production', 'post production']},
           {'tree-based system 8': ['pioneer', 'early production', 'peak production', 'post production']}]


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

def make_dict_value_from_keysmap_probality(keys_map, values):
    '''

    :param keys_map:
    :param values:
    :return:
    '''
    index = 0
    result = dict()
    for key in keys_map:
        try:
            if isinstance(key, dict):
                sub_dict = dict()
                index += 1
                for sub_key in key.values()[0]:
                    sub_dict[sub_key.lower()] = {'mean': values[index][0], 'cv': values[index][1]}
                    index += 1
                result[key.keys()[0].lower()] = sub_dict
            else:
                result[key.lower()] = {'mean': values[index][0], 'cv': values[index][1]}
                index += 1

        except IndexError:
            print index
    return result

value1 = sheet.col_values(2, start_rowx=26, end_rowx=76)
value2 = sheet.col_values(3, start_rowx=26, end_rowx=76)

# values = []
#
# for i in range(len(value1)):
#     values.append([value1[i], value2[i]])

values = zip(value1, value2)

test = make_dict_value_from_keysmap_probality(keys_map, values)

print json.dumps(test, indent=4, sort_keys=True)


def make_dict_from_keys_map_extension(keys_map, extensions, values):
    '''

    :param keys_map:
    :param extensions:
    :param values:
    :return:
    '''
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
                                for i in range (len(extensions))
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


values = zip(value1, value2)
extension = ['mean', 'cv']
# test = make_dict_value_from_keysmap_probality(keys_map, values)
test1 = make_dict_from_keys_map_extension(keys_map, extension, values)
print json.dumps(test, indent=4, sort_keys=True)

print test == test1

def make_dict_from_list(keys, values):
    result = dict()
    if len(keys) != len(values):
        raise "keys and values should be same in length"
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
                    range(len(key_list))
                    }
                index += 1
            return result
    else:
        result = make_dict_from_list(key_list, values)
        return result
