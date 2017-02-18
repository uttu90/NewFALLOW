# Array operation utils
import re


def make_key(key):
    return re.split(r'.?\(', key ) [0].strip().lower()


def list_dict_to_dict(list_dict, init_dict):
    for a_dict in list_dict:
        key = a_dict.keys()[0]
        if isinstance(a_dict[key], dict):
            init_dict[key] = a_dict[key]
        else:
            init_dict[key] = {}
            sub_dict = init_dict[key]
            list_dict_to_dict(a_dict[key], sub_dict)


def map_to_list_dict(init, keys_map, key_ref):
    for idx, key in enumerate(key_ref):
        if isinstance(key, dict):
            sub_list = []
            sub_key = key.keys()[0]
            init.append({sub_key: sub_list})
            map_to_list_dict(sub_list, keys_map[sub_key], key[sub_key])
        else:
            init.append({key: keys_map[key]})
