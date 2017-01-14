from PyQt4 import QtGui
from PyQt4 import QtCore
import sys
import TimeInputUI
from FALLOW.models import TimeInput
from FALLOW.models.utils.Tree import Tree
from FALLOW.models.utils import TableModel
import os
import pickle
import warnings
warnings.simplefilter(action="ignore", category=UserWarning)
from matplotlib.figure import Figure
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from matplotlib.backends import qt4_compat
use_pyside = qt4_compat.QT_API == qt4_compat.QT_API_PYSIDE


class MainWindow(QtGui.QMainWindow, TimeInputUI.Ui_MainWindow):
    def __init__(self, parent=None, filename='TimeSeries.pkl', directory="C:"):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.projectdirectory = directory
        self.inputdirectory = directory + "\\Input\\"
        self.outputdirectory = directory + "\\Output\\"
        self.create_Plot_Frame()
        QtCore.QObject.connect(self.TSInputTreeview, QtCore.SIGNAL("clicked (QModelIndex)"), self.row_clicked)
        self.connect(self.action_Save, QtCore.SIGNAL("triggered()"), self.on_Save_Clicked)
        self.filename = filename
        if filename == 'TimeSeries.pkl':
            self.fileName = self.inputdirectory + 'TimeSeries.pkl'
            if (os.path.isfile(self.fileName)):
                with open(self.fileName, 'rb') as output:
                    TimeParameter = pickle.load(output)
                    self.timesimulation = TimeParameter[0]
                    self.TimeSeriesNode = TimeParameter[1]
                    self.usingtimeseries = TimeParameter[2]
                    output.close()
            else:
                self.TimeSeriesNode = TimeInput.TimeSeries
                self.timesimulation = 30
                self.usingtimeseries= 1
            self.usingts_chk.setChecked(self.usingtimeseries)
            self.simulationtime_lineedit.setText(str(self.timesimulation))
            self.TStreeModel = Tree(self.TimeSeriesNode)
            self.TSInputTreeview.setModel(self.TStreeModel)
            #print self.TimeSeriesNode._typeinfo
            #print self.TimeSeriesNode._headerdata
            self.activeIndex = None
        elif filename == 'OutputTimeSeries.pkl':
            self.fileName = self.outputdirectory + 'OutputTimeSeries.pkl'
            with open(self.fileName, 'rb') as output:
                self.OutputTimeseires = pickle.load(output)
                self.TStreeModel = Tree(self.OutputTimeseires)
                self.TSInputTreeview.setModel(self.TStreeModel)

    def row_clicked(self, index):
        self.activeIndex = index
        if self.activeIndex.internalPointer().childCount() == 0:
            array = self.activeIndex.internalPointer().value()
            self.TSModel = TableModel.TimeSeriesModel(array)
            self.TSModel.datachange.connect(self.on_datachange)
            self.TSInputTableview.setModel(self.TSModel)
            self.plot(array)

    def plot(self, array):
        self.fig.clear()
        self.axes = self.fig.add_subplot(111)
        self.axes.plot(array)

    def create_Plot_Frame(self):
        self.main_frame = self.TSInputDiagram
        self.fig = Figure((7.0, 7.0), dpi=80)
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

    def on_key_press(self, event):
        key_press_handler(event, self.canvas, self.mpl_toolbar)

    def on_Save_Clicked(self):
        self.Save()
        #print("Save complete")

    def plot(self,array):
        self.fig.clear()
        self.axes = self.fig.add_subplot(111)
        self.axes.set_xlim(0, len(array)-1)
        self.axes.set_ylim(0, max(array)*1.1)
        self.axes.set_autoscale_on(False)
        self.axes.plot(array, linestyle='steps-post')
        self.axes.set_xlabel('year')
        self.canvas.draw()

    def Save(self):
        with open(self.fileName, 'wb') as input:
            #pickle.dump(self.TimeSeriesNode, input)
            TimeParameter = [int(self.simulationtime_lineedit.text()),self.TimeSeriesNode,self.usingts_chk.checkState()]
            pickle.dump(TimeParameter,input)
            input.close()

    @QtCore.pyqtSlot()
    def on_datachange(self):
        array = self.activeIndex.internalPointer().value()
        self.TSModel = TableModel.TimeSeriesModel(array)
        self.TSModel.datachange.connect(self.on_datachange)
        self.TSInputTableview.setModel(self.TSModel)
        self.plot(array)

    def closeEvent(self,event):
        reply = QtGui.QMessageBox.question(self,'Message',"Do you want to save your input before quitting?",QtGui.QMessageBox.Yes,QtGui.QMessageBox.No,QtGui.QMessageBox.Cancel)
        if reply == QtGui.QMessageBox.Yes:
            self.Save()
            # self.time_closing.emit()
            event.accept()
        elif reply == QtGui.QMessageBox.Cancel:
            event.ignore()
        else:
            # self.time_closing.emit()
            event.accept()


def main():
    app = QtGui.QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()
if __name__ == '__main__':
    main()
