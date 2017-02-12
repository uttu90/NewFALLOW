import sys
import os
import ConfigParser
from shutil import copy2

from PyQt4 import QtCore, QtGui
import NewProjectUI

import json


input_para_extension = "Excel Files (*.xls)"
model_file_extension = "Python Files (*.py)"


class NewProject(QtGui.QDialog, NewProjectUI.Ui_diagnewprj):
    def __init__(self, parent=None, project_path="C:/"):
        super(NewProject, self).__init__(parent)
        self.setupUi(self)
        self.project_path = project_path
        self.lineprjdirectory.setText(project_path)
        self.connect(self.btnprjdirectory,
                     QtCore.SIGNAL("clicked()"),
                     self.browse_project)
        self.connect(self.btninputpara,
                     QtCore.SIGNAL("clicked()"),
                     self.browse_input_file)
        self.connect(self.btnmodelfile,
                     QtCore.SIGNAL("clicked()"),
                     self.browse_model_file)
        self.ready = True
        self.config = ConfigParser.RawConfigParser()
        self.value = None

    def _raise_message(self, header, message):
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Information)
        msg.setText(header)
        msg.setInformativeText(message)
        msg.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
        # msg.exec_()
        msg.show()
        msg.exec_()

    def _check_blank(self, line_edit, text):
        if not line_edit.text():
            header = "%s information should be filled" % text
            message = "Please fill the information to " \
                      "%s" % text
            self.ready = False
            self._raise_message(header, message)

    def browse_project(self):
        project = QtGui.QFileDialog.getExistingDirectory(
            self, 'Select a folder:', self.lineprjdirectory.text(),
            QtGui.QFileDialog.ShowDirsOnly)
        if project:
            self.lineprjdirectory.setText(project)

    def _browse_file(self, message='Open file', filters=None, line_edit=None):
        filename = QtGui.QFileDialog.getOpenFileName(
            self, message, self.project_path , filters)
        line_edit.setText(filename)

    def browse_input_file(self):
        self._browse_file(message='Open input parameter file',
                          filters=input_para_extension,
                          line_edit=self.lineinputpara)

    def browse_model_file(self):
        self._browse_file(message='Open model file',
                          filters=model_file_extension,
                          line_edit=self.linemodelfile)

    def _create_config_file(self):
        prj_directory = self.lineprjdirectory.text()
        if not os.path.isdir(prj_directory):
            os.mkdir(prj_directory)
        config_path = os.path.join(str(prj_directory), 'project.cfg')
        try:
            self.config.add_section('project')
        except ConfigParser.DuplicateSectionError:
            pass
        self.config.set('project', 'directory', prj_directory)
        self.config.set('project', 'modeler name',
                        self.linemodelername.text())
        self.config.set('project', 'modeler email',
                        self.linemodeleremail.text())
        # self.config.set('project', 'input parameter',
        #                 self.lineinputpara.text())
        # self.config.set('project', 'model file',
        #                 self.linemodelfile.text())
        with open(config_path, 'wb') as configfile:
            self.config.write(configfile)

    def _prepare_frame(self):
        input_file = os.path.join(str(self.lineprjdirectory.text()),
                                  'input_parameters.xls')
        model_file = os.path.join(str(self.lineprjdirectory.text()),
                                  'model_file.py')
        copy2(str(self.lineinputpara.text()), input_file)
        copy2(str(self.linemodelfile.text()), model_file)
        self.config.set('project', 'input parameter', input_file)
        self.config.set('project', 'model file', model_file)
        input_dir = os.path.join(str(self.lineprjdirectory.text()), 'Input')
        output_dir = os.path.join(str(self.lineprjdirectory.text()), 'Output')
        try:
            os.mkdir(input_dir)
            os.mkdir(output_dir)
        except WindowsError:
            pass

    def accept(self):
        self._check_blank(self.lineprjdirectory, 'project path')
        self._check_blank(self.linemodelername, 'modeler name')
        self._check_blank(self.linemodeleremail, 'modeler email')
        self._check_blank(self.lineinputpara, 'input parameter file')
        self._check_blank(self.linemodelfile, 'model file')

        if self.ready:
            self._create_config_file()
            self._prepare_frame()
            if not os.path.isfile('projects.josn'):
                projects = {}
            else:
                with open('projects.json', 'r') as file:
                    projects = json.load(file)
            abs_path = str(self.lineprjdirectory.text())
            projects[os.path.basename(abs_path)] = abs_path
            with open('projects.json', 'w') as file:
                json.dump(projects, file)
            self.value = str(self.lineprjdirectory.text())
            super(NewProject, self).accept()
        else:
            self.ready = True

    def return_value(self):
        return self.value


def main():
    app = QtGui.QApplication(sys.argv)
    form = NewProject()
    form.show()
    app.exec_()
    del form

if __name__ == '__main__':
    main()
