# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1633, 1053)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/MainWindowIcons/icon/transparent/ICRAF.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(500, 600))
        self.frame.setStyleSheet("border-image: url(:/background/IMG_7136(s).jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout.addWidget(self.frame)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1633, 38))
        self.menuBar.setObjectName("menuBar")
        self.menuInput = QtWidgets.QMenu(self.menuBar)
        self.menuInput.setObjectName("menuInput")
        self.menuSimulation = QtWidgets.QMenu(self.menuBar)
        self.menuSimulation.setObjectName("menuSimulation")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuLanguages = QtWidgets.QMenu(self.menuBar)
        self.menuLanguages.setObjectName("menuLanguages")
        self.menuProject = QtWidgets.QMenu(self.menuBar)
        self.menuProject.setObjectName("menuProject")
        self.menuImport = QtWidgets.QMenu(self.menuBar)
        self.menuImport.setObjectName("menuImport")
        MainWindow.setMenuBar(self.menuBar)
        self.inputMap = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/MainWindowIcons/icon/map.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/MainWindowIcons/icon/global.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.inputMap.setIcon(icon1)
        self.inputMap.setObjectName("inputMap")
        self.action_Biophysics = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/MainWindowIcons/icon/transparent/environment.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(":/MainWindowIcons/icon/environment.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.action_Biophysics.setIcon(icon2)
        self.action_Biophysics.setObjectName("action_Biophysics")
        self.action_Economy = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/MainWindowIcons/icon/economy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(":/MainWindowIcons/icon/dollar.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.action_Economy.setIcon(icon3)
        self.action_Economy.setObjectName("action_Economy")
        self.action_Social = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/MainWindowIcons/icon/community.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap("../Resources/icon/transparent/comunitiy.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.action_Social.setIcon(icon4)
        self.action_Social.setObjectName("action_Social")
        self.action_Input_Timeseries = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/MainWindowIcons/icon/timeseries.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Input_Timeseries.setIcon(icon5)
        self.action_Input_Timeseries.setObjectName("action_Input_Timeseries")
        self.play = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/MainWindowIcons/icon/transparent/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play.setIcon(icon6)
        self.play.setObjectName("play")
        self.action_Other = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/MainWindowIcons/icon/transparent/more.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.action_Other.setIcon(icon7)
        self.action_Other.setObjectName("action_Other")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionEnglish = QtWidgets.QAction(MainWindow)
        self.actionEnglish.setObjectName("actionEnglish")
        self.actionVietnamese = QtWidgets.QAction(MainWindow)
        self.actionVietnamese.setObjectName("actionVietnamese")
        self.openProject = QtWidgets.QAction(MainWindow)
        self.openProject.setObjectName("openProject")
        self.createProject = QtWidgets.QAction(MainWindow)
        self.createProject.setObjectName("createProject")
        self.actionClone_project = QtWidgets.QAction(MainWindow)
        self.actionClone_project.setObjectName("actionClone_project")
        self.actionLand_cover = QtWidgets.QAction(MainWindow)
        self.actionLand_cover.setObjectName("actionLand_cover")
        self.importData = QtWidgets.QAction(MainWindow)
        self.importData.setObjectName("importData")
        self.reload = QtWidgets.QAction(MainWindow)
        self.reload.setObjectName("reload")
        self.menuInput.addAction(self.inputMap)
        self.menuSimulation.addAction(self.play)
        self.menuHelp.addAction(self.actionHelp)
        self.menuLanguages.addAction(self.actionEnglish)
        self.menuLanguages.addAction(self.actionVietnamese)
        self.menuProject.addAction(self.openProject)
        self.menuProject.addAction(self.createProject)
        self.menuImport.addAction(self.importData)
        self.menuImport.addAction(self.reload)
        self.menuBar.addAction(self.menuProject.menuAction())
        self.menuBar.addAction(self.menuInput.menuAction())
        self.menuBar.addAction(self.menuImport.menuAction())
        self.menuBar.addAction(self.menuSimulation.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuBar.addAction(self.menuLanguages.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FALLOW"))
        self.menuInput.setTitle(_translate("MainWindow", "Input"))
        self.menuSimulation.setTitle(_translate("MainWindow", "Simulation"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuLanguages.setTitle(_translate("MainWindow", "Languages"))
        self.menuProject.setTitle(_translate("MainWindow", "Project"))
        self.menuImport.setTitle(_translate("MainWindow", "Import"))
        self.inputMap.setText(_translate("MainWindow", "&Maps"))
        self.inputMap.setToolTip(_translate("MainWindow", "Input Maps"))
        self.inputMap.setShortcut(_translate("MainWindow", "Ctrl+M"))
        self.action_Biophysics.setText(_translate("MainWindow", "&Biophysics"))
        self.action_Biophysics.setToolTip(_translate("MainWindow", "Input Biophysics Parameters"))
        self.action_Biophysics.setShortcut(_translate("MainWindow", "Ctrl+B"))
        self.action_Economy.setText(_translate("MainWindow", "&Economy"))
        self.action_Economy.setToolTip(_translate("MainWindow", "Input Economy Parameters"))
        self.action_Economy.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.action_Social.setText(_translate("MainWindow", "&Social"))
        self.action_Social.setToolTip(_translate("MainWindow", "Input Social Parameters"))
        self.action_Social.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_Input_Timeseries.setText(_translate("MainWindow", "&Timeseries"))
        self.action_Input_Timeseries.setToolTip(_translate("MainWindow", "Input Timeseries"))
        self.action_Input_Timeseries.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.play.setText(_translate("MainWindow", "P&lay"))
        self.play.setToolTip(_translate("MainWindow", "Play"))
        self.play.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.action_Other.setText(_translate("MainWindow", "&Other"))
        self.action_Other.setToolTip(_translate("MainWindow", "Input Other Parameters"))
        self.action_Other.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionHelp.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actionEnglish.setText(_translate("MainWindow", "English"))
        self.actionVietnamese.setText(_translate("MainWindow", "Vietnamese"))
        self.openProject.setText(_translate("MainWindow", "Open project"))
        self.openProject.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.createProject.setText(_translate("MainWindow", "Create new project"))
        self.createProject.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionClone_project.setText(_translate("MainWindow", "Clone project"))
        self.actionLand_cover.setText(_translate("MainWindow", "Land cover"))
        self.importData.setText(_translate("MainWindow", "Choose data file"))
        self.importData.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.reload.setText(_translate("MainWindow", "Reload"))
        self.reload.setShortcut(_translate("MainWindow", "Ctrl+R"))

