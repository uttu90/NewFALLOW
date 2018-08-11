import os
import json
import sys
import warnings

import numpy
from PyQt5 import QtCore, QtWidgets
import tree_model
from matplotlib import cm as cms
from matplotlib.cbook import MatplotlibDeprecationWarning
from osgeo import gdal

from matplotlib.figure import Figure
from matplotlib import colors as colorsmap
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from matplotlib.backends import qt_compat

import inputMaps_dialog_ui
import model
from FALLOW import map_models

import pcraster

warnings.simplefilter(action="ignore", category=MatplotlibDeprecationWarning)
warnings.simplefilter(action="ignore", category=RuntimeWarning)


use_pyside = qt_compat.QT_API == qt_compat.QT_API_PYSIDE

filters = "Tiff Files (*.tif *.png *.jpg *.jpg2000);;All files(*.*)"
HEADER = ['Name', 'Path', 'Description']
FLAGS = [
    QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable,
    QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable,
    QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable |
    QtCore.Qt.ItemIsEditable,
]


def make_cmap(colors):
    for i in range(len(colors)):
        colors[i] = (float((colors[i][0]))/255,
                     float((colors[i][1]))/255,
                     float((colors[i][2]))/255)
    cmap = colorsmap.ListedColormap(colors)
    return cmap

lc_colors = [
    (255, 255, 255), (150, 255, 0), (0, 255, 0), (0, 125, 0),
    (0, 75, 0), (255, 255, 0), (255, 0, 0), (255, 150, 0),
    (115, 165, 139), (215, 215, 0), (175, 175, 0), (130, 130, 0),
    (91, 91, 255), (33, 33, 205), (0, 0, 204), (0, 0, 150),
    (232, 138, 116), (225, 104, 75), (204, 66, 34), (150, 50, 25),
    (255, 45, 255), (226, 0, 226), (150, 0, 150), (200, 200, 200),
    (150, 150, 150), (75, 75, 75), (25, 25, 25), (175, 255, 255),
    (25, 255, 255), (0, 223, 218), (0, 150, 150), (255, 199, 143),
    (255, 161, 67), (250, 125, 0), (200, 100, 0), (255, 205, 215),
    (255, 151, 171), (255, 101, 130), (255, 50, 90), (255, 50, 90)]
lc_cm = make_cmap(lc_colors)
areacolors = [(102, 51, 0)]
area_cm = make_cmap(areacolors)
boolean_colors = [(0, 0, 255), (255, 0, 0)]
boolean_cm = make_cmap(boolean_colors)
fire_cm = make_cmap([(102, 255, 255), (255, 0, 0)])
soil_cm = make_cmap([(204, 102, 0), (168, 84, 0), (136, 68, 0),
                     (100, 50, 0), (64, 32, 0)])

COLORS = {
    'Simulated area': {'colors': area_cm, 'ticks': [1]},
    'Initial landcover': {'colors': lc_cm, 'ticks': [i for i in range(41)]},
    'Soil fertility': {'colors': soil_cm, 'ticks': [i for i in range(6)]},
    'Sub-catchment area': {'colors': boolean_cm, 'ticks': [0, 1]},
    'Initial logging area': {'colors': boolean_cm, 'ticks': [0, 1]},
    'Suitable area': {'colors': boolean_cm, 'ticks': [0, 1]},
    'Protected area': {'colors': boolean_cm, 'ticks': [0, 1]},
    'Disastered area': {'colors': boolean_cm, 'ticks': [0, 1]},
}


class MapsDialog(QtWidgets.QDialog, inputMaps_dialog_ui.Ui_Dialog):
    def __init__(self, parent=None, input_directory=''):
        super(MapsDialog, self).__init__(parent)
        self.setupUi(self)

        # self.create_plot_frame()
        self.path = input_directory or  os.path.dirname(__file__)
        self.map_file = os.path.join(self.path, 'maps.json')
        abstract_model = self.load()
        self.active_node = None
        self.maps_treeView.setModel(abstract_model)
        self.root = abstract_model.root_item

        self.maps_treeView.clicked.connect(self.on_row_clicked)
        self.maps_treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.maps_treeView.customContextMenuRequested.connect(
            self.on_open_context_menu
        )

        # Define action:
        self.open_map = QtWidgets.QAction('Open map', self)
        self.set_description = QtWidgets.QAction('Set description', self)
        self.select_type = QtWidgets.QAction('Select type', self)

        # Connect action:
        self.open_map.triggered.connect(self.on_open_map)
        self.set_description.triggered.connect(self.on_set_description)
        self.select_type.triggered.connect(self.on_select_type)

        self.popMenu = QtWidgets.QMenu(self)
        self.popMenu.addAction(self.open_map)
        self.popMenu.addAction(self.set_description)
        self.popMenu.addAction(self.select_type)

        self.main_frame = None
        self.fig = None
        self.canvas = None
        self.mpl_toolbar = None

        self.create_plot_frame()

    def load(self):
        try:
            with open(self.map_file) as model_file:
                map_model = json.load(model_file)
                abstract_model = tree_model.TreeModel(
                    parent=None,
                    headers=['text', 'path', 'description', 'type'],
                    input_model=map_model
                )
        except IOError:
            abstract_model = tree_model.TreeModel(
                parent=None,
                headers=['text', 'path', 'description', 'type'],
                input_model=map_models.map_model
            )

        return abstract_model

    def on_open_context_menu(self, point):
        selected_indexes = self.maps_treeView.selectedIndexes()
        try:
            active_index = selected_indexes[0]
            active_node = active_index.internalPointer()
            if active_node.rows() == 0:
                self.active_node = active_node
                self.popMenu.exec_(
                    self.maps_treeView.viewport().mapToGlobal(point)
                )
            else:
                self.active_node = None
        except IndexError:
            self.active_node = None

    def on_open_map(self):
        options = QtWidgets.QFileDialog.Options()
        if self.active_node:
            filename = QtWidgets.QFileDialog.getOpenFileName(
                        self,
                        "QFileDialog.getOpenFileName()",
                        "",
                        "All Files (*);;Map Files (*.tif)",
                        options=options)
            self.active_node.set_data('path', filename[0])
            self._display_map()

    def on_set_description(self):
        if not self.active_node:
            return
        text, ok = QtWidgets.QInputDialog.getText(
                    self,
                    "Set description",
                    "Input map description: ",
                    QtWidgets.QLineEdit.Normal,
                    self.active_node.data['description']
                )
        if ok:
            self.active_node.set_data('description', text)

    def on_select_type(self):
        items = ("linear", "bool", "landcover", "landuse")

        item, ok = QtWidgets.QInputDialog.getItem(
                        self,
                        "Select map type",
                        "Type: ",
                        items,
                        0,
                        False)

        if ok and item:
            self.active_node.set_data('type', item)
            self._display_map()

    @staticmethod
    def _get_type(node):
        parent = node
        while parent.parent().name != 'root':
            parent = parent.parent()
        return parent.name

    def on_row_clicked(self, index):
        node = index.internalPointer()
        if node.rows() > 0:
            return
        self.active_node = node
        self._display_map()

    def create_plot_frame(self):
        self.main_frame = self.map_frame
        self.fig = Figure((1.0, 1.0), dpi=60)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.main_frame)
        self.canvas.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.canvas.setFocus()
        self.canvas.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding)
        self.mpl_toolbar = NavigationToolbar(self.canvas, self.main_frame)
        self.canvas.mpl_connect('key_press_event', self.on_key_press)
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.canvas)  # the matplotlib canvas
        vbox.addWidget(self.mpl_toolbar)
        self.main_frame.setLayout(vbox)

    def _get_color_bar(self, map_type):
        result = {}
        try:
            color_map = COLORS[map_type]['colors']
            data = COLORS[map_type]['ticks']
            result['mappable'] = self.axes.imshow(
                self.elevationm,
                cmap=cms.get_cmap(color_map),
                vmin=data[0], vmax=data[-1],
                interpolation='nearest',
                aspect='equal')
            result['ticks'] = data
        except KeyError:
            result['mappable'] = self.axes.imshow(
                self.elevationm,
                interpolation='nearest',
                aspect='equal')
        return result

    def _display_map(self):
        if not self.active_node:
            return
        file_name = self.active_node.data['path']
        map_type = self.active_node.data['type'] or 'linear'

        if file_name:
            ds = gdal.Open(file_name)
            band = ds.GetRasterBand(1)
            # print band
            elevation = band.ReadAsArray()
            # print(ds.GetGeoTransform())
            geoTransform = ds.GetGeoTransform()
            # print elevation.shape(0)
            # print(elevation)
            # print(elevation.shape)
            # print(elevation)
            # print(elevation)
            pcraster.setclone(elevation.shape[0], elevation.shape[1], geoTransform[1], geoTransform[0], geoTransform[3])

            self.elevationm = numpy.ma.masked_where(
                elevation<=-9999,
                elevation)
            abc = (elevation == 1) * 1.0
            farr = numpy.ma.filled(abc, -9999)

            n2p = pcraster.numpy2pcr(pcraster.Nominal, farr, -9999)
            self.fig.clear()
            self.axes = self.fig.add_subplot(111)
            self.fig.colorbar(**self._get_color_bar(map_type))

            self.canvas.draw()
            self.canvas.mpl_connect('button_press_event', self.on_click)

    def on_key_press(self, event):
        key_press_handler(event, self.canvas, self.mpl_toolbar)

    def on_click(self, event):
        if event.button == 2:
            x_data = event.xdata
            y_data = event.ydata
            try:
                float(self.elevationm[y_data][x_data])
                abc = 'x=%.3f, y=%.3f, value = %.3f' % (
                    x_data,
                    y_data,
                    self.elevationm[y_data+0.5][x_data+0.5])
            except:
                abc = 'x=%.3f, y=%.3f, value = nv' % (
                    x_data, y_data)
            message = QtWidgets.QMessageBox(self)
            message.setWindowTitle("Value")
            message.setText(abc)
            message.setStyleSheet(
                "QMessageBox { messagebox-text-interaction-flags: 5; }"
            )
            message.show()

    def accept(self):
        map_data = []
        self.root.to_json(map_data)
        with open(self.map_file, 'wb') as map_file:
            json.dump(map_data[0]['root'], map_file, indent=2)
        super(MapsDialog, self).accept()


def main():
    app = QtWidgets.QApplication(sys.argv)
    dialog = MapsDialog()
    dialog.show()
    app.exec_()


if __name__ == '__main__':
    main()
