class NodeModel:
    def __init__(self, parent=None, **kwargs):
        self._children = []
        self._parent = parent
        if parent is not None:
            parent.add_child(self)
        self._data = kwargs

    def add_child(self, child):
        self._children.append(child)

    @property
    def children(self):
        return self._children

    @property
    def parent(self):
        return self._parent

    @property
    def data(self):
        return self._data

    def set_data(self, key, value):
        self._data[key] = value

    def child(self, row):
        try:
            return self._children[row]
        except IndexError:
            return None

    def rows(self):
        return len(self._children)

    def cols(self):
        return len(self._data.keys())

    def row(self):
        if self.parent:
            return self.parent.children.index(self)
        return 0

    def to_dict(self, init_dict):
        if not self.children:
            init_dict[self.data['text']] = self.data
        else:
            init_dict[self.data['text']] = {}
            for child in self.children:
                child.to_dict(init_dict[self.data['text']])

    def to_json(self, init_list):
        if not self.children:
            init_list.append(self.data)
        else:
            try:
                key = self.data['text']
            except KeyError:
                key = 'root'
            sub_dict = {key: []}
            init_list.append(sub_dict)
            for child in self.children:
                child.to_json(sub_dict[key])


def make_node(root, data):
    for datum in data:
        if 'name' in datum.keys():
            NodeModel(root, **datum)
        else:
            child_text = datum.keys()[0]
            child = NodeModel(root, text=child_text)
            make_node(child, datum[child_text])




