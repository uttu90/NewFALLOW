from PyQt4 import QtGui, QtCore, uic
import sys
from numpy import *


class TimeSeriesModel(QtCore.QAbstractTableModel):
    datachange = QtCore.pyqtSignal()
    def __init__(self, ts, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._array = ts

    def rowCount(self, parent):
        return len(self._array)

    def columnCount(self, parent):
        return 1

    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def data(self, index, role):
        row = index.row()
        if role == QtCore.Qt.DisplayRole:
            return str(self._array[row])
        elif role == QtCore.Qt.EditRole:
            return str(self._array[row])

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if role == QtCore.Qt.EditRole:
            row = index.row()
            column = index.column()
            print(row, column)
            value = value.toString()
            print(value)
            if column == 0:
                try:
                    value = float(value)
                    self._array[row] = value
                    self.datachange.emit()
                    return True
                except ValueError:
                    self._array[row] = 0
                    self.datachange.emit()
                    return True
        return False

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return "Value"
            else:
                return str(section) + "  "


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setStyle("plastique")
    a = zeros(100)
    @QtCore.pyqtSlot()
    def on_datachange():
        print("Hello")
    tableView = QtGui.QTableView()
    tableView.show()
    model = TimeSeriesModel(a)
    model.datachange.connect(on_datachange)
    tableView.setModel(model)
    sys.exit(app.exec_())
