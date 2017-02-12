import copy
import os
import pickle
import sys
import warnings

from FALLOW.models import MapsInput
import numpy
from PyQt4 import QtCore
from PyQt4 import QtGui
from matplotlib import cm as cms
from matplotlib.cbook import MatplotlibDeprecationWarning
from osgeo import gdal

import MapInputUI
from FALLOW.models import tree

warnings.simplefilter(action="ignore", category=MatplotlibDeprecationWarning)
warnings.simplefilter(action="ignore", category=RuntimeWarning)
from matplotlib.figure import Figure
from matplotlib import colors as colorsmap
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from matplotlib.backends import qt4_compat

use_pyside = qt4_compat.QT_API == qt4_compat.QT_API_PYSIDE

filters = "Tiff Files (*.tif *.png *.jpg *.jpg2000);;All files(*.*)"
HEADER = ['Name', 'Path', 'Description']
FLAGS = [
    QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable,
    QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable,
    QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable |
    QtCore.Qt.ItemIsEditable,
]

def make_cmap(colors, position=None, bit=False):
    for i in range(len(colors)):
        colors[i] = (float((colors[i][0]))/255,
                     float((colors[i][1]))/255,
                     float((colors[i][2]))/255)
    cmap = colorsmap.ListedColormap(colors)
    return cmap

colors = [(255, 255, 255), (150, 255, 0), (0, 255, 0), (0, 125, 0), (0, 75, 0),
          (255, 255, 0), (255, 0, 0), (255, 150, 0), (115, 165, 139), (215, 215, 0),
          (175, 175, 0), (130, 130, 0), (91, 91, 255), (33, 33, 205), (0, 0, 204),
          (0, 0, 150), (232, 138, 116), (225, 104, 75), (204, 66, 34), (150, 50, 25),
          (255, 45, 255), (226, 0, 226), (150, 0, 150), (200, 200, 200), (150, 150, 150),
          (75, 75, 75), (25, 25, 25), (175, 255, 255), (25, 255, 255), (0, 223, 218),
          (0, 150, 150), (255, 199, 143), (255, 161, 67), (250, 125, 0), (200, 100, 0),
          (255, 205, 215), (255, 151, 171), (255, 101, 130), (255, 50, 90), (255, 50, 90)]


class MainWindow(QtGui.QMainWindow, MapInputUI.Ui_MainWindow):
    def __init__(self, parent=None, directory="D:/test FALLOW"):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.activeIndex = None
        self.create_Plot_Frame()
        self.map_file = os.path.join(directory, 'maps.json')
        if os.path.isfile(self.map_file):
            self.MapInputModel = tree.TreModel(self.map_file, HEADER, FLAGS)
            self.MapInputTreeView.setModel(self.MapInputModel)
        else:
            self.MapInputModel = tree.TreModel('maps.json', HEADER, FLAGS)
            self.MapInputTreeView.setModel(self.MapInputModel)
        self.preferdirectory = "C:/"
        self.projectdirectory = directory + "\\Input\\"
        # self.fileName = self.projectdirectory + 'MapInput.pkl'
        # if os.path.isfile(self.fileName):
        #     with open(self.fileName, 'rb') as output:
        #         MapParameter = pickle.load(output)
        #         self.pixelsize = MapParameter[0]
        #         self.MapInputNode = MapParameter[1]
        #         output.close()
        # else:
        #     self.MapInputNode = MapsInput.rootNode
        #     self.pixelsize = 4
        # self.pixelsize_lineedit.setText(str(self.pixelsize))
        # self.MapInputModel = Tree(self.MapInputNode)
        # self.MapInputTreeView.setModel(self.MapInputModel)
        self.setupcolor()
        # Define action click
        self.connect(self.action_Open, QtCore.SIGNAL("triggered()"), self.on_Open_Clicked)
        self.connect(self.action_Compare, QtCore.SIGNAL("triggered()"), self.on_Compare_Clicked)
        self.connect(self.action_Save, QtCore.SIGNAL("triggered()"), self.on_Save_Clicked)
        QtCore.QObject.connect(self.MapInputTreeView, QtCore.SIGNAL("clicked (QModelIndex)"), self.row_clicked)
        QtCore.QObject.connect(self.MapInputTreeView, QtCore.SIGNAL("doubleclicked(QModelIndex)"), self.row_doubleclicked)

    def row_doubleclicked(self,index):
        self.activeIndex = index
        activeNode = self.activeIndex.internalPointer()
        filename = index.internalPointer().value()
        typename = index.internalPointer().name()
        ptypename = index.internalPointer().parent().name()
        print filename
        print typename
        if os.path.isfile(filename):
            self.MapsDisplay(filename, typename)

    def setupcolor(self):
        colorpath = self.projectdirectory + 'mycolor.pkl'
        if os.path.isfile(colorpath):
            with open(colorpath, 'rb') as f:
                self.lccolors = pickle.load(f)
                f.close()
        else:
            self.lccolors = copy.deepcopy(colors)
        self.lc_cm = make_cmap(self.lccolors, bit=True)
        self.areacolors = [(102, 51, 0)]
        self.area_cm = make_cmap(self.areacolors)
        self.boolean_colors = [(0, 0, 255), (255, 0, 0)]
        self.boolean_cm = make_cmap(self.boolean_colors)
        self.fire_cm = make_cmap([(102, 255, 255), (255, 0, 0)], bit=False)
        self.soil_cm = make_cmap(
                [(204, 102, 0), (168, 84, 0), (136, 68, 0), (100, 50, 0), (64, 32, 0)], bit=False)

    def row_clicked(self, index):
        self.activeIndex = index
        activeNode = index.internalPointer()
        if len(activeNode.children()) == 0:
            data = activeNode.data()['Path']
            name = activeNode.name
            print name
            self.MapsDisplay(data)

            # if activeNode.data():
            #     filename = str(index.internalPointer().value())
            #     typename = index.internalPointer().name()
            #     ptypename = index.internalPointer().parent().name()
            #     if os.path.isfile(filename):
            #         self.MapsDisplay(filename, typename, ptypename)
            #     else:
            #         message = QtGui.QMessageBox(self)
            #         yesbtn = message.addButton(QtGui.QMessageBox.Yes)
            #         message.setWindowTitle("Your file path is not valid")
            #         message.setText("Would you like to choose another files")
            #         QtCore.QObject.connect(yesbtn, QtCore.SIGNAL("clicked()"), self.on_Open_Clicked)
            #         message.addButton(QtGui.QMessageBox.No)
            #         message.show()
            # else:
            #     if (self.activeIndex.internalPointer().childCount() == 0):
            #         message = QtGui.QMessageBox(self)
            #         yesbtn = message.addButton(QtGui.QMessageBox.Yes)
            #         message.setWindowTitle("No file selected")
            #         message.setText("Would you like to choose a map file")
            #         QtCore.QObject.connect(yesbtn, QtCore.SIGNAL("clicked()"), self.on_Open_Clicked)
            #         message.addButton(QtGui.QMessageBox.No)
            #         message.show()

    def on_Open_Clicked(self):
        if (self.activeIndex and
                len(self.activeIndex.internalPointer().children()) == 0):
            filename = str(QtGui.QFileDialog.getOpenFileName(filter=filters, directory=self.preferdirectory))
            # self.preferdirectory = os.path.dirname(filename)
            # node = self.activeIndex.internalPointer()
            # typename = self.activeIndex.internalPointer().name()
            # ptypename = self.activeIndex.internalPointer().parent().name()
            # node.setValue(filename)
            self.MapsDisplay(filename)

    def on_Save_Clicked(self):
        self.Save()

    def on_Compare_Clicked(self):
        print("Compare")

    def create_Plot_Frame(self):
        self.main_frame = self.MapInputWidget
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
        vbox.addWidget(self.canvas)  # the matplotlib canvas
        vbox.addWidget(self.mpl_toolbar)
        self.main_frame.setLayout(vbox)

    def MapsDisplay(self, filename, typemap=None, ptypename = None):
        if filename:
            ds = gdal.Open(filename)
            band = ds.GetRasterBand(1)
            elevation = band.ReadAsArray()
            self.elevationm= numpy.ma.masked_where(elevation<=-9999,elevation)
            self.fig.clear()
            self.axes = self.fig.add_subplot(111)
            #print typemap
            if typemap == 'area':
                cm = self.area_cm
                i = self.axes.imshow(self.elevationm, cmap=cms.get_cmap(cm), vmin=1, vmax=1,
                                     interpolation='nearest', aspect='equal')
                self.fig.colorbar(i, ticks=[1])
            elif typemap == 'initlc':
                cm = self.lc_cm
                i = self.axes.imshow(self.elevationm, cmap=cms.get_cmap(cm), vmin=0, vmax=40,
                                     interpolation='nearest', aspect='equal')
                v = [j for j in range(0, 41)]
                self.fig.colorbar(i, ticks=v)
            elif typemap in ['soilfert', 'initsoilfert', 'maxsoilfert']:
                cm = self.soil_cm
                i = self.axes.imshow(self.elevationm, cmap=cms.get_cmap(cm), vmin=1, vmax=5,
                                     interpolation='nearest', aspect='equal')
                v = [j for j in range(1, 6)]
                self.fig.colorbar(i, ticks=v)
            elif typemap in ['subcat', 'initlog', 'reserve', 'disaster', 'suitability'] or ptypename=='suitability':
                cm = self.boolean_cm
                i = self.axes.imshow(self.elevationm, cmap=cms.get_cmap(cm), vmin=0, vmax=1,
                                     interpolation='nearest', aspect='equal')
                self.fig.colorbar(i, ticks=[0, 1])
            else:
                i = self.axes.imshow(self.elevationm, interpolation='nearest', aspect='equal')
                self.fig.colorbar(i)
            self.canvas.draw()
            self.canvas.mpl_connect('button_press_event', self.onclick)
            #self.axes.format_coord = self.format_coord

    def on_key_press(self, event):
        key_press_handler(event, self.canvas, self.mpl_toolbar)

    def onclick(self, event):
        if (event.button == 2):
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

    def Save(self):
        with open(self.fileName, 'wb') as input:
            MapParameter = [int(self.pixelsize_lineedit.text()),self.MapInputNode]
            #pickle.dump(self.MapInputNode, input)
            pickle.dump(MapParameter,input)
            input.close()

    def format_coord(self,xdata,ydata):
        try:
                float(self.elevationm[ydata][xdata])
                abc = 'x=%.3f, y=%.3f ' % (
                    xdata, ydata)
        except:
            abc = 'x=%.3f, y=%.3f, value = nv' % (
                    xdata, ydata)
        return abc

    def closeEvent(self,event):
        reply=QtGui.QMessageBox.question(self,'Message',"Do you want to save your input before quitting?",QtGui.QMessageBox.Yes,QtGui.QMessageBox.No,QtGui.QMessageBox.Cancel)
        if reply==QtGui.QMessageBox.Yes:
            self.Save()
            #self.mapinput_closing.emit()
            event.accept()
        elif reply==QtGui.QMessageBox.Cancel:
            event.ignore()
        else:
            #self.mapinput_closing.emit()
            event.accept()
def main():
    app = QtGui.QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()
if __name__ == '__main__':
    main()
