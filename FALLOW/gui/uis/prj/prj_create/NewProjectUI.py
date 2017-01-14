# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\newproject.ui'
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

class Ui_diagnewprj(object):
    def setupUi(self, diagnewprj):
        diagnewprj.setObjectName(_fromUtf8("diagnewprj"))
        diagnewprj.resize(550, 428)
        self.buttonBox = QtGui.QDialogButtonBox(diagnewprj)
        self.buttonBox.setGeometry(QtCore.QRect(190, 380, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.prjdirectory = QtGui.QGroupBox(diagnewprj)
        self.prjdirectory.setGeometry(QtCore.QRect(20, 20, 511, 71))
        self.prjdirectory.setObjectName(_fromUtf8("prjdirectory"))
        self.lineprjdirectory = QtGui.QLineEdit(self.prjdirectory)
        self.lineprjdirectory.setGeometry(QtCore.QRect(10, 30, 361, 20))
        self.lineprjdirectory.setObjectName(_fromUtf8("lineprjdirectory"))
        self.btnprjdirectory = QtGui.QPushButton(self.prjdirectory)
        self.btnprjdirectory.setGeometry(QtCore.QRect(410, 30, 75, 23))
        self.btnprjdirectory.setObjectName(_fromUtf8("btnprjdirectory"))
        self.modeler = QtGui.QGroupBox(diagnewprj)
        self.modeler.setGeometry(QtCore.QRect(20, 110, 511, 71))
        self.modeler.setObjectName(_fromUtf8("modeler"))
        self.label = QtGui.QLabel(self.modeler)
        self.label.setGeometry(QtCore.QRect(20, 30, 31, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.modeler)
        self.label_2.setGeometry(QtCore.QRect(230, 30, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.linemodelername = QtGui.QLineEdit(self.modeler)
        self.linemodelername.setGeometry(QtCore.QRect(60, 30, 151, 20))
        self.linemodelername.setObjectName(_fromUtf8("linemodelername"))
        self.linemodeleremail = QtGui.QLineEdit(self.modeler)
        self.linemodeleremail.setGeometry(QtCore.QRect(260, 30, 221, 20))
        self.linemodeleremail.setObjectName(_fromUtf8("linemodeleremail"))
        self.groupBox = QtGui.QGroupBox(diagnewprj)
        self.groupBox.setGeometry(QtCore.QRect(20, 200, 511, 71))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lineinputpara = QtGui.QLineEdit(self.groupBox)
        self.lineinputpara.setGeometry(QtCore.QRect(10, 30, 361, 20))
        self.lineinputpara.setObjectName(_fromUtf8("lineinputpara"))
        self.btninputpara = QtGui.QPushButton(self.groupBox)
        self.btninputpara.setGeometry(QtCore.QRect(410, 30, 75, 23))
        self.btninputpara.setObjectName(_fromUtf8("btninputpara"))
        self.groupBox_2 = QtGui.QGroupBox(diagnewprj)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 290, 511, 71))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.linemodelfile = QtGui.QLineEdit(self.groupBox_2)
        self.linemodelfile.setGeometry(QtCore.QRect(10, 30, 361, 20))
        self.linemodelfile.setObjectName(_fromUtf8("linemodelfile"))
        self.btnmodelfile = QtGui.QPushButton(self.groupBox_2)
        self.btnmodelfile.setGeometry(QtCore.QRect(410, 30, 75, 23))
        self.btnmodelfile.setObjectName(_fromUtf8("btnmodelfile"))

        self.retranslateUi(diagnewprj)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), diagnewprj.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), diagnewprj.reject)
        QtCore.QMetaObject.connectSlotsByName(diagnewprj)

    def retranslateUi(self, diagnewprj):
        diagnewprj.setWindowTitle(_translate("diagnewprj", "Create new project", None))
        self.prjdirectory.setTitle(_translate("diagnewprj", "Directory", None))
        self.btnprjdirectory.setText(_translate("diagnewprj", "Browse", None))
        self.modeler.setTitle(_translate("diagnewprj", "Modeler", None))
        self.label.setText(_translate("diagnewprj", "Name", None))
        self.label_2.setText(_translate("diagnewprj", "Email", None))
        self.groupBox.setTitle(_translate("diagnewprj", "Input paramters", None))
        self.btninputpara.setText(_translate("diagnewprj", "Browse", None))
        self.groupBox_2.setTitle(_translate("diagnewprj", "Model File", None))
        self.btnmodelfile.setText(_translate("diagnewprj", "Browse", None))

