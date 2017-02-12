import sys
import os
import ConfigParser

from PyQt4 import QtGui, QtCore

import MainWindowUI
from FALLOW.gui.uis import input_maps
from FALLOW.gui.uis import input_timeseries
from FALLOW.gui.uis.prj import prj_clone, prj_create, prj_open


APP = 'application'
CURRENT_PROJECT = 'current project'

class MainWindow(QtGui.QMainWindow, MainWindowUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.languageDirectory = "translates/"
        self.languagelocale = "en"
        self.languageTranslator = QtCore.QTranslator()
        self.config = ConfigParser.RawConfigParser()
        if os.path.isfile('app.cfg'):
            self.config.read('app.cfg')
            self.project_path = self.config.get(APP, CURRENT_PROJECT)
            self._update_title()
        else:
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
            self.project_path = prj_interface.return_value()
        self._update_config()

    def on_open_project_click(self):
        prj_interface = prj_open.OpenProject(self)
        prj_interface.show()
        if prj_interface.exec_():
            self.project_path = prj_interface.return_value()
        self._update_config()

    def on_clone_project_click(self):
        prj_interface = prj_clone.CloneProject(self)
        prj_interface.show()
        if prj_interface.exec_():
            self.project_path = prj_interface.return_value()
        self._update_config()

    def on_input_map_click(self):
        if self.project_path:
            map_interface = input_maps.MainWindow(self,
                                                  directory=self.project_path)
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
        languageFilePath = r"C:\Users\UTTU\Documents\GitHub\
        NewFALLOW\FALLOW\gui\uis\translates\qt_vi.qm"
        self.languageTranslator = QtCore.QTranslator()
        if self.languageTranslator.load(languageFilePath):
            app.installTranslator(self.languageTranslator)

    def _update_config(self):
        try:
            self.config.add_section(APP)
        except ConfigParser.DuplicateSectionError:
            pass
        self.config.set(APP, CURRENT_PROJECT,
                        self.project_path)
        config_path = 'app.cfg'
        with open(config_path, 'wb') as configfile:
            self.config.write(configfile)
        self._update_title()

    def _update_title(self):
        current_title = 'FALLOW - ' + self.project_path
        self.setWindowTitle(current_title)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()
    del form