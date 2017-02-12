from PyQt4 import QtCore
from PyQt4 import QtGui

class TreModel(QtCore.QAbstractItemModel):
    def __init__(self, root, parent=None):
        super(TreModel, self).__init__()
        self.rootNode = root
        self.header = ['Name', 'Path', 'Description']

    def rowCount(self, parent):
        if not parent.isValid():
            parentNode = self.rootNode
        else:
            parentNode = parent.internalPointer()
        return parentNode.rows()

    def columnCount(self, parent):
        # if not parent.isValid():
        #     parentNode = self.rootNode
        # else:
        #     parentNode = parent.internalPointer()
        # return parentNode.cols()
        return 3

    def parent(self, index):
        node = index.internalPointer()
        parentNode = node.parent()
        if parentNode == self.rootNode:
            return QtCore.QModelIndex()
        return self.createIndex(parentNode.row(), 0, parentNode)

    def index(self, row, column, parent):
        if not parent.isValid():
            parentNode = self.rootNode
        else:
            parentNode = parent.internalPointer()
        child = parentNode.child(row)
        if child:
            return self.createIndex(row, column, child)
        else:
            return QtCore.QModelIndex()

    def flags(self, index):
        """Returns the item flags for the given index. """
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable

    def data(self, index, role):
        """Returns the data stored under the given role for the item
        referred to by the index."""
        column = index.column()
        if not index.isValid():
            return QtCore.QVariant()
        node = self.nodeFromIndex(index)
        if role == QtCore.Qt.DisplayRole:
            try:
                return QtCore.QVariant(node.values()[column])
            except IndexError:
                return QtCore.QVariant()
        else:
            return QtCore.QVariant()

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        value = value.toString()
        if index.isValid():
            if role == QtCore.Qt.EditRole:
                node = index.internalPointer()
                column = index.column()
                data = {}
                data[self.header[column]] = value
                print data
                node.set_data(**data)
                return True
        return False

    def headerData(self, section, orientation, role):
        """Returns the data for the given role and section in the header
        with the specified orientation.
        """

        if (orientation, role) == (QtCore.Qt.Horizontal, \
                                   QtCore.Qt.DisplayRole):
            return QtCore.QVariant('Sample tree')

        return QtCore.QVariant()

    def nodeFromIndex(self, index):
        """Retrieves the tree node with a given index."""

        if index.isValid():
            return index.internalPointer()
        else:
            return self.root
