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

    def child(self, row):
        try:
            return self._children[row]
        except IndexError:
            return None

    def rows(self):
        return len(self._children)

    def cols(self):
        return len(self._data.keys())


def make_node(root, data):
    for datum in data:
        if 'name' in datum.keys():
            NodeModel(root, **datum)
        else:
            child_text = datum.keys()[0]
            child = NodeModel(root, text=child_text)
            make_node(child, datum[child_text])


if __name__ == '__main__':
    from FALLOW import map_models
    my_dict = [
        {'node 1': [
            {
                'name': 'node 11',
                'text': 'Node 11'
            },
            {
                'name': 'node 12',
                'text': 'Node 12'
            },
            {
                'node 13': [
                    {
                        'name': 'node 131',
                        'text': 'Node 132'
                    }
                ]
            }
        ]},
        {
            'name': 'node 2',
            'text': 'Node 22'
        },
    ]
    root = NodeModel()
    make_node(root, map_models.map_model)
    print root.child(0).data
    # print root.child(0).child(2).child(0).data
