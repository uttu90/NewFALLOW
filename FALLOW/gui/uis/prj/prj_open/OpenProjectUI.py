# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\openproject.ui'
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

class Ui_openprj(object):
    def setupUi(self, openprj):
        openprj.setObjectName(_fromUtf8("openprj"))
        openprj.resize(499, 162)
        self.buttonBox = QtGui.QDialogButtonBox(openprj)
        self.buttonBox.setGeometry(QtCore.QRect(140, 110, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.groupBox = QtGui.QGroupBox(openprj)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 461, 71))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lineopenprj = QtGui.QLineEdit(self.groupBox)
        self.lineopenprj.setGeometry(QtCore.QRect(20, 30, 291, 20))
        self.lineopenprj.setObjectName(_fromUtf8("lineopenprj"))
        self.btnopenprj = QtGui.QPushButton(self.groupBox)
        self.btnopenprj.setGeometry(QtCore.QRect(350, 30, 75, 23))
        self.btnopenprj.setObjectName(_fromUtf8("btnopenprj"))

        self.retranslateUi(openprj)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), openprj.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), openprj.reject)
        QtCore.QMetaObject.connectSlotsByName(openprj)

    def retranslateUi(self, openprj):
        openprj.setWindowTitle(_translate("openprj", "Open a project", None))
        self.groupBox.setTitle(_translate("openprj", "GroupBox", None))
        self.btnopenprj.setText(_translate("openprj", "Browse", None))

