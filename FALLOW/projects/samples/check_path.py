import json
import os

with open('maps.json', 'rb') as file:
    x_root = json.load(file)

# print json.dumps(x_root, indent=2)

def checkpath(list_dict):
    for e in list_dict:
        key = e.keys()[0]
        if isinstance(e[key], dict):
            if not os.path.isfile(e[key]['Path']):
                print key
            else:
                print 'pass: ' + key
        else:
            checkpath(e[key])

checkpath(x_root)