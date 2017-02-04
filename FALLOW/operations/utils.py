# Array operation utils
import numpy as np


def list_dict_to_dict(list_dict, init_dict):
    for a_dict in list_dict:
        key = a_dict.keys()[0]
        if isinstance(a_dict[key], dict):
            init_dict[key] = a_dict[key]
        else:
            init_dict[key] = {}
            sub_dict = init_dict[key]
            list_dict_to_dict(a_dict[key], sub_dict)
