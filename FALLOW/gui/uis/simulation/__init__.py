import sys
import os
import imp
import warnings

import numpy

from FALLOW.constants import output_maps_key_ref, timeseries_key_ref
from FALLOW.models import tree

from PyQt4 import QtGui, QtCore

from matplotlib import cm as cms
from matplotlib.cbook import MatplotlibDeprecationWarning
from osgeo import gdal

from matplotlib.figure import Figure
from matplotlib import colors as colorsmap
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from matplotlib.backends import qt4_compat

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
        self._create_plot_frame()
        self.model_file = os.path.join(project, 'model_file.py')
        self.simulation_module = imp.load_source('model_file', self.model_file)
        self.simulation = self.simulation_module.SimulatingThread(self.project)
        self.connect(self.playButton,
                     QtCore.SIGNAL('clicked()'),
                     self.on_play_click)
        self.connect(self.simulation, QtCore.SIGNAL("update"),
                     self.update_result)
        QtCore.QObject.connect(self.mapOutput,
                               QtCore.SIGNAL("clicked (QModelIndex)"),
                               self.row_map_clicked)
        QtCore.QObject.connect(self.timeseriesOutput,
                               QtCore.SIGNAL("clicked (QModelIndex)"),
                               self.row_timeseries_clicked)
        self.active_node = None
        self.data_type = 'map'

    def update_result(self, output_timeseries, output_maps, time):
        self.output_map_model = tree.TreModel(HEADER, FLAGS,
                                              key_maps=output_maps,
                                              key_ref=output_maps_key_ref)
        self.mapOutput.setModel(self.output_map_model)
        self.output_time_model = tree.TreModel(HEADER, FLAGS,
                                               key_maps=output_timeseries,
                                               key_ref=timeseries_key_ref)
        self.timeseriesOutput.setModel(self.output_time_model)
        self.time = time
        self.yearNumber.display(int(time) + 1)
        self._display_timeseries(output_timeseries['Population'])
        if self.active_node:
            self.data = self.active_node.data()['value']
            if self.data_type == 'map':
                file_name = self.data[time]
                self._display_map(file_name)
            else:
                self._display_timeseries(self.data)

    def _create_plot_frame(self):
        self.main_frame = self.mapDisplay
        self.fig = Figure((1.0, 1.0), dpi=60)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.main_frame)
        self.canvas.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.canvas.setFocus()
        self.canvas.setSizePolicy(
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Expanding)
        self.mpl_toolbar = NavigationToolbar(self.canvas, self.main_frame)
        self.canvas.mpl_connect('key_press_event', self.on_key_press)
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.canvas)
        vbox.addWidget(self.mpl_toolbar)
        self.main_frame.setLayout(vbox)

    def on_play_click(self):
        self.simulation.start()

    def on_key_press(self, event):
        key_press_handler(event, self.canvas, self.mpl_toolbar)

    def on_pause_click(self):
        pass

    def on_stop_click(self):
        pass

    def display(self):
        pass

    def row_map_clicked(self, index):
        self.activeIndex = index
        self.active_node = index.internalPointer()
        self.data_type = 'map'
        if len(self.active_node.children()) == 0:
            self.data = self.active_node.data()['value']
            file_name = self.data[self.time]
            self._display_map(file_name)

    def row_timeseries_clicked(self, index):
        self.activeIndex = index
        self.active_node = index.internalPointer()
        self.data_type = 'time'
        if len(self.active_node.children()) == 0:
            self.data = self.active_node.data()['value']
            self._display_timeseries(self.data)

    def _display_timeseries(self, array):
        self.fig.clear()
        self.axes = self.fig.add_subplot(111)
        self.axes.set_xlim(0, len(array) - 1)
        self.axes.set_ylim(0, max(array) * 1.1)
        self.axes.set_autoscale_on(False)
        self.axes.plot(array, linestyle='steps-post')
        self.axes.set_xlabel('year')
        self.canvas.draw()

    def _display_map(self, filename, map_type=None):
        if filename:
            ds = gdal.Open(filename)
            band = ds.GetRasterBand(1)
            elevation = band.ReadAsArray()
            self.elevationm = numpy.ma.masked_where(
                elevation <= -9999,
                elevation)
            self.fig.clear()
            self.axes = self.fig.add_subplot(111)
            self.fig.colorbar(self.axes.imshow(
                self.elevationm,
                interpolation='nearest',
                aspect='equal'))
            self.canvas.draw()
            self.canvas.mpl_connect('button_press_event', self.onclick)

    def onclick(self, event):
        if event.button == 2:
            xdata = event.xdata
            ydata = event.ydata
            try:
                float(self.elevationm[ydata][xdata])
                abc = 'x=%.3f, y=%.3f, value = %.3f' % (
                    xdata, ydata, self.elevationm[ydata+0.5][xdata+0.5])
            except:
                abc = 'x=%.3f, y=%.3f, value = nv' % (
                    xdata, ydata)
            message = QtGui.QMessageBox(self)
            message.setWindowTitle("Value")
            message.setText(abc)
            message.setStyleSheet(
                "QMessageBox "
                "{ messagebox-text-interaction-flags: 5; }")
            message.show()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()
    del form
