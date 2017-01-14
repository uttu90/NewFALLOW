# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TSInputUI1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.TSInputDiagram = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TSInputDiagram.sizePolicy().hasHeightForWidth())
        self.TSInputDiagram.setSizePolicy(sizePolicy)
        self.TSInputDiagram.setMinimumSize(QtCore.QSize(400, 400))
        self.TSInputDiagram.setObjectName(_fromUtf8("TSInputDiagram"))
        self.gridLayout_3.addWidget(self.TSInputDiagram, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.dockWidgetContents)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.simulationtime_lineedit = QtGui.QLineEdit(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.simulationtime_lineedit.sizePolicy().hasHeightForWidth())
        self.simulationtime_lineedit.setSizePolicy(sizePolicy)
        self.simulationtime_lineedit.setMaximumSize(QtCore.QSize(30, 16777215))
        self.simulationtime_lineedit.setObjectName(_fromUtf8("simulationtime_lineedit"))
        self.gridLayout.addWidget(self.simulationtime_lineedit, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(102, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.TSInputTreeview = QtGui.QTreeView(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TSInputTreeview.sizePolicy().hasHeightForWidth())
        self.TSInputTreeview.setSizePolicy(sizePolicy)
        self.TSInputTreeview.setAcceptDrops(False)
        self.TSInputTreeview.setAutoScroll(False)
        self.TSInputTreeview.setItemsExpandable(True)
        self.TSInputTreeview.setWordWrap(False)
        self.TSInputTreeview.setObjectName(_fromUtf8("TSInputTreeview"))
        self.gridLayout.addWidget(self.TSInputTreeview, 2, 0, 1, 3)
        self.usingts_chk = QtGui.QCheckBox(self.dockWidgetContents)
        self.usingts_chk.setObjectName(_fromUtf8("usingts_chk"))
        self.gridLayout.addWidget(self.usingts_chk, 0, 0, 1, 1)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.dockWidget_2 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_2.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
        self.dockWidget_2.setObjectName(_fromUtf8("dockWidget_2"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.TSInputTableview = QtGui.QTableView(self.dockWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TSInputTableview.sizePolicy().hasHeightForWidth())
        self.TSInputTableview.setSizePolicy(sizePolicy)
        self.TSInputTableview.setObjectName(_fromUtf8("TSInputTableview"))
        self.gridLayout_2.addWidget(self.TSInputTableview, 0, 0, 1, 1)
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_2)
        self.action_Save = QtGui.QAction(MainWindow)
        self.action_Save.setObjectName(_fromUtf8("action_Save"))
        self.toolBar.addAction(self.action_Save)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.dockWidget.setWindowTitle(_translate("MainWindow", "Timeseries", None))
        self.label.setText(_translate("MainWindow", "Simulation time (years)", None))
        self.usingts_chk.setText(_translate("MainWindow", "Using Timeseries", None))
        self.dockWidget_2.setWindowTitle(_translate("MainWindow", "Values", None))
        self.action_Save.setText(_translate("MainWindow", "&Save", None))
        self.action_Save.setToolTip(_translate("MainWindow", "Save", None))
        self.action_Save.setShortcut(_translate("MainWindow", "Ctrl+S", None))

