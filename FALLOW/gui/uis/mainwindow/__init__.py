import sys
from PyQt5 import QtWidgets, QtCore

import MainWindowUI


class App(QtWidgets.QMainWindow, MainWindowUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setupUi(self)
        self.showMaximized()

        self.path = ''

        self.openProject.triggered.connect(self.open_project)

    def open_project(self):
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(
            self,
            'Select project folder',
            self.path,
            QtWidgets.QFileDialog.ShowDirsOnly
        )

        if folder_path:
            self.path = folder_path
            self.setWindowTitle(self.windowTitle() + ' - ' + folder_path)






if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = App()
    form.show()
    app.exec_()
    del form