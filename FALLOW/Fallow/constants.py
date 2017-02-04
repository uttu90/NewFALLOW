# List of map keys
maps = [
    {'Simulated area': {'Path': '', 'Descitpion': ''}},
    {'Initial landcover': {'Path': '', 'Description': ''}},
    {'Sub-catchment area': {'Path': '', 'Description': ''}},
    {'Initial logging area': {'Path': '', 'Description': ''}},
    {'Soil fertility': [
        {'Initial soil fertility': {'Path': '', 'Description': ''}},
        {'Maximum soil fertility': {'Path': '', 'Description': ''}},]},
    {'Slope': {'Path': '', 'Description': ''}},
    {'Suitable area': [
        {'Annual crop 1': {'Path': '', 'Description': ''}},
        {'Annual crop 2': {'Path': '', 'Description': ''}},
        {'Annual crop 3': {'Path': '', 'Description': ''}},
        {'Annual crop 4': {'Path': '', 'Description': ''}},
        {'Tree-based system 1': {'Path': '', 'Description': ''}},
        {'Tree-based system 2': {'Path': '', 'Description': ''}},
        {'Tree-based system 3': {'Path': '', 'Description': ''}},
        {'Tree-based system 4': {'Path': '', 'Description': ''}},
        {'Tree-based system 5': {'Path': '', 'Description': ''}},
        {'Tree-based system 6': {'Path': '', 'Description': ''}},
        {'Tree-based system 7': {'Path': '', 'Description': ''}},
        {'Tree-based system 8': {'Path': '', 'Description': ''}},
    ]},
    {'Distance to road': [
        {'Period 1': {'Path': '', 'Description': ''}},
        {'Period 2': {'Path': '', 'Description': ''}},
        {'Period 3': {'Path': '', 'Description': ''}},
        {'Period 4': {'Path': '', 'Description': ''}},

    ]},
    {'Distance to market': [
        {'Period 1': {'Path': '', 'Description': ''}},
        {'Period 2': {'Path': '', 'Description': ''}},
        {'Period 3': {'Path': '', 'Description': ''}},
        {'Period 4': {'Path': '', 'Description': ''}},

    ]},
    {'Distance to river': [
        {'Period 1': {'Path': '', 'Description': ''}},
        {'Period 2': {'Path': '', 'Description': ''}},
        {'Period 3': {'Path': '', 'Description': ''}},
        {'Period 4': {'Path': '', 'Description': ''}},

    ]},
    {'Distance to factory': [
        {'Non-timber forest products': [
        {'Period 1': {'Path': '', 'Description': ''}},
        {'Period 2': {'Path': '', 'Description': ''}},
        {'Period 3': {'Path': '', 'Description': ''}},
        {'Period 4': {'Path': '', 'Description': ''}},
    ]},
        {'Timber': [
        {'Period 1': {'Path': '', 'Description': ''}},
        {'Period 2': {'Path': '', 'Description': ''}},
        {'Period 3': {'Path': '', 'Description': ''}},
        {'Period 4': {'Path': '', 'Description': ''}},
    ]},
        {'Annual crop 1': [
        {'Period 1': {'Path': '', 'Description': ''}},
        {'Period 2': {'Path': '', 'Description': ''}},
        {'Period 3': {'Path': '', 'Description': ''}},
        {'Period 4': {'Path': '', 'Description': ''}},

    ]},
        {'Annual crop 2': [
        {'Period 1': {'Path': '', 'Description': ''}},
        {'Period 2': {'Path': '', 'Description': ''}},
        {'Period 3': {'Path': '', 'Description': ''}},
        {'Period 4': {'Path': '', 'Description': ''}},

    ]},
        {'Annual crop 3': [
        {'Period 1': {'Path': '', 'Description': ''}},
        {'Period 2': {'Path': '', 'Description': ''}},
        {'Period 3': {'Path': '', 'Description': ''}},
        {'Period 4': {'Path': '', 'Description': ''}},

    ]},
        {'Annual crop 4': [
        {'Period 1': {'Path': '', 'Description': ''}},
        {'Period 2': {'Path': '', 'Description': ''}},
        {'Period 3': {'Path': '', 'Description': ''}},
        {'Period 4': {'Path': '', 'Description': ''}},

    ]},
        {'Tree-based system 1': [
        {'Period 1': {'Path': '', 'Description': ''}},
        {'Period 2': {'Path': '', 'Description': ''}},
        {'Period 3': {'Path': '', 'Description': ''}},
        {'Period 4': {'Path': '', 'Description': ''}},

    ]},
        {'Tree-based system 2': [
        {'Period 1': {'Path': '', 'Description': ''}},
        {'Period 2': {'Path': '', 'Description': ''}},
        {'Period 3': {'Path': '', 'Description': ''}},
        {'Period 4': {'Path': '', 'Description': ''}},

    ]},
        {'Tree-based system 3': [
        {'Period 1': {'Path': '', 'Description': ''}},
        {'Period 2': {'Path': '', 'Description': ''}},
        {'Period 3': {'Path': '', 'Description': ''}},
        {'Period 4': {'Path': '', 'Description': ''}},

    ]},
        {'Tree-based system 4': [
        {'Period 1': {'Path': '', 'Description': ''}},
        {'Period 2': {'Path': '', 'Description': ''}},
        {'Period 3': {'Path': '', 'Description': ''}},
        {'Period 4': {'Path': '', 'Description': ''}},

    ]},
        {'Tree-based system 5': [
        {'Period 1': {'Path': '', 'Description': ''}},
        {'Period 2': {'Path': '', 'Description': ''}},
        {'Period 3': {'Path': '', 'Description': ''}},
        {'Period 4': {'Path': '', 'Description': ''}},

    ]},
        {'Tree-based system 6': [
        {'Period 1': {'Path': '', 'Description': ''}},
        {'Period 2': {'Path': '', 'Description': ''}},
        {'Period 3': {'Path': '', 'Description': ''}},
        {'Period 4': {'Path': '', 'Description': ''}},

    ]},
        {'Tree-based system 7': [
        {'Period 1': {'Path': '', 'Description': ''}},
        {'Period 2': {'Path': '', 'Description': ''}},
        {'Period 3': {'Path': '', 'Description': ''}},
        {'Period 4': {'Path': '', 'Description': ''}},

    ]},
        {'Tree-based system 8': [
        {'Period 1': {'Path': '', 'Description': ''}},
        {'Period 2': {'Path': '', 'Description': ''}},
        {'Period 3': {'Path': '', 'Description': ''}},
        {'Period 4': {'Path': '', 'Description': ''}},

    ]},
    ]},
    {'Distance to settlement': [
        {'Period 1': {'Path': '', 'Description': ''}},
        {'Period 2': {'Path': '', 'Description': ''}},
        {'Period 3': {'Path': '', 'Description': ''}},
        {'Period 4': {'Path': '', 'Description': ''}},

    ]},
    {'Protected area': {'Path': '', 'Description': ''}},
    {'Disastered area': {'Path': '', 'Description': ''}},
]

def list_dict_to_dict(list_dict, init_dict):
    for a_dict in list_dict:
        key = a_dict.keys()[0]
        if isinstance(a_dict[key], dict):
            init_dict[key] = a_dict[key]
        else:
            init_dict[key] = {}
            sub_dict = init_dict[key]
            list_dict_to_dict(a_dict[key], sub_dict)

x = {}
list_dict_to_dict(maps, x)

import json

print json.dumps(x, indent=2)


time_series = [

]