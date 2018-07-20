from PyQt5 import QtCore


class TreeModel(QtCore.QAbstractItemModel):
    def __init__(self, root, headers):
        super(TreeModel, self).__init__()
        self.root = root
        self.headers = headers

    def rowCount(self, parent=None):
        if not parent.isValid():
            parent_node = self.rootNode
        else:
            parent_node = parent.internalPointer()
        return parent_node.rows()

    def columnCount(self, parent=None):
        return len(self.headers)

    def parent(self, index):
        selected_node = index.internalPointer()
        parent_node = selected_node.parent()
        if parent_node == self.rootNode:
            return QtCore.QModelIndex()
        return self.createIndex(parent_node.row(), 0, parent_node)

    def index(self, row, column, parent):
        if not parent.isValid():
            parent_node = self.rootNode
        else:
            parent_node = parent.internalPointer()
        child = parent_node.child(row)
        if child:
            return self.createIndex(row, column, child)
        else:
            return QtCore.QModelIndex()

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
    from PyQt5.QtGui import QIcon

    from PyQt5.QtCore import (QDate, QDateTime, QRegExp, QSortFilterProxyModel,
                              Qt,
                              QTime)
    from PyQt5.QtGui import QStandardItemModel
    from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox,
                                 QGridLayout,
                                 QGroupBox, QHBoxLayout, QLabel, QLineEdit,
                                 QTreeView, QVBoxLayout,
                                 QWidget)
    from FALLOW import models

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

    class App(QWidget):

        FROM, SUBJECT, DATE = range(3)

        def __init__(self):
            super(App, self).__init__()
            self.title = 'PyQt5 Treeview Example - pythonspot.com'
            self.left = 10
            self.top = 10
            self.width = 640
            self.height = 240
            self.initUI()

        def initUI(self):
            self.setWindowTitle(self.title)
            self.setGeometry(self.left, self.top, self.width, self.height)

            self.dataGroupBox = QGroupBox("Inbox")
            self.dataView = QTreeView()
            self.dataView.setRootIsDecorated(False)
            self.dataView.setAlternatingRowColors(True)

            dataLayout = QHBoxLayout()
            dataLayout.addWidget(self.dataView)
            self.dataGroupBox.setLayout(dataLayout)

            model = self.createMailModel()
            self.dataView.setModel(model)
            # self.addMail(model, 'service@github.com', 'Your Github Donation',
            #              '03/25/2017 02:05 PM')
            # self.addMail(model, 'support@github.com', 'Github Projects',
            #              '02/02/2017 03:05 PM')
            # self.addMail(model, 'service@phone.com', 'Your Phone Bill',
            #              '01/01/2017 04:05 PM')

            mainLayout = QVBoxLayout()
            mainLayout.addWidget(self.dataGroupBox)
            self.setLayout(mainLayout)

            self.show()

        def createMailModel(self):
            # model = QStandardItemModel(0, 3, parent)
            # model.setHeaderData(self.FROM, Qt.Horizontal, "From")
            # model.setHeaderData(self.SUBJECT, Qt.Horizontal, "Subject")
            # model.setHeaderData(self.DATE, Qt.Horizontal, "Date")
            # return model

            root = models.NodeModel()
            models.make_node(root, my_dict)
            return TreeModel(root, ['a', 'b', 'c'])

        # def addMail(self, model, mailFrom, subject, date):
        #     model.insertRow(0)
        #     model.setData(model.index(0, self.FROM), mailFrom)
        #     model.setData(model.index(0, self.SUBJECT), subject)
        #     model.setData(model.index(0, self.DATE), date)


    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())