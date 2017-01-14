# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MapInputUI.ui'
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
        MainWindow.resize(990, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.MapInputWidget = QtGui.QWidget(self.centralwidget)
        self.MapInputWidget.setEnabled(True)
        self.MapInputWidget.setMinimumSize(QtCore.QSize(500, 500))
        self.MapInputWidget.setMouseTracking(True)
        self.MapInputWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.MapInputWidget.setAcceptDrops(True)
        self.MapInputWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.MapInputWidget.setObjectName(_fromUtf8("MapInputWidget"))
        self.gridLayout_2.addWidget(self.MapInputWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
        self.dockWidget.setMinimumSize(QtCore.QSize(368, 139))
        self.dockWidget.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.pixelsize_lineedit = QtGui.QLineEdit(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pixelsize_lineedit.sizePolicy().hasHeightForWidth())
        self.pixelsize_lineedit.setSizePolicy(sizePolicy)
        self.pixelsize_lineedit.setMinimumSize(QtCore.QSize(30, 20))
        self.pixelsize_lineedit.setMaximumSize(QtCore.QSize(30, 20))
        self.pixelsize_lineedit.setObjectName(_fromUtf8("pixelsize_lineedit"))
        self.horizontalLayout.addWidget(self.pixelsize_lineedit)
        spacerItem = QtGui.QSpacerItem(100, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.MapInputTreeView = QtGui.QTreeView(self.dockWidgetContents)
        self.MapInputTreeView.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MapInputTreeView.sizePolicy().hasHeightForWidth())
        self.MapInputTreeView.setSizePolicy(sizePolicy)
        self.MapInputTreeView.setMinimumSize(QtCore.QSize(350, 0))
        self.MapInputTreeView.setMouseTracking(True)
        self.MapInputTreeView.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.MapInputTreeView.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.MapInputTreeView.setAcceptDrops(True)
        self.MapInputTreeView.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.MapInputTreeView.setEditTriggers(QtGui.QAbstractItemView.DoubleClicked|QtGui.QAbstractItemView.EditKeyPressed)
        self.MapInputTreeView.setProperty("showDropIndicator", False)
        self.MapInputTreeView.setDragEnabled(False)
        self.MapInputTreeView.setDragDropOverwriteMode(False)
        self.MapInputTreeView.setDragDropMode(QtGui.QAbstractItemView.NoDragDrop)
        self.MapInputTreeView.setTextElideMode(QtCore.Qt.ElideRight)
        self.MapInputTreeView.setObjectName(_fromUtf8("MapInputTreeView"))
        self.gridLayout.addWidget(self.MapInputTreeView, 1, 0, 1, 1)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.action_Open = QtGui.QAction(MainWindow)
        self.action_Open.setObjectName(_fromUtf8("action_Open"))
        self.action_Save = QtGui.QAction(MainWindow)
        self.action_Save.setObjectName(_fromUtf8("action_Save"))
        self.action_Compare = QtGui.QAction(MainWindow)
        self.action_Compare.setObjectName(_fromUtf8("action_Compare"))
        self.toolBar.addAction(self.action_Open)
        self.toolBar.addAction(self.action_Save)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Input Maps", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.dockWidget.setWindowTitle(_translate("MainWindow", "Map Input", None))
        self.label.setText(_translate("MainWindow", "Pixel size (ha)", None))
        self.pixelsize_lineedit.setText(_translate("MainWindow", "30", None))
        self.action_Open.setText(_translate("MainWindow", "&Open", None))
        self.action_Open.setToolTip(_translate("MainWindow", "Choose a map file", None))
        self.action_Open.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.action_Save.setText(_translate("MainWindow", "&Save", None))
        self.action_Save.setToolTip(_translate("MainWindow", "Save project", None))
        self.action_Save.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.action_Compare.setText(_translate("MainWindow", "&Compare", None))
        self.action_Compare.setToolTip(_translate("MainWindow", "Choose files to compare with", None))
        self.action_Compare.setShortcut(_translate("MainWindow", "Ctrl+C", None))

