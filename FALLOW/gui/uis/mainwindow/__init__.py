import sys, os, re

from PyQt4 import QtGui, QtCore

import MainWindow

from FALLOW.gui.uis.prj import prj_clone, prj_create, prj_open
from FALLOW.gui.uis import input_maps
from FALLOW.gui.uis import input_timeseries


class MainWindow(QtGui.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.languageDirectory = "translates/"
        self.languagelocale = "en"
        self.languageTranslator = QtCore.QTranslator()
        self.project_path = None

        self.connect(self.actionVietnamese,
                     QtCore.SIGNAL('triggered()'),
                     self.on_vi_language_change)
        self.connect(self.actionEnglish,
                     QtCore.SIGNAL('triggered()'),
                     self.on_en_language_change)
        self.connect(self.actionCreate_new_project,
                     QtCore.SIGNAL('triggered()'),
                     self.on_create_new_project_click)
        self.connect(self.actionOpen_project,
                     QtCore.SIGNAL('triggered()'),
                     self.on_open_project_click)
        self.connect(self.actionClone_project,
                     QtCore.SIGNAL('triggered()'),
                     self.on_clone_project_click)
        self.connect(self.action_Maps,
                     QtCore.SIGNAL('triggered()'),
                     self.on_input_map_click)
        self.connect(self.action_Input_Timeseries,
                     QtCore.SIGNAL('triggered()'),
                     self.on_input_timeseries_click)
        self.connect(self.action_Play,
                     QtCore.SIGNAL('triggered()'),
                     self.on_play_click)
        self.connect(self.action_Pause,
                     QtCore.SIGNAL('triggered()'),
                     self.on_pause_click)
        self.connect(self.action_Stop,
                     QtCore.SIGNAL('triggered()'),
                     self.on_stop_click)
        self.connect(self.actionLand_cover,
                     QtCore.SIGNAL('triggered()'),
                     self.on_land_cover_click)
        self.connect(self.actionHelp,
                     QtCore.SIGNAL('triggered()'),
                     self.on_help_click)

    def on_create_new_project_click(self):
        prj_interface = prj_create.NewProject(self)
        prj_interface.show()
        if prj_interface.exec_():
            self.project_path = prj_interface.returnValues()

    def on_open_project_click(self):
        prj_interface = prj_open.OpenProject(self)
        prj_interface.show()
        if prj_interface.exec_():
            self.project_path = prj_interface.returnValues()

    def on_clone_project_click(self):
        prj_interface = prj_clone.CloneProject(self)
        prj_interface.show()
        if prj_interface.exec_():
            self.project_path = prj_interface.returnValues()

    def on_input_map_click(self):
        if self.project_path:
            map_interface = input_maps.MainWindow(
                self, directory=self.project_path)
            map_interface.show()

    def on_input_timeseries_click(self):
        if self.project_path:
            time_interface = input_timeseries.MainWindow(
                self, directory=self.project_path)
            time_interface.show()

    def on_play_click(self):
        pass

    def on_pause_click(self):
        pass

    def on_stop_click(self):
        pass

    def on_result_click(self):
        pass

    def on_land_cover_click(self):
        pass

    def on_help_click(self):
        pass

    @QtCore.pyqtSlot()
    def on_vi_language_change(self):
        self.setLanguage("vi")

    @QtCore.pyqtSlot()
    def on_en_language_change(self):
        self.resetLanguage()

    def resetLanguage(self):
        app = QtGui.QApplication.instance()
        app.removeTranslator(self.languageTranslator)
        self.languageTranslator = QtCore.QTranslator()
        languageFilePath = ""
        self.languageTranslator = QtCore.QTranslator()
        if self.languageTranslator.load(languageFilePath):
            app.installTranslator(self.languageTranslator)

    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.LanguageChange:
            self.retranslateUi(self)

        super(MainWindow, self).changeEvent(event)

    def setLanguage(self, language):
        app = QtGui.QApplication.instance()
        app.removeTranslator(self.languageTranslator)
        languageFilePath = r"C:\Users\UTTU\Documents\GitHub\NewFALLOW\FALLOW\gui\uis\translates\qt_vi.qm"
        self.languageTranslator = QtCore.QTranslator()
        if self.languageTranslator.load(languageFilePath):
            app.installTranslator(self.languageTranslator)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # app.setQuitOnLastWindowClosed(False)
    form = MainWindow()
    form.show()
    app.exec_()
    del form