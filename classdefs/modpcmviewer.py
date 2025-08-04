from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, Signal
import numpy as np

from qtdesigner.pcmviewer.UI_PCM_viewer import Ui_PCM_viewer
from functions.modcalculategenindicesatangle import calculate_gen_indices_at_angle
from functions.modbuildxelements import build_x_elements_m
from functions.modcalculatedirectrayanglespixel import calculate_angles_direct_rays_to_pixel_all_el_deg
from functions.modordergenindicesforcumsum import order_gen_indices_for_cumsum
from corevariables.modphasorarrowschemes import dict_phasor_schemes
from corevariables.modsumtypes import dict_sum_types
from qtdesigner.dialogs.moddialogprettyprint import DialogPrettyPrint


class PCMViewer(QWidget, Ui_PCM_viewer):
    """PCM stands for pixel contributions matrix, and this class is a viewer widget that displays the PCM for a
    selected pixel."""

    # Define a signal to emit when this window is closed:
    pcm_viewer_closed = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Instance variables:
        self.critical_angle_lines_visible = False
        self.pcm_complex = np.zeros([64, 64])
        self.pcm_amplitudes_mV = np.zeros([64, 64])
        self.c_min_mv = -1
        self.c_max_mv = 1
        self.n_tx = None
        self.pitch_mm = None
        self.z_pixel_m = None
        self.x_pixel_m = None
        self.real = True
        self.set_pcm_data_function = self.set_data_amplitude
        self.mouse_down_in_amp_vs_angle_plot = False

        # Set attributes:
        self.setAttribute(Qt.WA_DeleteOnClose)

        # Set window flags:
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        # Set 'real' tickbox to be ticked by default:
        self.checkBox_real.setChecked(True)

        # Add phasor arrow color schemes to combo box from reference dict:
        for color_scheme in dict_phasor_schemes.keys():
            self.comboBox_phasor_schemes.addItem(color_scheme)

        # Add mask gen angle meanings to combo box from reference dict:
        self.comboBox_mask_gen_angle_meaning.addItem('Maximum')
        self.comboBox_mask_gen_angle_meaning.addItem('Minimum')

        # Add sum types to combo box from reference dict:
        for sum_type in dict_sum_types.keys():
            self.comboBox_sum_type.addItem(sum_type)

        # Wire signals to slots:
        self.check_box_crit.checkStateChanged.connect(self.toggle_crit_lines)
        self.check_box_sign.checkStateChanged.connect(self.toggle_sign_contrast)
        self.checkBox_real.checkStateChanged.connect(self.real_toggled)
        self.checkBox_imag.checkStateChanged.connect(self.imag_toggled)
        self.pushButton_re_calc_phasor.pressed.connect(self.plot_phasor_button_clicked)
        self.pushButton_plot_cumsum.pressed.connect(self.update_sum_vs_gen_angle_plot)
        self.pushButton_print_pcm.pressed.connect(self.print_pcm_pressed)
        self.pushButton_print_graph.pressed.connect(self.print_graph_pressed)

        # Matplotlib events:
        self.sum_vs_mask_angle_widget.mpl_canvas.fig.canvas.mpl_connect('button_press_event',
                                                                        self.amp_vs_mask_angle_button_press)
        self.sum_vs_mask_angle_widget.mpl_canvas.fig.canvas.mpl_connect('motion_notify_event',
                                                                        self.amp_vs_mask_angle_motion_notify)
        self.sum_vs_mask_angle_widget.mpl_canvas.fig.canvas.mpl_connect('button_release_event',
                                                                        self.amp_vs_mask_angle_button_release)
        self.sum_vs_mask_angle_widget.mpl_canvas.fig.canvas.mpl_connect('scroll_event',
                                                                        self.amp_vs_mask_angle_scroll)

    def closeEvent(self, event):
        self.pcm_viewer_closed.emit()
        super().closeEvent(event)

    def macro_new_pixel_clicked(self, pcm_complex, x_pixel_m, z_pixel_m, critical_angle_radians, pitch_mm, n_tx):
        # The user has clicked a new pixel.
        self.n_tx = n_tx
        self.x_pixel_m = x_pixel_m
        self.z_pixel_m = z_pixel_m
        self.pitch_mm = pitch_mm
        # Update the pcm display:
        self.update_pcm(pcm_complex)
        # Update the critical angle lines:
        self.update_critical_angle_lines(x_pixel_m, z_pixel_m, critical_angle_radians, pitch_mm, n_tx)

    def update_pcm(self, pcm_complex):
        self.pcm_complex = pcm_complex

        if self.checkBox_real.isChecked():
            self.pcm_amplitudes_mV = np.real(pcm_complex) * 1000
        else:
            self.pcm_amplitudes_mV = np.imag(pcm_complex) * 1000

        # Call the current set_pcm_data function:
        self.set_pcm_data_function()

    def toggle_crit_lines(self):
        if self.check_box_crit.isChecked():
            # Make the critical angle lines visible:
            self.mpl_widget_pcm.crit_angle_line_lower.set_visible(True)
            self.mpl_widget_pcm.crit_angle_line_upper.set_visible(True)
            self.sum_vs_mask_angle_widget.line_crit_angle.set_visible(True)
        else:
            # Make the critical angle lines invisible:
            self.mpl_widget_pcm.crit_angle_line_lower.set_visible(False)
            self.mpl_widget_pcm.crit_angle_line_upper.set_visible(False)
            self.sum_vs_mask_angle_widget.line_crit_angle.set_visible(False)

        # Blit the critical angle lines on both the PCM plot and sum vs mask angle plot:
        self.mpl_widget_pcm.blit_manager.blit_all_animated_artists()
        self.sum_vs_mask_angle_widget.blit_manager.blit_all_animated_artists()

    def update_critical_angle_lines(self, x_pixel_m, z_pixel_m, critical_angle_radians, pitch_mm, n_tx):
        # Calculate critical gen indices:
        gen_index_crit_lower, gen_index_crit_upper = calculate_gen_indices_at_angle(x_pixel_m, z_pixel_m,
                                                                                    critical_angle_radians,
                                                                                    pitch_mm, n_tx)
        # Re-position the critical boundary lines on the PCM plot:
        self.mpl_widget_pcm.reposition_crit_angle_lines(gen_index_crit_lower, gen_index_crit_upper)

        # Re-position the critical angle line on the amp vs mask angle graph:
        self.sum_vs_mask_angle_widget.reposition_crit_angle_line(np.rad2deg(critical_angle_radians))

    def toggle_sign_contrast(self):
        if self.check_box_sign.isChecked():
            # Enter sign contrast:
            self.set_pcm_data_function = self.set_data_sign
            self.mpl_widget_pcm.axes_image.set_clim(vmin=-1, vmax=1)
        else:
            # Return to normal imshow contrast:
            self.set_pcm_data_function = self.set_data_amplitude
            self.mpl_widget_pcm.axes_image.set_clim(vmin=self.c_min_mv,
                                                    vmax=self.c_max_mv)

        # Call the new function:
        self.set_pcm_data_function()
        self.re_draw_pcm_mplcanvas()

    def new_c_min(self, c_min_mv):
        self.c_min_mv = c_min_mv
        if not self.check_box_sign.isChecked():
            # Update the c limit of the axes image:
            self.mpl_widget_pcm.axes_image.set_clim(vmin=c_min_mv)

    def new_c_max(self, c_max_mv):
        self.c_max_mv = c_max_mv
        if not self.check_box_sign.isChecked():
            # Update the c limit of the axes image:
            self.mpl_widget_pcm.axes_image.set_clim(vmax=c_max_mv)

    def re_draw_pcm_mplcanvas(self):
        self.mpl_widget_pcm.mpl_canvas.draw()

    def update_axes(self, n_tx):
        self.mpl_widget_pcm.axes_image.set_extent((0, n_tx-1, n_tx-1, 0))

    def set_data_amplitude(self):
        self.mpl_widget_pcm.axes_image.set_data(self.pcm_amplitudes_mV)

    def set_data_sign(self):
        self.mpl_widget_pcm.axes_image.set_data(np.sign(self.pcm_amplitudes_mV))

    def real_toggled(self):
        if self.checkBox_real.isChecked():
            # Use real:
            # Un-check imag checkbox without emitting signals:
            self.checkBox_imag.blockSignals(True)
            self.checkBox_imag.setChecked(False)
            self.checkBox_imag.blockSignals(False)
            # Use real part:
            self.pcm_amplitudes_mV = np.real(self.pcm_complex)
        else:
            # Use imag:
            # Check imag checkbox without emitting signals:
            self.checkBox_imag.blockSignals(True)
            self.checkBox_imag.setChecked(True)
            self.checkBox_imag.blockSignals(False)
            # Use imag part:
            self.pcm_amplitudes_mV = np.imag(self.pcm_complex)
        # Call set data function:
        self.set_pcm_data_function()
        # Re-draw pcm mpl_canvas:
        self.mpl_widget_pcm.mpl_canvas.draw()

    def imag_toggled(self):
        if self.checkBox_imag.isChecked():
            # Use imag:
            # Un-check real checkbox without emitting signals:
            self.checkBox_real.blockSignals(True)
            self.checkBox_real.setChecked(False)
            self.checkBox_real.blockSignals(False)
            # Use imag part:
            self.pcm_amplitudes_mV = np.imag(self.pcm_complex)
        else:
            # Use real:
            # Check real checkbox without emitting signals:
            self.checkBox_real.blockSignals(True)
            self.checkBox_real.setChecked(True)
            self.checkBox_real.blockSignals(False)
            # Use real part:
            self.pcm_amplitudes_mV = np.real(self.pcm_complex)
        # Call set data function:
        self.set_pcm_data_function()
        # Re-draw pcm mpl_canvas:
        self.mpl_widget_pcm.mpl_canvas.draw()

    def plot_phasor_button_clicked(self):
        # Obtain the PhasorScheme instance associated with the selection of the ComboBox:
        phasor_scheme = dict_phasor_schemes[self.comboBox_phasor_schemes.currentText()]
        # Sum elements of the PCM depending on which phasor scheme has been selected:
        complex_numbers = phasor_scheme.summing_func(self.pcm_complex)
        # Create a list of rgb colors for the arrows according to the color_func of the selected PhasorScheme:
        n_tx = np.shape(self.pcm_complex)[1]
        colors = phasor_scheme.color_func(n_tx)
        # Call plotting method of Phasor plot widget:
        max_amp = np.max(np.abs(complex_numbers))
        self.phasor_plot_widget.plot_phase_arrows(complex_numbers, colors, max_amp)
        # Re-draw phasor MplCanvas:
        self.phasor_plot_widget.mpl_canvas.draw()

    def update_sum_vs_gen_angle_plot(self):
        # Update the sum vs gen angle plot:
        x_elements_m = build_x_elements_m(self.n_tx, self.pitch_mm)
        gen_angles = calculate_angles_direct_rays_to_pixel_all_el_deg(self.x_pixel_m, self.z_pixel_m, x_elements_m)
        # Determine the order in which to sum the columns of the PCM based on the value of the mask angle meaning
        # comboBox:
        mask_angle_meaning = self.comboBox_mask_gen_angle_meaning.currentText()
        gen_indices_in_cumsum_order = order_gen_indices_for_cumsum(gen_angles, mask_angle_meaning)
        # Calculate the cumulative sum in the manner specified by the sum type comboBox:
        sum_type = self.comboBox_sum_type.currentText()
        summing_func = dict_sum_types[sum_type]
        cumsum = summing_func(self.pcm_complex, gen_indices_in_cumsum_order)
        # Set x and y data of plot widget:
        gen_angles_ordered = gen_angles[gen_indices_in_cumsum_order]
        self.sum_vs_mask_angle_widget.update_data(gen_angles_ordered, cumsum, y_label=sum_type)
        # Prompt re-draw of cumsum vs angle widget:
        self.sum_vs_mask_angle_widget.mpl_canvas.draw()

    def amp_vs_mask_angle_button_press(self, event):
        if event.inaxes is None:
            return
        elif event.button != 1:
            return
        else:
            # The user has clicked the left mouse button inside the plot.
            self.mouse_down_in_amp_vs_angle_plot = True
            # Move the angle marker lines:
            self.update_mouse_angle_markers(event.xdata)

    def amp_vs_mask_angle_motion_notify(self, event):
        if self.mouse_down_in_amp_vs_angle_plot is False:
            return
        elif event.inaxes is None:
            return
        elif event.button != 1:
            return
        else:
            # Move the marker lines:
            self.update_mouse_angle_markers(event.xdata)

    def amp_vs_mask_angle_button_release(self, event):
        if event.button != 1:
            return
        else:
            self.mouse_down_in_amp_vs_angle_plot = False

    def update_mouse_angle_markers(self, angle_degrees):
        # Sum vs mask angle plot:
        # Send the angle to the marker line:
        self.sum_vs_mask_angle_widget.reposition_mouse_angle_line_and_text(angle_degrees)
        # Blit the marker lines:
        self.sum_vs_mask_angle_widget.blit_manager.blit_all_animated_artists()

        # PCM plot:
        # Move the mouse angle lines to new gen indices based on the selected angle:
        gen_lower, gen_upper = calculate_gen_indices_at_angle(self.x_pixel_m, self.z_pixel_m, np.deg2rad(angle_degrees),
                                                              self.pitch_mm, self.n_tx)
        self.mpl_widget_pcm.reposition_mouse_angle_lines(gen_upper, gen_lower)
        # Blit the marker lines:
        self.mpl_widget_pcm.blit_manager.blit_all_animated_artists()

    def amp_vs_mask_angle_scroll(self, event):
        # The direction ('up' or 'down') of the scroll event should move the mouse angle lines by + or - an increment:
        increment_degrees = 0.5 if event.button == 'up' else -0.5
        # Calculate the new mouse angle:
        min_angle, max_angle = self.sum_vs_mask_angle_widget.mpl_canvas.ax.get_xlim()
        old_mouse_angle = self.sum_vs_mask_angle_widget.line_mouse_angle.get_xdata()[0]
        new_mouse_angle = np.clip(old_mouse_angle + increment_degrees, min_angle, max_angle)
        # Move the marker lines:
        self.update_mouse_angle_markers(new_mouse_angle)

    def print_pcm_pressed(self):
        # Launch an instance of the PrettyPrint dialog:
        title_string = f'Pixel contributions matrix for pixel at ({self.x_pixel_m * 1000:.2f}, {self.z_pixel_m * 1000:.2f}) mm'
        dialog_pretty_print = DialogPrettyPrint(self, self.mpl_widget_pcm.mpl_canvas.fig,
                                                'Generation index',
                                                'Detection index',
                                                'Amplitude (mV)',
                                                title_string=title_string)
        dialog_pretty_print.exec()

    def print_graph_pressed(self):
        # Launch an instance of the PrettyPrint dialog:
        title_string = f'[insert] vs mask angle for pixel at ({self.x_pixel_m * 1000 :.2f}, {self.z_pixel_m * 1000 :.2f}) mm'
        dialog_pretty_print = DialogPrettyPrint(self, self.sum_vs_mask_angle_widget.mpl_canvas.fig,
                                                'Mask angle (°)',
                                                '[Insert]',
                                                'Amplitude (mV)',
                                                title_string=title_string)
        dialog_pretty_print.exec()
