from FALLOW import projectManager

from PyQt4 import QtCore, QtGui
import ListProjectUI

input_para_extension = "Excel Files (*.xls)"
model_file_extension = "Python Files (*.py)"


class ListProject(QtGui.QDialog, ListProjectUI.Ui_Dialog):
    def __init__(self, parent=None, project_path="C:/"):
        super(ListProject, self).__init__(parent)
        self.setupUi(self)
        self._load_project()
        self.select_project = None

    def _load_project(self, file_name='projects.json'):
        projects = projectManager.get_projects(file_name)
        for key in projects.keys():
            prj = key + ': ' + projects[key]
            self.listProject.addItem(prj)
        self.listProject.itemClicked.connect(self._selected_item)

    def _selected_item(self, item):
        self.select_project = item.text()

    def return_value(self):
        return self.select_project


def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    form = ListProject()
    form.show()
    app.exec_()
    x = form.return_value()
    print x
    del form

if __name__ == '__main__':
    main()