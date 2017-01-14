#!/usr/bin/env python
#-*- coding:utf-8 -*-

#---------
# IMPORT
#---------
import sys, os, re

import sip
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)

from PyQt4 import QtGui, QtCore

#---------
# DEFINE
#---------
class MyWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        self.languageDirectory  = "C:/Users/UTTU/Documents/GitHub/Fallow/"
        self.languageLocale     = "en"
        self.languageTranslator = QtCore.QTranslator()

        self.centralWidget = QtGui.QWidget(self)

        self.labelLanguageSelect = QtGui.QLabel(self.centralWidget)
        self.labelLanguageChange = QtGui.QLabel(self.centralWidget)

        self.comboBoxLanguage = QtGui.QComboBox(self.centralWidget)
        self.comboBoxLanguage.addItem("en" , "")

        for filePath in os.listdir(self.languageDirectory):
            fileName  = os.path.basename(filePath)
            fileMatch = re.match("qt_([a-z]{2,}).qm", fileName)
            if fileMatch:
                self.comboBoxLanguage.addItem(fileMatch.group(1), filePath)

        self.sortFilterProxyModelLanguage = QtGui.QSortFilterProxyModel(self.comboBoxLanguage)
        self.sortFilterProxyModelLanguage.setSourceModel(self.comboBoxLanguage.model())

        self.comboBoxLanguage.model().setParent(self.sortFilterProxyModelLanguage)
        self.comboBoxLanguage.setModel(self.sortFilterProxyModelLanguage)
        self.comboBoxLanguage.currentIndexChanged.connect(self.on_comboBoxLanguage_currentIndexChanged)
        self.comboBoxLanguage.model().sort(0)

        self.buttonBox = QtGui.QDialogButtonBox(self.centralWidget)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Yes|QtGui.QDialogButtonBox.Cancel)
        self.buttonBox.clicked.connect(self.on_buttonBox_clicked)

        self.layoutGrid = QtGui.QGridLayout(self.centralWidget)
        self.layoutGrid.addWidget(self.labelLanguageSelect, 0, 0, 1, 1)
        self.layoutGrid.addWidget(self.comboBoxLanguage, 0, 1, 1, 1)
        self.layoutGrid.addWidget(self.labelLanguageChange, 1, 0, 1, 1)
        self.layoutGrid.addWidget(self.buttonBox, 1, 1, 1, 1)

        self.setCentralWidget(self.centralWidget)
        self.retranslateUi()
        self.resetLanguage()
        self.updateButtons()

    @QtCore.pyqtSlot()
    def on_comboBoxLanguage_currentIndexChanged(self):
        self.setLanguage()
        self.updateButtons()

    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.LanguageChange:
            self.retranslateUi()

        super(MyWindow, self).changeEvent(event)

    @QtCore.pyqtSlot(QtGui.QAbstractButton)
    def on_buttonBox_clicked(self, button):
        buttonRole = self.buttonBox.buttonRole(button)

        if buttonRole == QtGui.QDialogButtonBox.YesRole:
            self.languageLocale = self.comboBoxLanguage.currentText()
            self.updateButtons()

        elif buttonRole == QtGui.QDialogButtonBox.RejectRole:
            self.resetLanguage()

    def resetLanguage(self):
        index = self.comboBoxLanguage.findText(self.languageLocale)
        self.comboBoxLanguage.setCurrentIndex(index)

    def setLanguage(self):
        app = QtGui.QApplication.instance()
        app.removeTranslator(self.languageTranslator)

        languageIndex      = self.comboBoxLanguage.currentIndex()
        languageFileName   = self.comboBoxLanguage.itemData(languageIndex, QtCore.Qt.UserRole)

        print languageFileName
        if languageFileName != "en":
            languageFilePath = os.path.join(self.languageDirectory, languageFileName)
        else:
            languageFilePath = ""
        print languageFilePath
        self.languageTranslator = QtCore.QTranslator()

        if self.languageTranslator.load(languageFilePath):
            app.installTranslator(self.languageTranslator)

    def updateButtons(self):
        state = self.languageLocale != self.comboBoxLanguage.currentText()

        self.buttonBox.button(QtGui.QDialogButtonBox.Cancel).setEnabled(state)
        self.buttonBox.button(QtGui.QDialogButtonBox.Yes).setEnabled(state)

    def retranslateUi(self):
        # This text is not included in te .qm file.
        # You'll have to create your own .qm file specifying the translation,
        # otherwise it won't get translated.

        self.labelLanguageSelect.setText(self.tr("Select Language:"))
        self.labelLanguageChange.setText(self.tr("Change Language:"))

#---------
# MAIN
#---------
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('MyWindow')

    main = MyWindow()
    main.resize(333, 111)
    main.show()

    sys.exit(app.exec_())