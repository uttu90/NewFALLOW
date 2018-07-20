from PyQt5 import QtWidgets
import project_diaglog_ui


class ProjectDiaglog( QtWidgets.QDialog, project_diaglog_ui.Ui_Dialog ):
    def __init__(self, parent=None, title='', button_title=''):
        super(ProjectDiaglog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(title)
        self.button.setText(button_title)

        self.value = ''

        self.button.clicked.connect(self.choose_folder)

    def choose_folder(self):
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(
            self,
            'Select project folder',
            self.lineEdit.text(),
            QtWidgets.QFileDialog.ShowDirsOnly
        )

        if folder_path:
            self.lineEdit.setText(folder_path)

    def accept(self):
        self.value = str(self.lineEdit.text())
        super(ProjectDiaglog, self).accept()
        # self.result()

    def return_value(self):
        return self.value