from PySide6.QtWidgets import QDialog, QDialogButtonBox

from qtdesigner.dialogs.UI_dialog_tfm_parameters_fmclp import Ui_dialog_tfm_parameters_fmclp
from corevariables.modwavetypes import (dict_wave_types_send, dict_wave_types_receive)
from corevariables.modmaskbehaviours import dict_mask_behaviours
from corevariables.modpresetmaskangles import dict_mask_angles
from classdefs.modtfmgridpreviewwidget import TFMGridPreviewWidget
from classdefs.modtfmconstructor import TFMConstructor
from classdefs.modmaterial import Material
from classdefs.modfilterspec import FilterSpec
from classdefs.modmaskspec import MaskSpec


class DialogTFMParamsFMCLP(QDialog, Ui_dialog_tfm_parameters_fmclp):
    def __init__(self, n_elements, parent=None, tfm_constructor_previous=None):
        super().__init__(parent)

        self.setupUi(self)

        # Pre-define instance variables:
        self.n_elements = n_elements
        self.tfm_constructor = tfm_constructor_previous

        # Modify text on accept button:
        self.buttonBox.button(QDialogButtonBox.Ok).setText('Run TFM')
        # Set the accept button to disabled by default:
        # self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)

        # Add wave type strings to combo boxes from reference dicts:
        # Send types:
        for wave_type_string in dict_wave_types_send.keys():
            self.comboBox_send.addItem(wave_type_string)
        # Receive types:
        for wave_type_string in dict_wave_types_receive.keys():
            self.comboBox_receive.addItem(wave_type_string)

        # Add pre-set mask angles to combo box from reference dict:
        for pre_set_mask_angle in dict_mask_angles.keys():
            self.comboBox_mask_angle_gen.addItem(pre_set_mask_angle)
            self.comboBox_mask_angle_det.addItem(pre_set_mask_angle)

        # Add mask behaviours to combo box from reference dict:
        for mask_behaviour in dict_mask_behaviours.keys():
            self.comboBox_mask_behaviour_gen.addItem(mask_behaviour)
            self.comboBox_mask_behaviour_det.addItem(mask_behaviour)

        if tfm_constructor_previous:
            # Display the previous set of tfm params input by the user:
            self.set_tfm_params_in_input_widgets(tfm_constructor_previous)

        # Update the angle value to reflect the default choice of pre-set angle:
        default_preset_angle_gen = self.comboBox_mask_angle_gen.currentText()
        self.combobox_mask_angle_gen_text_changed(default_preset_angle_gen)
        default_preset_angle_det = self.comboBox_mask_angle_det.currentText()
        self.combobox_mask_angle_det_text_changed(default_preset_angle_det)

        # Add an instance of the TFMGridPreviewWidget to the main horizontal layout:
        self.grid_preview_widget = TFMGridPreviewWidget(n_elements,
                                                        self.doubleSpinBox_grid_size_x_mm.value(),
                                                        self.doubleSpinBox_grid_size_z_mm.value(),
                                                        self.spinBox_n_pixels_z.value())
        self.h_layout_main.addWidget(self.grid_preview_widget)

        # Set the maximum bandpass filter frequency to be frequency_sampling / 2:

        # Wire signals to slots:
        self.buttonBox.accepted.connect(self.accept_button_clicked)
        self.doubleSpinBox_pitch_mm.editingFinished.connect(self.update_array)
        self.doubleSpinBox_grid_size_x_mm.editingFinished.connect(self.update_grid)
        self.doubleSpinBox_grid_size_z_mm.editingFinished.connect(self.update_grid)
        self.spinBox_n_pixels_z.editingFinished.connect(self.update_grid)
        self.comboBox_mask_angle_gen.currentTextChanged.connect(self.combobox_mask_angle_gen_text_changed)
        self.doubleSpinBox_c_l_mpers.editingFinished.connect(self.speed_value_changed)
        self.doubleSpinBox_c_t_mpers.editingFinished.connect(self.speed_value_changed)

    def accept_button_clicked(self):
        # The user has submitted TFM parameters and wishes to proceed to TFM.

        # Build Material class instance:
        material = Material(self.doubleSpinBox_c_l_mpers.value(),
                            self.doubleSpinBox_c_t_mpers.value(),
                            self.doubleSpinBox_c_lsaw_mpers.value())

        # Build FilterSpec instance if requested:
        if self.groupBox_filter.isChecked():
            # A filter has been requested.
            filter_spec = FilterSpec(self.spinBox_butter_order.value(),
                                     self.doubleSpinBox_band_min_MHz.value(),
                                     self.doubleSpinBox_band_max_MHz.value())
        else:
            # No filter requested.
            filter_spec = None

        # Build MaskSpec instances for gen if requested:
        if self.groupBox_mask_gen.isChecked():
            # Generation ray angle masks have been requested:
            mask_behaviour_gen = dict_mask_behaviours[self.comboBox_mask_behaviour_gen.currentText()]
            mask_spec_gen = MaskSpec(self.doubleSpinBox_mask_angle_gen.value(), mask_behaviour_gen)
        else:
            # No generation ray masks have been requested:
            mask_spec_gen = None

        # Build MaskSpec instances for det if requested:
        if self.groupBox_mask_det.isChecked():
            # detection ray angle masks have been requested:
            mask_behaviour_det = dict_mask_behaviours[self.comboBox_mask_behaviour_det.currentText()]
            mask_spec_det = MaskSpec(self.doubleSpinBox_mask_angle_det.value(), mask_behaviour_det)
        else:
            # No generation ray masks have been requested:
            mask_spec_det = None

        # Collect the TFM parameters from the input widgets into the tfm_constructor instance:
        self.tfm_constructor = TFMConstructor(image_name_string=self.line_edit_description.text(),
                                              pitch_mm=self.doubleSpinBox_pitch_mm.value(),
                                              n_elements=self.n_elements,
                                              grid_size_x_mm=self.doubleSpinBox_grid_size_x_mm.value(),
                                              grid_size_z_mm=self.doubleSpinBox_grid_size_z_mm.value(),
                                              n_pixels_z=self.spinBox_n_pixels_z.value(),
                                              material=material,
                                              wave_type_send=dict_wave_types_send[self.comboBox_send.currentText()],
                                              wave_type_receive=dict_wave_types_receive[
                                                  self.comboBox_receive.currentText()],
                                              filter_spec=filter_spec,
                                              mask_spec_gen=mask_spec_gen,
                                              mask_spec_det=mask_spec_det)
        # The tfm_constructor instance variable will be accessible from the DialogTFMParams instance wherever it is created.

    def set_tfm_params_in_input_widgets(self, tfm_constructor):
        # Set array parameters:
        self.doubleSpinBox_pitch_mm.setValue(tfm_constructor.pitch_mm)

        # Set imaging grid parameters:
        self.doubleSpinBox_grid_size_x_mm.setValue(tfm_constructor.grid_size_x_mm)
        self.doubleSpinBox_grid_size_z_mm.setValue(tfm_constructor.grid_size_z_mm)
        self.spinBox_n_pixels_z.setValue(tfm_constructor.n_pixels_z)

        # Set material parameters:
        self.doubleSpinBox_c_l_mpers.setValue(tfm_constructor.material.c_l_mpers)
        self.doubleSpinBox_c_t_mpers.setValue(tfm_constructor.material.c_t_mpers)
        self.doubleSpinBox_c_lsaw_mpers.setValue(tfm_constructor.material.c_lsaw_mpers)

        # Set send and receive wave types:
        # Send wave type:
        index_send = self.comboBox_send.findText(tfm_constructor.wave_type_send.string_name)
        if index_send >= 0:
            self.comboBox_send.setCurrentIndex(index_send)
        # Receive wave type:
        index_receive = self.comboBox_receive.findText(tfm_constructor.wave_type_receive.string_name)
        if index_receive >= 0:
            self.comboBox_receive.setCurrentIndex(index_receive)

        # Set filter parameters:
        if tfm_constructor.filter_spec:
            self.groupBox_filter.setChecked(True)
            self.spinBox_butter_order.setValue(tfm_constructor.filter_spec.butter_order)
            self.doubleSpinBox_band_min_MHz.setValue(tfm_constructor.filter_spec.band_min_mhz)
            self.doubleSpinBox_band_max_MHz.setValue(tfm_constructor.filter_spec.band_max_mhz)

        # Set masking parameters:
        if tfm_constructor.mask_spec_gen:
            # Set groupbox tickbox:
            self.groupBox_mask_gen.setChecked(True)
            # Set mask angle in spinbox:
            self.doubleSpinBox_mask_angle_gen.setValue(tfm_constructor.mask_spec_gen.mask_angle_deg)
            # Set mask behaviour in combobox:
            behaviour_string = tfm_constructor.mask_spec_gen.mask_behaviour.string_name
            index = self.comboBox_mask_behaviour_gen.findText(behaviour_string)
            if index >= 0:
                self.comboBox_mask_behaviour_gen.setCurrentIndex(index)
        if tfm_constructor.mask_spec_det:
            # Set groupbox tickbox:
            self.groupBox_mask_det.setChecked(True)
            # Set mask angle in spinbox:
            self.doubleSpinBox_mask_angle_det.setValue(tfm_constructor.mask_spec_det.mask_angle_deg)
            # Set mask behaviour in combobox:
            behaviour_string = tfm_constructor.mask_spec_det.mask_behaviour.string_name
            index = self.comboBox_mask_behaviour_det.findText(behaviour_string)
            if index >= 0:
                self.comboBox_mask_behaviour_det.setCurrentIndex(index)

    def combobox_mask_angle_gen_text_changed(self, mask_angle_choice):
        angle_calculation_function = dict_mask_angles[mask_angle_choice]
        if angle_calculation_function:
            # Make the mask angle doubleSpinBox read-only:
            self.doubleSpinBox_mask_angle_gen.setReadOnly(True)
            # Calculate the chosen mask angle:
            mask_angle = angle_calculation_function(c_l_mpers=self.doubleSpinBox_c_l_mpers.value(),
                                                    c_t_mpers=self.doubleSpinBox_c_t_mpers.value())
            # Write the mask angle value to the DoubleSpinBox:
            self.doubleSpinBox_mask_angle_gen.setValue(mask_angle)
        else:
            # The user has selected the 'manual entry' option (which has no associated angle generation function):
            # Make the mask angle doubleSpinBox editable:
            self.doubleSpinBox_mask_angle_gen.setReadOnly(False)

    def combobox_mask_angle_det_text_changed(self, mask_angle_choice):
        angle_calculation_function = dict_mask_angles[mask_angle_choice]
        if angle_calculation_function:
            # Make the mask angle doubleSpinBox read-only:
            self.doubleSpinBox_mask_angle_det.setReadOnly(True)
            # Calculate the chosen mask angle:
            mask_angle = angle_calculation_function(c_l_mpers=self.doubleSpinBox_c_l_mpers.value(),
                                                    c_t_mpers=self.doubleSpinBox_c_t_mpers.value())
            # Write the mask angle value to the DoubleSpinBox:
            self.doubleSpinBox_mask_angle_det.setValue(mask_angle)
        else:
            # The user has selected the 'manual entry' option (which has no associated angle generation function):
            # Make the mask angle doubleSpinBox editable:
            self.doubleSpinBox_mask_angle_det.setReadOnly(False)

    def speed_value_changed(self):
        # The user has changed the value of either c_T or c_L.  This changes the value of the critical angle, so:
        angle_combo_boxes = (self.comboBox_mask_angle_gen, self.comboBox_mask_angle_det)
        angle_double_spin_boxes = (self.doubleSpinBox_mask_angle_gen, self.doubleSpinBox_mask_angle_det)
        for combo_box, double_spin_box in zip(angle_combo_boxes, angle_double_spin_boxes):
            mask_angle_choice = combo_box.currentText()
            if mask_angle_choice == 'Critical angle':
                angle_calculation_function = dict_mask_angles[mask_angle_choice]
                # Calculate the angle, no matter what the user has asked for:
                mask_angle = angle_calculation_function(c_l_mpers=self.doubleSpinBox_c_l_mpers.value(),
                                                        c_t_mpers=self.doubleSpinBox_c_t_mpers.value())
                # Write the critical angle value to the DoubleSpinBox:
                double_spin_box.setValue(mask_angle)

    def update_grid(self):
        self.grid_preview_widget.update_checkerboard(self.doubleSpinBox_grid_size_x_mm.value(),
                                                     self.doubleSpinBox_grid_size_z_mm.value(),
                                                     self.spinBox_n_pixels_z.value())

    def update_array(self):
        self.grid_preview_widget.update_array_pitch(self.doubleSpinBox_pitch_mm.value())
