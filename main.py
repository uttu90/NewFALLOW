import sys
from PyQt4 import QtCore, QtGui

from FALLOW.gui.uis import mainwindow

app = QtGui.QApplication(sys.argv)
form = mainwindow.MainWindow()
form.show()
app.exec_()
del form