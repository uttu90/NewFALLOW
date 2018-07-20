import os
import json
import sys
import warnings

import numpy
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
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

import MapInputUI
import model
# from FALLOW.models import tree

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


class MainWindow(QtWidgets.QMainWindow, MapInputUI.Ui_MainWindow):
    def __init__(self, parent=None, directory=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        # self.activeIndex = None
        self.create_plot_frame()
        self.directory = directory or  os.path.dirname(__file__)
        self.map_file = os.path.join(self.directory, 'maps.json')
        # self.directory = directory
        self.changed = False
        model = tree_model.TreeModel(parent=None, headers=['text', 'path', 'description', 'type'])
        self.mapTree.setModel(model)
        self.root = model.rootItem
        # if os.path.isfile(self.map_file):
        #     self.MapInputModel = tree.TreModel(HEADER,
        #                                        FLAGS,
        #                                        file=self.map_file)
        #     self.MapInputTreeView.setModel(self.MapInputModel)
        # else:
        #     self.MapInputModel = tree.TreModel(HEADER,
        #                                        FLAGS,
        #                                        file='maps.json')
        #     self.MapInputTreeView.setModel(self.MapInputModel)
        # self.root = self.MapInputModel.rootNode
        # self.connect(self.action_Open,
        #              QtCore.SIGNAL("triggered()"),
        #              self.on_open_clicked)
        # self.connect(self.action_Save,
        #              QtCore.SIGNAL("triggered()"),
        #              self.on_save_clicked)
        self.mapTree.clicked.connect(self.row_clicked)
        self.mapTree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.mapTree.customContextMenuRequested.connect(self.on_open_context_menu)
        # self.connect(self.openMap, QtCore.SIGNAL("trigge"))
        self.openMap.triggered.connect(self.on_open_clicked)
        self.save.triggered.connect(self.on_save_clicked)
        # QtCore.QObject.connect(self.mapTree,
        #                        QtCore.SIGNAL("clicked (QModelIndex)"),
        #                        self.row_clicked)
        SAMPLE_FILE = 'C:\Users\uttu\NewFALLOW\FALLOW\projects\samples\INPUT\maps\BK_area.tif'
        self.activeIndex = None
        self._changed = False
        self._display_map(SAMPLE_FILE)

        self.popMenu = QtWidgets.QMenu(self)
        self.popMenu.addAction(QtWidgets.QAction('test0', self))
        self.popMenu.addAction(QtWidgets.QAction('test1', self))
        self.popMenu.addSeparator()
        self.popMenu.addAction(self.openMap)
        self.popMenu.addAction(QtWidgets.QAction('test2', self))

    def on_open_context_menu(self, point):
        # print 'Hello world'
        print point
        indexes = self.mapTree.selectedIndexes()
        print indexes
        try:
            for index in indexes:
                print index.internalPointer()
                # print index.connectlumn(), index.row(), index.data()
        except:
            print 'error'

    def _display_message(self, title, message, promt):
        m_dialg = QtWidgets.QMessageBox(self)
        yesbtn = m_dialg.addButton(QtWidgets.QMessageBox.Yes)
        m_dialg.setWindowTitle(title)
        m_dialg.setText(message)
        QtCore.QObject.connect(yesbtn, QtCore.SIGNAL("clicked()"),
                               promt)
        m_dialg.addButton(QtWidgets.QMessageBox.No)
        m_dialg.show()

    @staticmethod
    def _get_type(node):
        parent = node
        while parent.parent().name != 'root':
            parent = parent.parent()
        return parent.name

    def row_clicked(self, index):
        node = index.internalPointer()
        print node
        # print index.column(), index.row()
        if node.rows() > 0:
            return
        if index.column() == 0:
            print 'abc'
            self.activeIndex = index
            # self._display_message('abc')
        # self.activeIndex = index
        # active_node = index.internalPointer()
        # if len(active_node.children()) == 0:
            data = node.data['path']
            if os.path.isfile(data):
                self._display_map(data)
            # elif not data:
        #         m_title = 'No file selected'
        #         m_message = 'Would you like to choose a map file?'
        #         self._display_message(m_title, m_message, self.on_open_clicked)
        #     else:
        #         m_title = 'Your file path is invalid'
        #         m_message = 'Would you like to chooes another file?'
        #         self._display_message(m_title, m_message, self.on_open_clicked)

    def on_open_clicked(self):
        # print self.activeIndex
        options = QtWidgets.QFileDialog.Options()

        if self.activeIndex:
            active_node = self.activeIndex.internalPointer()
            filename  = QtWidgets.QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
                # filter=filters,
                # directory=self.directory)
            active_node.set_data('path', filename[0])

            self._changed = True
            if self.activeIndex.column() == 0:
                data = active_node.data['path']
                self._display_map(data)

    def create_plot_frame(self):
        self.main_frame = self.MapInputWidget
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

    def _display_map(self, filename, map_type=None):
        if filename:
            ds = gdal.Open(filename)
            band = ds.GetRasterBand(1)
            elevation = band.ReadAsArray()
            self.elevationm= numpy.ma.masked_where(elevation<=-9999,elevation)
            self.fig.clear()
            self.axes = self.fig.add_subplot(111)
            self.fig.colorbar(**self._get_color_bar(map_type))

            self.canvas.draw()
            self.canvas.mpl_connect('button_press_event', self.onclick)

    def on_key_press(self, event):
        key_press_handler(event, self.canvas, self.mpl_toolbar)

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
            message.setStyleSheet("QMessageBox { messagebox-text-interaction-flags: 5; }")
            message.show()

    def on_save_clicked(self):
        self.changed = False
        map_data = []
        self.root.to_json(map_data)
        with open(self.map_file, 'wb') as map_file:
            json.dump(map_data[0]['root'], map_file, indent=2)
        self._changed = False

    def format_coord(self, xdata, ydata):
        try:
            float(self.elevationm[ydata][xdata])
            abc = 'x=%.3f, y=%.3f ' % (
                xdata, ydata)
        except:
            abc = 'x=%.3f, y=%.3f, value = nv' % (xdata, ydata)
        return abc

    def closeEvent(self, event):
        if self.changed:
            reply = QtGui.QMessageBox.question(
                self,
                'Message',
                "Do you want to save your input before quitting?",
                QtGui.QMessageBox.Yes,
                QtGui.QMessageBox.No,
                QtGui.QMessageBox.Cancel)
            if reply == QtGui.QMessageBox.Yes:
                self.save()
                event.accept()
            elif reply == QtGui.QMessageBox.Cancel:
                event.ignore()
            else:
                event.accept()
        else:
            event.accept()


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()
if __name__ == '__main__':
    main()
