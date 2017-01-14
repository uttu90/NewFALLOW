# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\cloneproject.ui'
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

class Ui_diagcloneprj(object):
    def setupUi(self, diagcloneprj):
        diagcloneprj.setObjectName(_fromUtf8("diagcloneprj"))
        diagcloneprj.resize(505, 362)
        self.buttonBox = QtGui.QDialogButtonBox(diagcloneprj)
        self.buttonBox.setGeometry(QtCore.QRect(140, 310, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.groupBox = QtGui.QGroupBox(diagcloneprj)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 461, 80))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 0, 461, 80))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.lineoriginalprj = QtGui.QLineEdit(self.groupBox_2)
        self.lineoriginalprj.setGeometry(QtCore.QRect(20, 30, 301, 20))
        self.lineoriginalprj.setObjectName(_fromUtf8("lineoriginalprj"))
        self.btnoriginalprj = QtGui.QPushButton(self.groupBox_2)
        self.btnoriginalprj.setGeometry(QtCore.QRect(370, 30, 75, 23))
        self.btnoriginalprj.setObjectName(_fromUtf8("btnoriginalprj"))
        self.groupBox_3 = QtGui.QGroupBox(diagcloneprj)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 120, 461, 71))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.linedestinationprj = QtGui.QLineEdit(self.groupBox_3)
        self.linedestinationprj.setGeometry(QtCore.QRect(20, 30, 301, 20))
        self.linedestinationprj.setObjectName(_fromUtf8("linedestinationprj"))
        self.btndestinationprj = QtGui.QPushButton(self.groupBox_3)
        self.btndestinationprj.setGeometry(QtCore.QRect(370, 30, 75, 23))
        self.btndestinationprj.setObjectName(_fromUtf8("btndestinationprj"))
        self.groupBox_4 = QtGui.QGroupBox(diagcloneprj)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 210, 461, 71))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.label = QtGui.QLabel(self.groupBox_4)
        self.label.setGeometry(QtCore.QRect(20, 30, 31, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.linemodelername = QtGui.QLineEdit(self.groupBox_4)
        self.linemodelername.setGeometry(QtCore.QRect(60, 30, 161, 20))
        self.linemodelername.setObjectName(_fromUtf8("linemodelername"))
        self.label_2 = QtGui.QLabel(self.groupBox_4)
        self.label_2.setGeometry(QtCore.QRect(230, 30, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.linemodeleremail = QtGui.QLineEdit(self.groupBox_4)
        self.linemodeleremail.setGeometry(QtCore.QRect(280, 30, 161, 20))
        self.linemodeleremail.setObjectName(_fromUtf8("linemodeleremail"))

        self.retranslateUi(diagcloneprj)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), diagcloneprj.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), diagcloneprj.reject)
        QtCore.QMetaObject.connectSlotsByName(diagcloneprj)

    def retranslateUi(self, diagcloneprj):
        diagcloneprj.setWindowTitle(_translate("diagcloneprj", "Clone a project", None))
        self.groupBox.setTitle(_translate("diagcloneprj", "Original project", None))
        self.groupBox_2.setTitle(_translate("diagcloneprj", "Original project", None))
        self.btnoriginalprj.setText(_translate("diagcloneprj", "Browse", None))
        self.groupBox_3.setTitle(_translate("diagcloneprj", "Destination project", None))
        self.btndestinationprj.setText(_translate("diagcloneprj", "Browse", None))
        self.groupBox_4.setTitle(_translate("diagcloneprj", "Modeler", None))
        self.label.setText(_translate("diagcloneprj", "Name", None))
        self.label_2.setText(_translate("diagcloneprj", "Email", None))

