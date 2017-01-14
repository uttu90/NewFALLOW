from PyQt4 import QtCore
from PyQt4 import QtGui
import Node


class Tree(QtCore.QAbstractItemModel):
    def __init__(self, root, parent=None):
        QtCore.QAbstractItemModel.__init__(self)
        self.rootNode = root
        if self.rootNode.typeInfo() == ["TimeNode"]:
            self._flags = [QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable,
                           QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable,
                           QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable,
                           QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable]
        elif self.rootNode.typeInfo() == "MapNode":
            self._flags = [QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable,
                           QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable,
                           QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable,
                           QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable]
        elif self.rootNode.typeInfo() == "ValueNode":
            self._flags = [QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable,
                           QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable,
                           QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable,
                           QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable]
        else:
            self._flags = [QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable,
                           QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable,
                           QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable,
                           QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable]

    def rowCount(self, parent):
        if not parent.isValid():
            parentNode = self.rootNode
        else:
            parentNode = parent.internalPointer()
        return parentNode.childCount()

    def columnCount(self, parent):
        return len(self.rootNode.headerdata())

    def data(self, index, role):
        if not index.isValid():
            return None
        node = index.internalPointer()
        column = index.column()
        if role == QtCore.Qt.DisplayRole:
            if node.headerdata()[column] == "Name":
                return QtCore.QVariant(node.text())
            elif node.headerdata()[column] == "Value":
                return QtCore.QVariant(node.value())
            elif node.headerdata()[column] == "Unit":
                return QtCore.QVariant(node.unit())
            else:
                return QtCore.QVariant(node.description())
        elif role == QtCore.Qt.BackgroundRole:
            if node.headerdata()[column] == "Value":
                return QtGui.QBrush(QtGui.QColor(240, 240, 240))
            elif node.headerdata()[column] == "Unit":
                return QtGui.QBrush(QtGui.QColor(240, 240, 255))
            elif node.headerdata()[column] == "Description":
                return QtGui.QBrush(QtGui.QColor(240, 255, 255))
        elif role == QtCore.Qt.EditRole:
            if node.headerdata()[column] == "Name":
                return QtCore.QVariant(node.text())
            elif node.headerdata()[column] == "Unit":
                return QtCore.QVariant(node.unit())
            elif node.headerdata()[column] == "Value":
                return QtCore.QVariant(node.value())
            else:
                return QtCore.QVariant(node.description())

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        value = value.toString()
        if index.isValid():
            if role == QtCore.Qt.EditRole:
                node = index.internalPointer()
                column = index.column()
                if node.headerdata()[column] == "Description":
                    node.setDescription(str(value))
                elif node.headerdata()[column] == "Unit":
                    node.setUnit(str(value))
                elif node.headerdata()[column] == "Value":
                    node.setValue(str(value))
                return True
        return False

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            return self.rootNode.headerdata()[section]

    def flags(self, index):
        node = index.internalPointer()
        if node.childCount() == 0:
            return self._flags[index.column()]
        else:
            return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled

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
        childItem = parentNode.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QtCore.QModelIndex()

