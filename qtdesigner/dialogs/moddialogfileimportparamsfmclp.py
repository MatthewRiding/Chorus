from PySide6.QtWidgets import QDialog, QFileDialog
from PySide6.QtGui import QIcon

from qtdesigner.dialogs.UI_dialog_import_fmclp_mat import Ui_dialog_tfm_parameters_fmclp


class DialogImportFMCLPmat(QDialog, Ui_dialog_tfm_parameters_fmclp):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)

        # Pre-define instance variables:
        self.parent_main_window = parent
        self.description_string = None
        self.file_path = None
        self.t_min_us = None
        self.t_max_us = None

        # Display folder icon on browse button:
        self.push_button_browse_for_file.setIcon(QIcon('graphicfiles/browse_folder.png'))

        # Wire signals to slots:
        self.push_button_browse_for_file.clicked.connect(self.browse_for_file)
        self.buttonBox.accepted.connect(self.accept_button_clicked)

    def browse_for_file(self):
        # Open a QFileDialog to get the path to the .mat file:
        file_path, file_filter = QFileDialog.getOpenFileName(parent=self.parent_main_window, filter='mat files (*.mat)')

        # After closure of the file dialog, display the file path in the line edit:
        self.lineEdit_file_path.setText(file_path)

    def accept_button_clicked(self):
        # Take the description, file path and time limits entered by the user and save them to the instance as
        # instance variables:
        self.description_string = self.line_edit_description.text()
        self.file_path = self.lineEdit_file_path.text()
        self.t_min_us = self.doubleSpinBox_time_min_us.value()
        self.t_max_us = self.doubleSpinBox_time_max_us.value()
