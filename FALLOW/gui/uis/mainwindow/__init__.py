import sys
import imp
import json
from os import path
from PyQt5 import QtWidgets, QtCore

import MainWindowUI
from FALLOW.excel_utils import get_data
from FALLOW.gui.uis import input_maps


class App(QtWidgets.QMainWindow, MainWindowUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setupUi(self)
        self.showMaximized()

        self.path = ''
        self.data_path = ''
        self.config_file = ''

        self.data = {}
        self.config = {}
        self.maps = {}

        self.openProject.triggered.connect(self.on_open_project)
        self.inputMap.triggered.connect(self.on_input_map)
        self.importData.triggered.connect(self.on_import_data)
        self.reload.triggered.connect(self.on_reload)
        self.play.triggered.connect(self.on_play)

        # self.project_check.setCheckable(False)
        self.project_check.setCheckable(False)
        self.data_check.setCheckable(False)
        self.map_check.setCheckable(False)

    def on_open_project(self):
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(
            self,
            'Select project folder',
            self.path,
            QtWidgets.QFileDialog.ShowDirsOnly
        )

        if folder_path:
            self.path = folder_path
            self.setWindowTitle(self.windowTitle() + ' - ' + folder_path)
            self.handle_change_project()

    def handle_change_project(self):
        config_file = path.join(self.path, 'config.json')
        self.project_check.setCheckState(True)
        if path.isfile(config_file):
            try:
                with open(config_file) as config:
                    self.config = json.load(config)
                    self.data_path = self.config['data']
                    self.data_check.setCheckState(
                        not not self.data_path
                    )
                    if path.isfile(self.data_path):
                        self.data = get_data.get_data_from_file(
                            self.data_path, 'Summary'
                        )
                    self.map_check.setCheckState(
                        not not self.config['map']
                    )
            except:
                return
        else:
            self.update_config()

    def on_input_map(self):
        input_map_dialog = input_maps.MapsDialog(self, self.path)
        input_map_dialog.showMaximized()
        ok = input_map_dialog.exec_()
        if ok:
            self.map_check.setCheckState(path.isfile(path.join(
                self.path, 'maps.json'))
            )
            self.config['map'] = path.join(self.path, 'maps.json')
            self.update_config()
            self._load_map_file()

    def _load_map_file(self):
        with open(path.join(self.path, 'maps.json'), 'r') as map_file:
            self.maps = json.load(map_file)

    def on_import_data(self):
        options = QtWidgets.QFileDialog.Options()
        self.data_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            'Select data file',
            '',
            "All Files (*);;Excel Files (*.xls)",
            options=options
        )
        try:
            self.data = get_data.get_data_from_file(self.data_path, 'Summary')
            self.data_check.setCheckState(True)
            self.config['data'] = self.data_path
            self.update_config()
        except:
            return

    def update_config(self):
        config_file = path.join(self.path, 'config.json')
        with open(config_file, 'w') as config:
            json.dump(self.config, config)

    def on_reload(self):
        self.data = get_data.get_data_from_file(self.data_path, 'Summary')

    def on_play(self):
        if not self.path:
            self.show_message(
                'Missing directory',
                'Please find a project directory'
            )
            return

        if not self.data:
            self.show_message(
                'Missing data',
                'Please find a data file'
            )
            return

        if not self.maps:
            self.show_message(
                'Missing maps',
                'Please add maps'
            )
            return
        # print(self.data, self.maps)
        self.simulation_module = imp.load_source(
            'model', path.join(self.path, 'model.py')
        )
        self.simulation = self.simulation_module.SimulatingThread(
            data=self.data,
            maps=self.maps,
            project=self.path
        )
        self.simulation.start()

    @staticmethod
    def show_message(title, content):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(title)
        msg.setInformativeText(content)
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.exec_()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = App()
    form.show()
    app.exec_()
    del form