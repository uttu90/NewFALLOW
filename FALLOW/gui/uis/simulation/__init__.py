import sys
import os
import imp
import ConfigParser
from FALLOW.operations import utils
from FALLOW.constants import output_maps_key_ref, timeseries_key_ref
from FALLOW.models import tree

from PyQt4 import QtGui, QtCore

import SimulationUI

HEADER = ['Name', 'Path', 'Description']
FLAGS = [
    QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable,
    QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable,
    QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable |
    QtCore.Qt.ItemIsEditable,
]


class MainWindow(QtGui.QMainWindow, SimulationUI.Ui_MainWindow):
    def __init__(self, parent=None, project='D:/test FALLOW'):
        super(MainWindow, self).__init__(parent)
        self.project = project
        self.setupUi(self)
        self.model_file = os.path.join(project, 'model_file.py')
        self.simulation_module = imp.load_source('model_file', self.model_file)
        self.simulation = self.simulation_module.SimulatingThread(self.project)
        self.connect(self.playButton,
                     QtCore.SIGNAL('clicked()'),
                     self.on_play_click)
        self.connect(self.simulation, QtCore.SIGNAL("update"),
                     self.update_result)

    def update_result(self, output_timeseries, output_maps, time):
        self.output_map_model = tree.TreModel(HEADER, FLAGS,
                                              key_maps=output_maps,
                                              key_ref=output_maps_key_ref)
        self.mapOutput.setModel(self.output_map_model)
        self.output_time_model = tree.TreModel(HEADER, FLAGS,
                                               key_maps=output_timeseries,
                                               key_ref=timeseries_key_ref)
        self.timeseriesOutput.setModel(self.output_time_model)
        self.yearNumber.display(int(time) + 1)

    def on_play_click(self):
        self.simulation.start()

    def on_pause_click(self):
        pass

    def on_stop_click(self):
        pass

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()
    del form
