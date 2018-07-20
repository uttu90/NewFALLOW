from PyQt5.QtCore import QAbstractItemModel, QFile, QIODevice, QModelIndex, Qt
from PyQt5.QtWidgets import QApplication, QTreeView
import model
from FALLOW import map_models


class TreeModel(QAbstractItemModel):
    def __init__(self, parent=None, headers=[]):
        super(TreeModel, self).__init__(parent)
        root_item = model.NodeModel()
        model.make_node(root_item, map_models.map_model)
        self.root_item = root_item
        self.headers = headers

    def rowCount(self, parent=None, *args, **kwargs):
        if parent.column() > 0:
            return 0

        if not parent.isValid():
            parent_item = self.root_item
        else:
            parent_item = parent.internalPointer()

        return parent_item.rows()

    def flags(self, index):
        if not index.isValid():
            return Qt.NoItemFlags
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def setData(self, index, value, role=None):
        if role == Qt.EditRole:
            node = index.internalPointer()
            node.set_data(self.headers[index.column()], str(value))
            return True
        return False

    def columnCount(self, parent=None, *args, **kwargs):
        return len(self.headers)

    def parent(self, index=None):
        if not index.isValid():
            return QModelIndex()
        child_item = index.internalPointer()
        parent_item = child_item.parent
        if parent_item == self.root_item:
            return QModelIndex()
        return self.createIndex(parent_item.row(), 0, parent_item)

    def index(self, row, col, parent=None, *args, **kwargs):
        if not self.hasIndex(row, col, parent):
            return QModelIndex()
        if not parent.isValid():
            parent_item = self.root_item
        else:
            parent_item = parent.internalPointer()

        child_item = parent_item.child(row)
        if child_item:
            return self.createIndex(row, col, child_item)
        else:
            return QModelIndex()

    def headerData(self, section, orientation, role=None):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.headers[section]
        return None

    def data(self, index, role=None):
        if not index.isValid():
            return None
        if role != Qt.DisplayRole:
            return None
        item = index.internalPointer()
        try:
            return item.data[self.headers[index.column()]]
        except KeyError:
            return None


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    # f = QFile(':/default.txt')
    # f.open(QIODevice.ReadOnly)
    model = TreeModel(parent=None, headers=['text', 'path', 'description'])
    # print model.rootItem.data(0)
    # f.close()

    view = QTreeView()
    view.setModel(model)
    view.setWindowTitle("Simple Tree Model")
    view.show()
    sys.exit(app.exec_())