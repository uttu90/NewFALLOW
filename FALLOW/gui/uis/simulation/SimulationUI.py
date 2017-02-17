# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'output.ui'
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
        MainWindow.resize(811, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.mapDisplay = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mapDisplay.sizePolicy().hasHeightForWidth())
        self.mapDisplay.setSizePolicy(sizePolicy)
        self.mapDisplay.setMinimumSize(QtCore.QSize(200, 200))
        self.mapDisplay.setObjectName(_fromUtf8("mapDisplay"))
        self.horizontalLayout_3.addWidget(self.mapDisplay)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setEnabled(True)
        self.dockWidget.setMouseTracking(True)
        self.dockWidget.setAcceptDrops(False)
        self.dockWidget.setFloating(False)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.mapOutput = QtGui.QTreeView(self.dockWidgetContents)
        self.mapOutput.setObjectName(_fromUtf8("mapOutput"))
        self.verticalLayout.addWidget(self.mapOutput)
        self.timeseriesOutput = QtGui.QTreeView(self.dockWidgetContents)
        self.timeseriesOutput.setObjectName(_fromUtf8("timeseriesOutput"))
        self.verticalLayout.addWidget(self.timeseriesOutput)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.horizontalSlider = QtGui.QSlider(self.dockWidgetContents)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.horizontalLayout.addWidget(self.horizontalSlider)
        self.yearNumber = QtGui.QLCDNumber(self.dockWidgetContents)
        self.yearNumber.setObjectName(_fromUtf8("yearNumber"))
        self.horizontalLayout.addWidget(self.yearNumber)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.playButton = QtGui.QPushButton(self.dockWidgetContents)
        self.playButton.setObjectName(_fromUtf8("playButton"))
        self.horizontalLayout_2.addWidget(self.playButton)
        self.pauseButton = QtGui.QPushButton(self.dockWidgetContents)
        self.pauseButton.setObjectName(_fromUtf8("pauseButton"))
        self.horizontalLayout_2.addWidget(self.pauseButton)
        self.stopButton = QtGui.QPushButton(self.dockWidgetContents)
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.horizontalLayout_2.addWidget(self.stopButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.actionTimeSeries = QtGui.QAction(MainWindow)
        self.actionTimeSeries.setObjectName(_fromUtf8("actionTimeSeries"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Simulation", None))
        self.playButton.setText(_translate("MainWindow", "Play", None))
        self.pauseButton.setText(_translate("MainWindow", "Pause", None))
        self.stopButton.setText(_translate("MainWindow", "Stop", None))
        self.actionTimeSeries.setText(_translate("MainWindow", "TimeSeries", None))
