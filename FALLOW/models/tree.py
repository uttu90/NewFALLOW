from PyQt4 import QtCore
import json
import node


class TreModel(QtCore.QAbstractItemModel):
    def __init__(self, file_name, header, flags):
        super(TreModel, self).__init__()
        self.rootNode = self.load_from_file(file_name)
        self.header = header
        self.flags = flags

    def load_from_dict(self, keys_maps, keys_list):
        pass

    @staticmethod
    def load_from_file(file_name):
        try:
            with open(file_name, 'r') as data_file:
                data_dict = json.load(data_file)
                root = node.Node('root')

                def make_node(parent, list_dict):
                    for a_dict in list_dict:
                        key = a_dict.keys()[0]
                        if isinstance(a_dict[key], dict):
                            node.Node(key, parent, **a_dict[key])
                        else:
                            sub_node = node.Node(key, parent)
                            make_node(sub_node, a_dict[key])

                make_node(root, data_dict)
            return root
        except IOError:
            pass

    def rowCount(self, parent):
        if not parent.isValid():
            parentNode = self.rootNode
        else:
            parentNode = parent.internalPointer()
        return parentNode.rows()

    def columnCount(self, parent):
        return len(self.header)

    def parent(self, index):
        selected_node = index.internalPointer()
        parentNode = selected_node.parent()
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
        selected_node = index.internalPointer()
        if len(selected_node.children()) == 0:
            return self.flags[index.column()]
        else:
            return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable

    def data(self, index, role):
        """Returns the data stored under the given role for the item
        referred to by the index."""
        column = index.column()
        if not index.isValid():
            return QtCore.QVariant()
        selected_node = self.nodeFromIndex(index)
        if role == QtCore.Qt.DisplayRole:
            try:
                return QtCore.QVariant(selected_node.values()[column])
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
                data[self.header[column]] = str(value)
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
            return QtCore.QVariant(self.header[section])

        return QtCore.QVariant()

    def nodeFromIndex(self, index):
        """Retrieves the tree node with a given index."""

        if index.isValid():
            return index.internalPointer()
        else:
            return self.root


if __name__ == '__main__':
    import sys
    import os

    from PyQt4.QtCore import *
    from PyQt4.QtGui import *


    FLAGS = [QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable,
            QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable,
            QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable,]


    class TreeModelTester(QMainWindow):
        """Test correctness of tree models/views """

        def __init__(self):
            """Initialize the application."""

            QMainWindow.__init__(self)

            # Make the GUI
            self.setWindowTitle('TreeView tester')
            central_widget = QWidget(self)
            central_layout = QVBoxLayout(central_widget)
            self.setCentralWidget(central_widget)
            self.dbs_tree_view = QTreeView(central_widget)
            central_layout.addWidget(self.dbs_tree_view)

            # The tree of databases model/view
            # print root
            self.dbs_tree_model = TreModel('maps.json', header=['Name', 'Path', 'Description'], flags=FLAGS)
            self.dbs_tree_view.setModel(self.dbs_tree_model)


    app = QApplication(sys.argv)
    form = TreeModelTester()
    form.show()
    app.exec_()