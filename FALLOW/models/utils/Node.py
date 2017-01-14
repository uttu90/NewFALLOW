import copy


class Node(object):
    def __init__(self, name="Noname", parent=None, text='nothing', unit='', value=None, description=''):
        self._name = name
        self._parent = parent
        self._text = text
        self._value = value
        self._unit = unit
        self._description = description
        self._children = []
        self._typeinfo = "Node"
        self._headerdata = ["Name", "Unit", "Value", "Description"]
        if parent is not None:
            parent.addChild(self)

    def row(self):
        if self._parent is not None:
            return self._parent._children.index(self)

    def child(self, row):
        return self._children[row]

    def children(self):
        return self._children

    def parent(self):
        return self._parent

    def typeInfo(self):
        return self._typeinfo

    def addChild(self, child):
        self._children.append(child)

    def childCount(self):
        return len(self._children)

    def name(self):
        return self._name

    def text(self):
        return self._text

    def unit(self):
        return self._unit

    def value(self):
        return self._value

    def description(self):
        return self._description

    def headerdata(self):
        return self._headerdata

    def setDescription(self, des):
        self._description = des

    def setUnit(self, unit):
        self._unit = unit

    def setValue(self, value):
        if self.childCount() == 0:
            self._value = value
        else:
            self._value = None

    def searchNode(self, nameNode):
        if self._name == nameNode:
            return self
        for node in self._children:
            n = node.searchNode(nameNode)
            if n:
                return n
        return None

    def toArray(self, array):
        if self.childCount() == 0:
            array += [self.value()]
        else:
            subarray = []
            for child in self.children():
                subarray += child.toArray([])
            array += [subarray]
        # print(array)
        return array


class TimeNode(Node):
    def __init__(self, name='Noname', parent=None, text='nothing', unit='', value=None, description=''):
        Node.__init__(self, name, parent, text, unit, value, description)
        self._headerdata = ['Name', 'Unit', 'Description', 'Value']
        self._typeinfo = ['TimeNode']

    def addBranch(self, array, value=None):
        # cvalue = copy.deepcopy(value)
        if self.childCount() == 0:
            for child in array:
                Node(name=child[0], parent=self, text=child[1], value=copy.deepcopy(value))
        else:
            for nodechild in self._children:
                nodechild.addBranch(array, value=copy.deepcopy(value))

    def toArray(self, array):
        if self.childCount() == 0:
            array += [self.value()]
        else:
            subarray = []
            for child in self.children():
                subarray += child.toArray([])
            array += [subarray]
        # print(array)
        return array


class MapNode(Node):
    def __init__(self, name='Noname', parent=None, text='nothing', unit='', value=None, description=''):
        Node.__init__(self,name, parent, text, unit, value, description)
        self._headerdata = ['Name', 'Unit', 'Value', 'Description']
        self._typeinfo = ['MapNode']

    def addBranch(self, array, value=None):
        # cvalue = copy.deepcopy(value)
        if self.childCount() == 0:
            for child in array:
                MapNode(name=child[0], parent=self, text=child[1], value=copy.deepcopy(value))
        else:
            for nodechild in self._children:
                nodechild.addBranch(array, value=copy.deepcopy(value))

    def toArray(self, array):
        if self.childCount() == 0:
            array += [self.value()]
        else:
            subarray = []
            for child in self.children():
                subarray += child.toArray([])
            array += [subarray]
        # print(array)
        return array


class ValueNode(Node):
    def __init__(self, name='Noname', parent=None, text='nothing', unit='', value=None, description=''):
        Node.__init__(self, name, parent, text, unit, value, description)
        self._headerdata = ['Name', 'Unit', 'Value', 'Description']
        self._typeinfo = ['ValueNode']

    def addBranch(self, array, value=None):
        # cvalue = copy.deepcopy(value)
        if self.childCount() == 0:
            for child in array:
                ValueNode(name=child[0], parent=self, text=child[1], value=copy.deepcopy(value))
        else:
            for nodechild in self._children:
                nodechild.addBranch(array, value=copy.deepcopy(value))

    def toArray(self, array):
        if self.childCount() == 0:
            array += [self.value()]
        else:
            subarray = []
            for child in self.children():
                subarray += child.toArray([])
            array += [subarray]
        # print(array)
        return array
