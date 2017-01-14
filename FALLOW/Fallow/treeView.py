# -*- coding: utf-8 -*-
#!/usr/bin/env python


import sys
import os

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from model import TreModel
from test_json import root

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
        self.dbs_tree_model = TreModel(root)
        self.dbs_tree_view.setModel(self.dbs_tree_model)

if __name__=='__main__':
    app = QApplication(sys.argv)
    form = TreeModelTester()
    form.show()
    app.exec_()
