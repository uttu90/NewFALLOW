# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inputMaps_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1748, 1235)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setMaximumSize(QtCore.QSize(500, 16777215))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pixelSize_label = QtWidgets.QLabel(self.widget)
        self.pixelSize_label.setObjectName("pixelSize_label")
        self.horizontalLayout_5.addWidget(self.pixelSize_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_5.addWidget(self.lineEdit)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.maps_treeView = QtWidgets.QTreeView(self.widget)
        self.maps_treeView.setObjectName("maps_treeView")
        self.verticalLayout_6.addWidget(self.maps_treeView)
        self.gridLayout.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.widget)
        self.map_frame = QtWidgets.QFrame(Dialog)
        self.map_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.map_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.map_frame.setObjectName("map_frame")
        self.horizontalLayout_3.addWidget(self.map_frame)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_5.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Input Maps"))
        self.pixelSize_label.setText(_translate("Dialog", "Pixel size (ha): "))

