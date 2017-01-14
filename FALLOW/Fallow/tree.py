

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

    def to_json(self, init_list):
        if not self.children():
            init_list.append({self.name: self.data()})
        else:
            sub_dict = {self.name: []}
            init_list.append(sub_dict)
            for child in self.children():
                child.to_json(sub_dict[self.name])

