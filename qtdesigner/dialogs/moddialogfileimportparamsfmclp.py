from PySide6.QtWidgets import QDialog, QFileDialog
from PySide6.QtGui import QIcon
import pathlib

from qtdesigner.dialogs.UI_dialog_import_fmclp import Ui_dialog_import_fmclp


class DialogImportFMCLP(QDialog, Ui_dialog_import_fmclp):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)

        # Pre-define instance variables:
        self.parent_main_window = parent
        self.description_string = None
        self.file_path = None
        self.file_extension = None
        self.t_min_us = None
        self.t_max_us = None
        self.conversion_factor_to_nm = None

        # Display folder icon on browse button:
        self.push_button_browse_for_file.setIcon(QIcon('graphicfiles/browse_folder.png'))

        # Wire signals to slots:
        self.push_button_browse_for_file.clicked.connect(self.browse_for_file)
        self.buttonBox.accepted.connect(self.accept_button_clicked)

    def browse_for_file(self):
        # Open a QFileDialog to get the path to the fmc file:
        # Permitted formats are: .mat, .npy, and .txt
        file_path, file_filter = QFileDialog.getOpenFileName(parent=self.parent_main_window,
                                                             filter='All compatible files (*.mat *.npy *.txt);;'
                                                                    'mat file (*.mat);;'
                                                                    'NumPy file (*.npy);;'
                                                                    'text file (*.txt)')
        # After closure of the file dialog, display the file path in the line edit:
        self.lineEdit_file_path.setText(file_path)

    def accept_button_clicked(self):
        # Take the description, file path and time limits entered by the user and save them to the instance as
        # instance variables:
        self.description_string = self.line_edit_description.text()
        self.file_path = self.lineEdit_file_path.text()
        # Get the file extension from the path string:
        self.file_extension = pathlib.Path(self.file_path).suffix
        self.t_min_us = self.doubleSpinBox_time_min_us.value()
        self.t_max_us = self.doubleSpinBox_time_max_us.value()
        # If the associated checkbox is ticked, save the specified conversion factor:
        if self.groupBox_convert_to_nm.isChecked():
            self.conversion_factor_to_nm = self.doubleSpinBox_conversion_factor_to_nm.value()
