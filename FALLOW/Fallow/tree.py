

class Node(object):
    def __init__(self, name, parent=None ,**kwargs):
        if parent is not None:
            self._parent = parent
            parent.add_child(self)
        self._data = kwargs
        self._children = []
        self.name = name

    def add_child(self, node):
        self._children.append(node)

    def children(self):
        return self._children

    def child(self, row):
        return self._children[row]

    def parent(self):
        return self._parent

    def set_data(self, **kwargs):
        for key in kwargs.keys():
            self._data[key] = kwargs[key]

    def data(self):
        return self._data

    def rows(self):
        return len(self._children)

    def cols(self):
        return len(self._data.keys())

    def row(self):
        if self._parent is not None:
            return self._parent._children.index(self)

    def values(self):
        return [self.name] + self._data.values()

    def to_dict(self, init_dict):
        if not self.children():
            init_dict[self.name] = self.data()
        else:
            init_dict[self.name] = {}
            for child in self.children():
                child.to_dict(init_dict[self.name])

    def to_json(self, init_list):
        if not self.children():
            init_list.append({self.name: self.data()})
        else:
            sub_dict = {self.name: []}
            init_list.append(sub_dict)
            for child in self.children():
                child.to_json(sub_dict[self.name])

if __name__ == '__main__':
    import json
    from tree import Node
    from constants import maps

    with open('maps.json', 'rb') as file:
        x_root = json.load(file)
    root = Node('root')


    def make_node(parent, list_dict):
        for a_dict in list_dict:
            key = a_dict.keys()[0]
            if isinstance(a_dict[key], dict):
                Node(key, parent, **a_dict[key])
            else:
                sub_node = Node(key, parent)
                make_node(sub_node, a_dict[key])

    make_node(root, maps)

    d = {}
    root.to_dict(d)

    with open('1maps.json', 'wb') as file:
        json.dump(d, file)
