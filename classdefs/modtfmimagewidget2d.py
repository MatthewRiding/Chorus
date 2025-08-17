import numpy as np
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QFrame, QLabel, QSlider, QComboBox, QDoubleSpinBox
from PySide6.QtCore import Signal, Qt
from classdefs.modmytoolbar import MyToolBar

from classdefs.modqtmatplotlib import MplCanvas
from classdefs.modblitmanager import BlitManager
from qtdesigner.dialogs.moddialogprettyprint import DialogPrettyPrint
from corevariables.modimagetypes import dict_image_types


class TFMImageWidget2D(QWidget):
    # Define custom signals:
    pixel_clicked = Signal(tuple)

    def __init__(self, *args, **kwargs):
        super(TFMImageWidget2D, self).__init__(*args, **kwargs)

        self.listed_tfm_image = None
        self.colormap_max_abs_nm = None
        self.colormap_dB_min = -10  # Default slider value in dB.
        self.image_type = dict_image_types['dB']  # Default to dB mode.

        # Create an instance of the MplCanvas class:
        self.mpl_canvas = MplCanvas(self, width=5, height=4, dpi=100)

        # Create the interactive matplotlib toolbar:
        self.toolbar = MyToolBar(self.mpl_canvas, self, self.save_button_clicked)

        # Add the toolbar to a horizontal layout with a label to describe the plot:
        layout_title_and_tools = QHBoxLayout()
        layout_title_and_tools.setContentsMargins(0, 0, 0, 0)
        self.label_title = QLabel()
        self.label_title.setStyleSheet("font: 14pt Segoe UI")
        self.label_title.setText('  TFM  ')
        v_line = QFrame()
        v_line.setFrameShape(QFrame.Shape.VLine)
        v_line.setFrameShadow(QFrame.Shadow.Sunken)
        layout_title_and_tools.addWidget(self.label_title)
        layout_title_and_tools.addWidget(v_line)
        layout_title_and_tools.addWidget(self.toolbar)

        # Stack the h layout and the Mplcanvas into a vertical layout:
        v_layout_toolbar_and_canvas = QVBoxLayout()
        v_layout_toolbar_and_canvas.addLayout(layout_title_and_tools)
        v_layout_toolbar_and_canvas.addWidget(self.mpl_canvas)

        # Create the slider area:
        # Create the widgets that will form the slider area:
        self.combo_box_image_type = QComboBox()
        self.label_slider_meaning = QLabel()
        self.spin_box_clim = QDoubleSpinBox()
        self.slider = QSlider(orientation=Qt.Vertical)
        # Stack these widgets into a vertical layout:
        v_layout_slider_area = QVBoxLayout()
        v_layout_slider_area.addWidget(self.combo_box_image_type, alignment=Qt.AlignHCenter)
        v_layout_slider_area.addWidget(self.label_slider_meaning, alignment=Qt.AlignHCenter)
        v_layout_slider_area.addWidget(self.spin_box_clim, alignment=Qt.AlignHCenter)
        v_layout_slider_area.addWidget(self.slider, alignment=Qt.AlignHCenter)

        # Stack the two vertical layouts horizontally into an H layout:
        h_layout = QHBoxLayout()
        h_layout.addLayout(v_layout_toolbar_and_canvas)
        h_layout.addLayout(v_layout_slider_area)

        # Apply this layout to the main widget:
        self.setLayout(h_layout)

        # Set MplCanvas style elements:
        my_grey = '0.3'
        fontsize_labels = 8
        self.mpl_canvas.fig.patch.set_alpha(0.0)
        self.mpl_canvas.ax.patch.set_alpha(0.0)
        self.mpl_canvas.setStyleSheet("background-color:transparent;")
        self.mpl_canvas.ax.tick_params(color=my_grey, labelcolor=my_grey)
        self.mpl_canvas.ax.spines[:].set_edgecolor(my_grey)
        self.mpl_canvas.ax.set_xlabel('x [mm]', fontsize=fontsize_labels)
        self.mpl_canvas.ax.set_ylabel('z [mm]', fontsize=fontsize_labels)
        self.mpl_canvas.ax.xaxis.label.set_color(my_grey)
        self.mpl_canvas.ax.yaxis.label.set_color(my_grey)
        self.mpl_canvas.ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
        self.mpl_canvas.ax.tick_params(axis='both', which='major', labelsize=8, pad=1)
        self.mpl_canvas.ax.xaxis.set_label_position('top')
        self.mpl_canvas.ax.autoscale(enable=True, axis='both', tight=True)

        # Plot a default image to update later:
        def empty_image_plot(**dict_kwargs):
            default_data_array_db = np.ones([200, 300]) * -100  # Decibels
            c_map = 'viridis'
            axes_image = self.mpl_canvas.ax.imshow(default_data_array_db, vmin=0, vmax=0, cmap=c_map,
                                                   interpolation='nearest', **dict_kwargs)
            return axes_image

        self.axes_image = empty_image_plot()

        # Update the axes image to reflect the default image_type:
        self.update_axis_image_clims_for_image_type()

        # Create an empty plot that will mark the selected pixel:
        self.plotref_selected_pixel, = self.mpl_canvas.ax.plot([], [],
                                                               markeredgewidth=0,
                                                               markersize=6,
                                                               color=[1, 1, 1],
                                                               linestyle='None',
                                                               marker=6)

        # Set up the slider area widgets:
        # Add image types to the image type combobox:
        self.combo_box_image_type.addItems(dict_image_types.keys())
        # Set the slider to always have a min of 0, a max of 100 and 100 steps.
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setSingleStep(1)
        # Configure the other slider area widgets for the default ImageType:
        self.configure_slider_area_for_image_type()
        # Deactivate the slider area widgets by default, since no TFM image has been loaded:
        self.set_slider_area_widgets_enabled(False)

        # Connect to the 'button_press_event':
        self.mpl_canvas.fig.canvas.mpl_connect('button_press_event', self.mplcanvas_click_response)

        # Create an instance of BlitManager to manage blitting:
        self.blit_manager = BlitManager(self.mpl_canvas, [self.axes_image,
                                                          self.plotref_selected_pixel])

        # Wire signals to slots:
        self.combo_box_image_type.currentTextChanged.connect(self.image_type_changed)
        self.slider.valueChanged.connect(self.slider_value_changed)
        self.spin_box_clim.valueChanged.connect(self.spinbox_value_changed)

    def mplcanvas_click_response(self, event):
        # Plot the white caret marker at the location that has been clicked:
        self.plotref_selected_pixel.set_data([event.xdata], [event.ydata])
        self.blit_manager.blit_all_animated_artists()

        # Emit the 'pixel_clicked' event to prompt the B-scan and iso-t widgets to display the associated delay law:
        x_coord_m = event.xdata * 10 ** -3
        z_coord_m = event.ydata * 10 ** -3
        self.pixel_clicked.emit((x_coord_m, z_coord_m))

    def motion_hover(self, event):
        # MatPlotLib mouse motion event response:
        if event.inaxes == self.mpl_canvas.ax:
            print(round(event.xdata), round(event.ydata))

    def display_default_image(self):
        self.axes_image.set_data(np.zeros([2, 2]))

    def clear_pixel_cursor(self):
        self.plotref_selected_pixel.set_data([], [])

    def redraw(self):
        self.mpl_canvas.draw()

    def save_button_clicked(self):
        # Launch an instance of the PrettyPrint dialog:
        dialog_pretty_print = DialogPrettyPrint(self, self.mpl_canvas.fig,
                                                'x (mm)',
                                                'z (mm)',
                                                'Intensity (dB)',
                                                title_string=self.listed_tfm_image.tfm_constructor.image_name_string)
        dialog_pretty_print.exec()

    def new_listed_tfm_image(self, listed_tfm_image):
        self.listed_tfm_image = listed_tfm_image

        # Compute new image array for current image type:
        self.update_image_array()

        # Update image x and z axis limits:
        self.update_axes_centred()

        # Create a bool to use as a flag:
        nm_clims_need_adjusting = False
        # If the current colormap_max_abs exceeds the max_abs of the new TFM image (or is still at its default 'None'),
        # then trim the colormap_max_abs value down to the new maximum:
        if self.colormap_max_abs_nm is None or self.colormap_max_abs_nm > self.listed_tfm_image.max_abs_nm:
            # Set colormap_max_abs to new image max_abs:
            self.colormap_max_abs_nm = self.listed_tfm_image.max_abs_nm
            nm_clims_need_adjusting = True

        # Update slider_max & current slider/spinbox value: This requires some logic.
        if self.image_type.slider_inverted_appearance:
            # The slider is in inverted mode.
            # The dB limits are always 0 - -40dB.  We are already in dB mode.  No need to change slider limits.
            pass
        else:
            # The current image type requires the slider limits to span from 0 to the maximum absolute value of
            # displacement in the new TFM image.
            # The minimum will already be zero.  We just need to set the new maximum based on the max(abs()) of the new
            # image.
            self.spin_box_clim.setMaximum(self.listed_tfm_image.max_abs_nm)

            # Check if the current value of the slider is greater than the max abs of the new TFM image:
            if nm_clims_need_adjusting:
                # Set slider & spinbox values to trimmed colormap_max_abs value:
                self.set_slider_and_spinbox_values_no_signals(self.colormap_max_abs_nm)
                # Set clim of axis image:
                self.axes_image.set_clim(vmin=-self.colormap_max_abs_nm, vmax=self.colormap_max_abs_nm)

        # Enable the dB min slider and spinbox:
        self.set_slider_area_widgets_enabled(True)

        # Completely re-draw the MplCanvas (axes limits may have changed, so Blitting is not appropriate):
        self.mpl_canvas.draw()

    def update_image_array(self):
        # Use the current ImageType's conversion function to compute the image array:
        image_array = self.image_type.conversion_function(self.listed_tfm_image.image_complex_nm)

        # Set image data for the axes image object:
        self.axes_image.set_data(image_array)

    def update_axes_centred(self):
        # Set axis limits to reflect the size of the chosen TFM grid:
        self.axes_image.set_extent((-self.listed_tfm_image.tfm_constructor.grid_size_x_mm / 2,
                                    self.listed_tfm_image.tfm_constructor.grid_size_x_mm / 2,
                                    self.listed_tfm_image.tfm_constructor.grid_size_z_mm,
                                    0))

    def image_type_changed(self):
        # Get the current image_type based on the text in the combobox:
        name_string = self.combo_box_image_type.currentText()
        self.image_type = dict_image_types[name_string]

        # Configure slider area for image type:
        self.configure_slider_area_for_image_type()

        # Update AxisImage to reflect chosen image type:
        self.update_axes_for_new_image_type()

    def update_axes_for_new_image_type(self):
        # Update the MplCanvas AxisImage 2D data array for this new ImageType:
        self.update_image_array()

        # Update the AxisImage colormap:
        self.axes_image.set_cmap(self.image_type.cmap)

        # Set up the AxisImage clims differently depending on whether we are in inverted mode or not:
        self.update_axis_image_clims_for_image_type()

        # Blit changes for fast updating:
        self.blit_manager.blit_all_animated_artists()

    def update_axis_image_clims_for_image_type(self):
        # Set up the AxisImage clims differently depending on whether we are in inverted mode or not:
        if self.image_type.slider_inverted_appearance:
            # We are in inverted mode, i.e. using Decibels relative to the chosen normalisation pixel.
            # Set the vmin and vmax clims of the AxisImage, remembering the previously stored value:
            v_min = self.colormap_dB_min
            v_max = 0
        else:
            # We are not in inverted mode, and are therefore displaying an image of raw summed displacement values (nm).
            # set the vmin and vmax clims of the AxisImage, recalling the previously stored value:
            v_max = self.colormap_max_abs_nm
            # Use clims that are symmetric about zero (for displacement images that can be either positive or negative,
            # e.g. the Real image), or vmin=0 (for images such as Abs that are always positive):
            if self.image_type.can_be_positive_and_negative:
                v_min = -v_max
            else:
                v_min = 0

        # Set the clims of the AxisImage:
        self.axes_image.set_clim(vmin=v_min, vmax=v_max)

    def configure_slider_area_for_image_type(self):
        # Set slider meaning label text:
        self.label_slider_meaning.setText(self.image_type.string_slider_meaning)
        # Set slider inverted appearance:
        self.slider.setInvertedAppearance(self.image_type.slider_inverted_appearance)
        # Set up the spinbox limits differently depending on whether we are in inverted mode
        # or not:
        if self.image_type.slider_inverted_appearance:
            # We are in inverted mode, i.e. using Decibels relative to the chosen normalisation pixel.
            self.configure_spinbox_for_db_mode()
            # Set the current values of the spinbox and slider:
            clim_value = self.colormap_dB_min
        else:
            # We are not in inverted mode, and are therefore displaying an image of raw summed displacement values (nm).
            self.configure_spinbox_for_nm_mode()
            # Set the current values of the spinbox and slider:
            clim_value = self.colormap_max_abs_nm

        self.set_slider_and_spinbox_values_no_signals(clim_value)

    def clear_and_deactivate_tfm_image_area(self):
        # The user has clicked on a TFM image that is still processing:
        # Display nothing on the TFM image plot:
        self.display_default_image()
        self.clear_pixel_cursor()
        self.mpl_canvas.redraw()
        # Display zero on the dB slider and spin box (this also sets self.decibel_minimum to zero):
        self.slider.setValue(0)
        self.spin_box_clim.setValue(0)
        # Disable the slider area widgets:
        self.set_slider_area_widgets_enabled(False)

    def set_slider_area_widgets_enabled(self, enabled_tf):
        self.combo_box_image_type.setEnabled(enabled_tf)
        self.spin_box_clim.setEnabled(enabled_tf)
        self.slider.setEnabled(enabled_tf)

    def set_slider_and_spinbox_values_no_signals(self, spinbox_value):
        # Set spinbox value:
        self.set_spinbox_value_without_signal(spinbox_value)
        # The slider only ever takes positive values:
        slider_integer = self.convert_spinbox_value_to_slider_integer(spinbox_value)
        self.set_slider_integer_without_signal(slider_integer)

    def slider_value_changed(self, slider_value):
        # The slider only outputs positive integers between 0 and 100.  These must be converted to nm or dB, depending
        # on the current ImageType.
        spinbox_value = self.convert_slider_output_to_spinbox_value(slider_value)
        # Display the new value in the spinbox, without emitting signals:
        self.set_spinbox_value_without_signal(spinbox_value)
        # Call the generic clim changed function:
        self.clim_value_changed(spinbox_value)

    def spinbox_value_changed(self, spinbox_value):
        # Slider always runs from 0-100.  Convert spinbox value to an integer in this range:
        slider_integer = self.convert_spinbox_value_to_slider_integer(spinbox_value)
        # Display the new value on the slider, without emitting signals:
        self.set_slider_integer_without_signal(slider_integer)
        # Call the generic dB min changed function:
        self.clim_value_changed(spinbox_value)

    def clim_value_changed(self, spinbox_value):
        # Different paths of action depending on whether we are in dB mode or not:
        if self.image_type.slider_inverted_appearance:
            # We are in dB mode:
            # Pin the new value to self:
            self.colormap_dB_min = spinbox_value
            # Set vmin of the AxesImage:
            self.axes_image.set_clim(vmin=self.colormap_dB_min)
        else:
            # We are not in dB mode, we are displaying displacements.
            # Pin the new value to self:
            self.colormap_max_abs_nm = spinbox_value
            # Set v_max:
            v_max = self.colormap_max_abs_nm
            # Set v_min depending on whether the image can be positive and negative or just positive:
            if self.image_type.can_be_positive_and_negative:
                v_min = -v_max
            else:
                v_min = 0
            self.axes_image.set_clim(vmin=v_min, vmax=v_max)

        # Blit the new RGB image:
        self.blit_manager.blit_all_animated_artists()

    def configure_spinbox_for_db_mode(self):
        self.spin_box_clim.blockSignals(True)
        self.spin_box_clim.setDecimals(1)
        step_size_db = 1
        self.spin_box_clim.setSingleStep(step_size_db)
        # Set the limits of the spinbox:
        self.spin_box_clim.setMaximum(0)
        self.spin_box_clim.setMinimum(self.image_type.spinbox_min)
        self.spin_box_clim.blockSignals(False)

    def configure_spinbox_for_nm_mode(self):
        self.spin_box_clim.blockSignals(True)
        self.spin_box_clim.setDecimals(4)
        step_size_nm = 0.001
        self.spin_box_clim.setSingleStep(step_size_nm)
        # Set the limits of the spinbox:
        self.spin_box_clim.setMaximum(self.listed_tfm_image.max_abs_nm)
        self.spin_box_clim.setMinimum(0)
        self.spin_box_clim.blockSignals(False)

    def convert_slider_output_to_spinbox_value(self, slider_value):
        # Slider value will be an integer between 0 and 100.
        slider_proportion = slider_value/self.slider.maximum()

        if self.image_type.slider_inverted_appearance:
            # We are in dB mode.  Slider 0 means 0dB, and slider 100 means image_type.spinbox_min dB:
            spinbox_value_when_slider_at_max = self.image_type.spinbox_min
        else:
            # We are in nm mode.  Sider 0 means 0nm, slider 100 means listed_tfm_image.max_abs_nm nm:
            spinbox_value_when_slider_at_max =  self.listed_tfm_image.max_abs_nm

        spinbox_value = slider_proportion * spinbox_value_when_slider_at_max
        return spinbox_value

    def convert_spinbox_value_to_slider_integer(self, spinbox_value):
        if self.image_type.slider_inverted_appearance:
            # We are in dB mode.
            spinbox_value_when_slider_100 = self.image_type.spinbox_min
        else:
            # We are in nm mode:
            spinbox_value_when_slider_100 = self.listed_tfm_image.max_abs_nm

        spinbox_proportion = spinbox_value / spinbox_value_when_slider_100
        slider_integer = spinbox_proportion * self.slider.maximum()
        return slider_integer

    def set_slider_integer_without_signal(self, slider_integer):
        self.slider.blockSignals(True)
        self.slider.setValue(slider_integer)
        self.slider.blockSignals(False)

    def set_spinbox_value_without_signal(self, spinbox_value):
        self.spin_box_clim.blockSignals(True)
        self.spin_box_clim.setValue(spinbox_value)
        self.spin_box_clim.blockSignals(False)
