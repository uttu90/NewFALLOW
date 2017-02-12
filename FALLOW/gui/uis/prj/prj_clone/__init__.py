import sys
import os
import ConfigParser
from shutil import copytree

from PyQt4 import QtCore, QtGui
import CloneProjectUI

input_para_extension = "Excel Files (*.xls)"
model_file_extension = "Python Files (*.py)"


class CloneProject(QtGui.QDialog, CloneProjectUI.Ui_diagcloneprj):
    def __init__(self, parent=None, project_path="C:/"):
        super(CloneProject, self).__init__(parent)
        self.setupUi(self)
        self.project_path = project_path
        self.connect(self.btnoriginalprj,
                     QtCore.SIGNAL("clicked()"),
                     self.browse_original_project)
        self.connect(self.btndestinationprj,
                     QtCore.SIGNAL("clicked()"),
                     self.browse_destination_project)
        self.ready = True
        self.value = None

    def _raise_message(self, header, message):
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Information)
        msg.setText(header)
        msg.setInformativeText(message)
        msg.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
        msg.show()
        msg.exec_()

    def _check_blank(self, line_edit, text):
        if not line_edit.text():
            header = "%s information should be filled" % text
            message = "Please fill the information to " \
                      "%s" % text
            self.ready = False
            self._raise_message(header, message)

    def browse_original_project(self):
        self._browse_project(self.lineoriginalprj)

    def browse_destination_project(self):
        self._browse_project(self.linedestinationprj)

    def _browse_project(self, line_edit):
        project = QtGui.QFileDialog.getExistingDirectory(
            self, 'Select a folder:', self.project_path,
            QtGui.QFileDialog.ShowDirsOnly)
        if project:
            line_edit.setText(project)

    def _prepare_frame(self):
        if not os.path.isdir(str(self.linedestinationprj.text())):
            os.mkdir(str(self.linedestinationprj.text()))
        # copytree(str(self.lineoriginalprj.text()),
        #          str(self.linedestinationprj.text()))

    def accept(self):
        self._check_blank(self.lineoriginalprj, 'original project')
        self._check_blank(self.linedestinationprj, 'destination project')
        self._check_blank(self.linemodelername, 'modeler name')
        self._check_blank(self.linemodeleremail, 'modeler email')

        if self.ready:
            self._prepare_frame()
            self.value = str(self.linedestinationprj.text())
            super(CloneProject, self).accept()
        else:
            self.ready = True

    def return_value(self):
        return self.value

def main():
    app = QtGui.QApplication(sys.argv)
    form = CloneProject()
    form.show()
    app.exec_()
    del form


if __name__ == '__main__':
    main()