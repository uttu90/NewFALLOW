import json
from tree import Node
from constants import maps

with open('maps.json', 'rb') as file:
    x_root = json.load(file)

# print x_root


root=Node('root')

def make_node(parent, list_dict):
    for a_dict in list_dict:
        key = a_dict.keys()[0]
        if isinstance(a_dict[key], dict):
            Node(key, parent, **a_dict[key])
        else:
            sub_node = Node(key, parent)
            make_node(sub_node, a_dict[key])

make_node(root, maps)

for child in root.children():
    print child.name
    pass

x = []
root.to_json(x)

x_root = x[0]['root']
import json

with open('xmaps.json', 'wb') as file:
    json.dump(x_root, file, indent=2)
# print len(root.children())