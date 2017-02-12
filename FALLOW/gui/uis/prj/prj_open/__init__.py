import sys
import os
import ConfigParser
from shutil import copy2

from PyQt4 import QtCore, QtGui
import OpenProjectUI
from FALLOW.gui.uis.prj import prj_list
from FALLOW import projectManager

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
        self.connect(self.btnlistprj,
                     QtCore.SIGNAL("clicked()"),
                     self.list_projects)
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
            projects = projectManager.get_projects()
            project = str(project)
            projects[os.path.basename(project)] = os.path.abspath(project)
            projectManager.put_projects(projects)

    def list_projects(self):
        list_project = prj_list.ListProject(self)
        list_project.show()
        if list_project.exec_():
            value = list_project.return_value()
            if value:
                self.project_path = str(value).split(": ")
                self.lineopenprj.setText(self.project_path[1])

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
