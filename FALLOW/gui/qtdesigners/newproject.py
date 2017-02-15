# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newproject.ui'
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
        diagnewprj.resize(550, 542)
        self.buttonBox = QtGui.QDialogButtonBox(diagnewprj)
        self.buttonBox.setGeometry(QtCore.QRect(190, 490, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.prjdirectory = QtGui.QGroupBox(diagnewprj)
        self.prjdirectory.setGeometry(QtCore.QRect(20, 10, 511, 71))
        self.prjdirectory.setObjectName(_fromUtf8("prjdirectory"))
        self.lineprjdirectory_2 = QtGui.QLineEdit(self.prjdirectory)
        self.lineprjdirectory_2.setGeometry(QtCore.QRect(10, 30, 361, 20))
        self.lineprjdirectory_2.setObjectName(_fromUtf8("lineprjdirectory_2"))
        self.btnprjdirectory = QtGui.QPushButton(self.prjdirectory)
        self.btnprjdirectory.setGeometry(QtCore.QRect(410, 30, 75, 23))
        self.btnprjdirectory.setObjectName(_fromUtf8("btnprjdirectory"))
        self.modeler = QtGui.QGroupBox(diagnewprj)
        self.modeler.setGeometry(QtCore.QRect(20, 90, 511, 71))
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
        self.groupBox.setGeometry(QtCore.QRect(20, 170, 511, 151))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lineinputpara = QtGui.QLineEdit(self.groupBox)
        self.lineinputpara.setGeometry(QtCore.QRect(170, 30, 201, 20))
        self.lineinputpara.setObjectName(_fromUtf8("lineinputpara"))
        self.btninputpara = QtGui.QPushButton(self.groupBox)
        self.btninputpara.setGeometry(QtCore.QRect(410, 30, 75, 23))
        self.btninputpara.setObjectName(_fromUtf8("btninputpara"))
        self.linemodelfile = QtGui.QLineEdit(self.groupBox)
        self.linemodelfile.setGeometry(QtCore.QRect(170, 70, 201, 20))
        self.linemodelfile.setObjectName(_fromUtf8("linemodelfile"))
        self.btnmodelfile = QtGui.QPushButton(self.groupBox)
        self.btnmodelfile.setGeometry(QtCore.QRect(410, 70, 75, 23))
        self.btnmodelfile.setObjectName(_fromUtf8("btnmodelfile"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 30, 141, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 70, 141, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(20, 110, 141, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.linemapfile = QtGui.QLineEdit(self.groupBox)
        self.linemapfile.setGeometry(QtCore.QRect(170, 110, 201, 20))
        self.linemapfile.setObjectName(_fromUtf8("linemapfile"))
        self.btnmapfile = QtGui.QPushButton(self.groupBox)
        self.btnmapfile.setGeometry(QtCore.QRect(410, 110, 75, 23))
        self.btnmapfile.setObjectName(_fromUtf8("btnmapfile"))
        self.groupBox_3 = QtGui.QGroupBox(diagnewprj)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 330, 511, 131))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 121, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.linetime = QtGui.QLineEdit(self.groupBox_3)
        self.linetime.setGeometry(QtCore.QRect(160, 30, 51, 20))
        self.linetime.setObjectName(_fromUtf8("linetime"))
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 121, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.linepixelsize = QtGui.QLineEdit(self.groupBox_3)
        self.linepixelsize.setGeometry(QtCore.QRect(160, 60, 51, 20))
        self.linepixelsize.setObjectName(_fromUtf8("linepixelsize"))
        self.label_5 = QtGui.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(20, 90, 121, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.checkBox = QtGui.QCheckBox(self.groupBox_3)
        self.checkBox.setGeometry(QtCore.QRect(160, 90, 70, 17))
        self.checkBox.setText(_fromUtf8(""))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))

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
        self.groupBox.setTitle(_translate("diagnewprj", "Files", None))
        self.btninputpara.setText(_translate("diagnewprj", "Browse", None))
        self.btnmodelfile.setText(_translate("diagnewprj", "Browse", None))
        self.label_6.setText(_translate("diagnewprj", "Input parameters (.xls)", None))
        self.label_7.setText(_translate("diagnewprj", "Simulation (.py)", None))
        self.label_8.setText(_translate("diagnewprj", "Maps (.json)", None))
        self.btnmapfile.setText(_translate("diagnewprj", "Browse", None))
        self.groupBox_3.setTitle(_translate("diagnewprj", "Options", None))
        self.label_3.setText(_translate("diagnewprj", "Simulation time (years)", None))
        self.linetime.setText(_translate("diagnewprj", "30", None))
        self.label_4.setText(_translate("diagnewprj", "Pixel size (ha)", None))
        self.linepixelsize.setText(_translate("diagnewprj", "4", None))
        self.label_5.setText(_translate("diagnewprj", "Using timeseries", None))

