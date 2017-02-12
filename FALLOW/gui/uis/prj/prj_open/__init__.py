import sys
import os
import ConfigParser
from shutil import copy2

from PyQt4 import QtCore, QtGui
import OpenProjectUI

input_para_extension = "Excel Files (*.xls)"
model_file_extension = "Python Files (*.py)"


class OpenProject(QtGui.QDialog, OpenProjectUI.Ui_openprj):
    def __init__(self, parent=None, project_path="C:/"):
        super(OpenProject, self).__init__(parent)
        self.setupUi(self)
        self.project_path = project_path
        self.connect(self.btnopenprj,
                     QtCore.SIGNAL("clicked()"),
                     self.browse_project)
        self.value = None
        # self.lineprjdirectory.setText(project_path)
        # self.connect(self.btnprjdirectory,

        #              QtCore.SIGNAL("clicked()"),
        #              self.browse_project)
        # self.connect(self.btninputpara,
        #              QtCore.SIGNAL("clicked()"),
        #              self.browse_input_file)
        # self.connect(self.btnmodelfile,
        #              QtCore.SIGNAL("clicked()"),
        #              self.browse_model_file)
        # self.ready = True
        # self.config = ConfigParser.RawConfigParser()

    def _raise_message(self, header, message):
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Information)
        msg.setText(header)
        msg.setInformativeText(message)
        msg.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
        msg.show()
        msg.exec_()

    def browse_project(self):
        project = QtGui.QFileDialog.getExistingDirectory(
            self, 'Select a folder:', self.lineopenprj.text(),
            QtGui.QFileDialog.ShowDirsOnly)
        if project:
            self.lineopenprj.setText(project)

    def accept(self):
        self.value = str(self.lineopenprj.text())
        super(OpenProject, self).accept()

    def return_value(self):
        return self.value


def main():
    app = QtGui.QApplication(sys.argv)
    form = OpenProject()
    form.show()
    app.exec_()
    del form


if __name__ == '__main__':
    main()
