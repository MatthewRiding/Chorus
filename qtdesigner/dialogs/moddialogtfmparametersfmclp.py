from PySide6.QtWidgets import QDialog, QDialogButtonBox

from qtdesigner.dialogs.UI_dialog_tfm_parameters_fmclp import Ui_dialog_tfm_parameters_fmclp
from classdefs.modtfmparams import TFMParams
from corevariables.modwavesets import dict_wave_sets
from corevariables.modmaskbehaviours import dict_mask_behaviours
from corevariables.modpresetmaskangles import dict_mask_angles


class DialogTFMParamsFMCLP(QDialog, Ui_dialog_tfm_parameters_fmclp):
    def __init__(self, parent=None, tfm_params_previous=None):
        super().__init__(parent)

        self.setupUi(self)

        # Pre-define instance variables:
        self.tfm_params = None

        # Modify text on accept button:
        self.buttonBox.button(QDialogButtonBox.Ok).setText('Run TFM')
        # Set the accept button to disabled by default:
        # self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)

        # Add wave set strings to combo box from reference dict:
        for wave_set_string in dict_wave_sets.keys():
            self.comboBox_wave_set.addItem(wave_set_string)

        # Add pre-set mask angles to combo box from reference dict:
        for pre_set_mask_angle in dict_mask_angles.keys():
            self.comboBox_mask_angle.addItem(pre_set_mask_angle)

        # Add mask behaviours to combo box from reference dict:
        for mask_behaviour in dict_mask_behaviours.keys():
            self.comboBox_mask_behaviour.addItem(mask_behaviour)

        if tfm_params_previous:
            # Display the previous set of tfm params input by the user:
            self.set_tfm_params_in_input_widgets(tfm_params_previous)

        # Update the angle value to reflect the default choice of pre-set angle:
        default_preset_angle = self.comboBox_mask_angle.currentText()
        self.combobox_mask_angle_text_changed(default_preset_angle)

        # Wire signals to slots:
        self.buttonBox.accepted.connect(self.accept_button_clicked)
        self.comboBox_mask_angle.currentTextChanged.connect(self.combobox_mask_angle_text_changed)
        self.doubleSpinBox_v_T_ms.editingFinished.connect(self.speed_value_changed)
        self.doubleSpinBox_v_L_ms.editingFinished.connect(self.speed_value_changed)

    def accept_button_clicked(self):
        # The user has submitted TFM parameters and wishes to proceed to TFM.
        # Collect the TFM parameters from the input widgets into the tfm_params instance variable:
        self.tfm_params = TFMParams(image_name_string=self.line_edit_description.text(),
                                    pitch_mm=self.doubleSpinBox_pitch_mm.value(),
                                    v_l_mpers=self.doubleSpinBox_v_L_ms.value(),
                                    v_t_mpers=self.doubleSpinBox_v_T_ms.value(),
                                    wave_set_string=self.comboBox_wave_set.currentText(),
                                    grid_size_x_mm=self.doubleSpinBox_grid_size_x_mm.value(),
                                    grid_size_z_mm=self.doubleSpinBox_grid_size_z_mm.value(),
                                    n_pixels_z=self.spinBox_n_pixels_z.value(),
                                    filter_tf=self.groupBox_filter.isChecked(),
                                    butter_order=self.spinBox_butter_order.value(),
                                    band_min_MHz=self.doubleSpinBox_band_min_MHz.value(),
                                    band_max_MHz=self.doubleSpinBox_band_max_MHz.value(),
                                    gen_mask_tf=self.groupBox_gen_mask.isChecked(),
                                    mask_angle_deg=self.doubleSpinBox_mask_angle.value(),
                                    mask_behaviour_string=self.comboBox_mask_behaviour.currentText())
        # The tfm_params instance variable will be accessible from the DialogTFMParams instance wherever it is created.

    def set_tfm_params_in_input_widgets(self, tfm_params):
        self.doubleSpinBox_pitch_mm.setValue(tfm_params.pitch_mm)
        self.doubleSpinBox_v_L_ms.setValue(tfm_params.v_l_mpers)
        self.doubleSpinBox_v_T_ms.setValue(tfm_params.v_t_mpers)
        index = self.comboBox_wave_set.findText(tfm_params.wave_set_string)
        if index >= 0:
            self.comboBox_wave_set.setCurrentIndex(index)
        self.doubleSpinBox_grid_size_x_mm.setValue(tfm_params.grid_size_x_mm)
        self.doubleSpinBox_grid_size_z_mm.setValue(tfm_params.grid_size_z_mm)
        self.spinBox_n_pixels_z.setValue(tfm_params.n_pixels_z)
        self.groupBox_filter.setChecked(tfm_params.filter_tf)
        self.spinBox_butter_order.setValue(tfm_params.butter_order)
        self.doubleSpinBox_band_min_MHz.setValue(tfm_params.band_min_MHz)
        self.doubleSpinBox_band_max_MHz.setValue(tfm_params.band_max_MHz)
        self.groupBox_gen_mask.setChecked(tfm_params.gen_mask_tf)
        self.doubleSpinBox_mask_angle.setValue(tfm_params.mask_angle_deg)
        index = self.comboBox_mask_behaviour.findText(tfm_params.mask_behaviour_string)
        if index >= 0:
            self.comboBox_mask_behaviour.setCurrentIndex(index)

    def combobox_mask_angle_text_changed(self, mask_angle_choice):
        angle_calculation_function = dict_mask_angles[mask_angle_choice]
        if angle_calculation_function:
            # Make the mask angle doubleSpinBox read-only:
            self.doubleSpinBox_mask_angle.setReadOnly(True)
            # Calculate the chosen mask angle:
            mask_angle = angle_calculation_function(v_l_mpers=self.doubleSpinBox_v_L_ms.value(),
                                                    v_t_mpers=self.doubleSpinBox_v_T_ms.value())
            # Write the mask angle value to the DoubleSpinBox:
            self.doubleSpinBox_mask_angle.setValue(mask_angle)
        else:
            # The user has selected the 'manual entry' option (which has no associated angle generation function):
            # Make the mask angle doubleSpinBox editable:
            self.doubleSpinBox_mask_angle.setReadOnly(False)

    def speed_value_changed(self):
        # The user has changed the value of either v_T or v_L.  This changes the value of the critical angle, so:
        mask_angle_choice = self.comboBox_mask_angle.currentText()
        if mask_angle_choice == 'Critical angle':
            angle_calculation_function = dict_mask_angles[mask_angle_choice]
            # Calculate the angle, no matter what the user has asked for:
            mask_angle = angle_calculation_function(v_l_mpers=self.doubleSpinBox_v_L_ms.value(),
                                                    v_t_mpers=self.doubleSpinBox_v_T_ms.value())
            # Write the critical angle value to the DoubleSpinBox:
            self.doubleSpinBox_mask_angle.setValue(mask_angle)
