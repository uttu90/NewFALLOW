import sys
from PyQt5 import QtWidgets

from FALLOW.gui.uis import mainwindow

window = QtWidgets.QApplication(sys.argv)
app = mainwindow.App()
app.show()
window.exec_()
del app