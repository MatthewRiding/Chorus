from PySide6.QtWidgets import (QWidget, QVBoxLayout, QCheckBox, QGroupBox, QSizePolicy)
from PySide6.QtGraphsWidgets import Q3DSurfaceWidgetItem
from PySide6.QtQuickWidgets import QQuickWidget
from PySide6.QtGraphs import (QSurfaceDataProxy, QSurface3DSeries, QValue3DAxis, QtGraphs3D, QGraphsTheme)
from PySide6.QtCore import Qt, Signal, QSize
from PySide6.QtGui import QColor, QLinearGradient
import numpy as np

from classdefs.modinvertedaxisformatter import InvertedYAxisFormatter


class DataVolumeVisWidget(QWidget):
    """
    Visualises the 3D data volume (g,d,t) associated with the full A-scan matrix of an ultrasonic array.

    This widget can receive data to update the visualisation of the selected iso-time plane as the selected time is
    varied by external controls.

    In order to achieve the desired chirality of the x and z axes relative to the rows and columns of the numpy
    array delay matrix, delay matrix numpy arrays will be transposed before plotting.  This will make the Qt x-axis
    represent the detection index (original delay matrix numpy rows), and the Qt z-axis represent the generation index
    (original delay matrix numpy columns).
    """

    # Define a closed signal:
    signal_closed = Signal()

    def __init__(self, signal_iso_t_time_changed, signal_iso_gen_index_changed, signal_iso_det_index_changed,
                 signal_delay_matrix_changed, signal_full_matrix_changed, n_elements, t_min_us, t_max_us,
                 iso_t_time_initial_us, iso_gen_index_initial, iso_det_index_initial, delay_matrix_initial_us=None):
        super().__init__()

        # Store instance variables:
        self.signal_iso_t_time_changed = signal_iso_t_time_changed
        self.signal_iso_gen_index_changed = signal_iso_gen_index_changed
        self.signal_iso_det_index_changed = signal_iso_det_index_changed
        self.signal_delay_matrix_changed = signal_delay_matrix_changed
        self.signal_full_matrix_changed = signal_full_matrix_changed
        self.n_elements = n_elements
        self.t_min_us = t_min_us
        self.t_max_us = t_max_us

        # Set window title:
        self.setWindowTitle('Data volume visualiser')

        # Set attributes:
        self.setAttribute(Qt.WA_DeleteOnClose)

        # Set window flags:
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        # Set widget size:
        height_screen_pixels = self.screen().size().height()
        height_initial = int(height_screen_pixels * 0.8)
        width_initial = int(height_initial // 1.2)
        size_initial = QSize(width_initial, height_initial)
        self.resize(size_initial)

        # Build 3D graph:
        # Make a normal QWidget to store a surface widget item:
        self.graph_area_widget = QQuickWidget()
        # Make the surface widget item and assign its home widget:
        self.surface_widget_item = Q3DSurfaceWidgetItem()
        self.surface_widget_item.setWidget(self.graph_area_widget)

        # Customise the QSurfaceWidgetItem aesthetics:
        # Set aspect ratio of surface widget item (x or z / y):
        self.surface_widget_item.setAspectRatio(0.4)
        # Set camera initial position & view:
        self.surface_widget_item.setCameraZoomLevel(200.0)
        self.surface_widget_item.setCameraPreset(QtGraphs3D.CameraPreset.IsometricRight)
        # Set margins around axis data limits:
        self.surface_widget_item.setMargin(0)
        theme = self.surface_widget_item.activeTheme()
        theme.setLabelBackgroundVisible(False)
        theme.setLabelBorderVisible(False)

        # Create axes objects to allow axis customisation:
        self._x_axis = QValue3DAxis()
        self._z_axis = QValue3DAxis()
        self._y_axis = QValue3DAxis()

        # Change axis parameters that will need to be the same for all three axes:
        for axis in [self._x_axis, self._z_axis, self._y_axis]:
            axis.setAutoAdjustRange(False)
            axis.setTitleVisible(True)

        # Customise y-axis:
        # Set title:
        self._y_axis.setTitle('Time (μs)')
        # Set range: Flip sign of all values to achieve inverted appearance:
        self._y_axis.setRange(-t_max_us, -t_min_us)
        self._y_axis.setLabelFormat("%.0f")
        # Use the custom subclass of QValue3DAxisFormatter to invert the tick labels back to positive:
        self._y_axis.setFormatter(InvertedYAxisFormatter())

        # Customise x & z axes:
        def customise_index_axis(q_value_3d_axis):
            q_value_3d_axis.setRange(0, (self.n_elements - 1))
            q_value_3d_axis.setLabelFormat("%u")
        customise_index_axis(self._z_axis)
        customise_index_axis(self._x_axis)
        # Set x & z axis titles:
        self._x_axis.setTitle('Detection index (d)')
        self._z_axis.setTitle('Generation index (g)')

        # Set axes objects as axes of surface widget item:
        self.surface_widget_item.setAxisX(self._x_axis)
        self.surface_widget_item.setAxisY(self._y_axis)
        self.surface_widget_item.setAxisZ(self._z_axis)

        # Each data series to be plotted requires a QSurfaceDataProxy and a QSurface3DSeries:

        # Delay matrix:
        self.surface_data_proxy_delay_matrix = QSurfaceDataProxy()
        self.surface_series_delay_matrix = QSurface3DSeries(self.surface_data_proxy_delay_matrix)
        # Customise appearance of delay surface:
        # Uniform color:
        color_delay_surface = QColor(255, 0, 255)
        self.surface_series_delay_matrix.setBaseColor(color_delay_surface)
        self.surface_series_delay_matrix.setColorStyle(QGraphsTheme.ColorStyle.Uniform)
        # Draw mode (surface, or wireframe or both):
        self.surface_series_delay_matrix.setDrawMode(QSurface3DSeries.DrawFlag.DrawSurfaceAndWireframe)
        # Color gradient:
        # gradient_delay_surface = QLinearGradient()
        # gradient_delay_surface.setColorAt(0.0, QColor(255, 0, 255))
        # gradient_delay_surface.setColorAt(1.0, QColor(0, 255, 0))
        # self.surface_series_delay_matrix.setBaseGradient(gradient_delay_surface)
        # self.surface_series_delay_matrix.setColorStyle(QGraphsTheme.ColorStyle.ObjectGradient)

        # Iso-time plane:
        self.surface_data_proxy_iso_time = QSurfaceDataProxy()
        self.surface_series_iso_time = QSurface3DSeries(self.surface_data_proxy_iso_time)
        # Customise appearance of iso-time plane:
        # Uniform color:
        color_iso_time_plane = QColor(0, 255, 255, 180)
        self.surface_series_iso_time.setBaseColor(color_iso_time_plane)
        self.surface_series_iso_time.setColorStyle(QGraphsTheme.ColorStyle.Uniform)
        # Draw mode (surface, or wireframe or both):
        self.surface_series_iso_time.setDrawMode(QSurface3DSeries.DrawFlag.DrawSurface)

        # Iso-gen plane:
        self.surface_data_proxy_iso_gen = QSurfaceDataProxy()
        self.surface_series_iso_gen = QSurface3DSeries(self.surface_data_proxy_iso_gen)
        # Customise appearance of iso-gen plane:
        # Uniform color:
        color_iso_gen_plane = QColor(255, 0, 92, 180)
        self.surface_series_iso_gen.setBaseColor(color_iso_gen_plane)
        self.surface_series_iso_gen.setColorStyle(QGraphsTheme.ColorStyle.Uniform)
        # Draw mode (surface, or wireframe or both):
        self.surface_series_iso_gen.setDrawMode(QSurface3DSeries.DrawFlag.DrawSurface)
        # Time coordinates:
        # REMEMBER: We are using negative time coordinate values to achieve the look of y-axis inversion:
        self.ydata_iso_gen = np.array([[-self.t_min_us, -self.t_min_us],
                                       [-self.t_max_us, -self.t_max_us]])

        # Iso-det plane:
        self.surface_data_proxy_iso_det = QSurfaceDataProxy()
        self.surface_series_iso_det = QSurface3DSeries(self.surface_data_proxy_iso_det)
        # Customise appearance of iso-det plane:
        # Uniform color:
        color_iso_det_plane = QColor(0, 255, 0, 180)
        self.surface_series_iso_det.setBaseColor(color_iso_det_plane)
        self.surface_series_iso_det.setColorStyle(QGraphsTheme.ColorStyle.Uniform)
        # Draw mode (surface, or wireframe or both):
        self.surface_series_iso_det.setDrawMode(QSurface3DSeries.DrawFlag.DrawSurface)
        # Time coordinates:
        # REMEMBER: We are using negative time coordinate values to achieve the look of y-axis inversion:
        self.ydata_iso_det = np.array([[-self.t_min_us, -self.t_max_us],
                                       [-self.t_min_us, -self.t_max_us]])
        self.surface_widget_item.addSeries(self.surface_series_delay_matrix)

        # If an initial delay matrix is given, display it:
        if delay_matrix_initial_us is not None:
            self.new_delay_matrix(delay_matrix_initial_us)
        else:
            # No initial delay matrix given:
            self.surface_series_delay_matrix.setVisible(False)

        # Display the initial iso-t time:
        self.surface_widget_item.addSeries(self.surface_series_iso_time)
        self.new_iso_t_time(iso_t_time_initial_us)

        # Display the initial iso-gen plane:
        self.surface_widget_item.addSeries(self.surface_series_iso_gen)
        self.new_iso_gen_index(iso_gen_index_initial)

        # Display the initial iso-det plane:
        self.surface_widget_item.addSeries(self.surface_series_iso_det)
        self.new_iso_det_index(iso_det_index_initial)

        # Create checkboxes to control the visibility of the iso-planes:
        self.checkbox_visibility_iso_time_plane = QCheckBox()
        self.checkbox_visibility_iso_time_plane.setText('Iso-time plane')
        self.checkbox_visibility_iso_time_plane.setChecked(True)
        self.checkbox_visibility_iso_gen_plane = QCheckBox()
        self.checkbox_visibility_iso_gen_plane.setText('Iso-gen plane')
        self.checkbox_visibility_iso_gen_plane.setChecked(True)
        self.checkbox_visibility_iso_det_plane = QCheckBox()
        self.checkbox_visibility_iso_det_plane.setText('Iso-det plane')
        self.checkbox_visibility_iso_det_plane.setChecked(True)

        # Organise the visibility checkboxes into a vertical layout:
        layout_visibility_checkboxes = QVBoxLayout()
        layout_visibility_checkboxes.addWidget(self.checkbox_visibility_iso_time_plane)
        layout_visibility_checkboxes.addWidget(self.checkbox_visibility_iso_gen_plane)
        layout_visibility_checkboxes.addWidget(self.checkbox_visibility_iso_det_plane)

        # Place visibility checkboxes inside a groupbox:
        group_box = QGroupBox()
        group_box.setTitle('Show :')
        group_box.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        group_box.setLayout(layout_visibility_checkboxes)

        # Build layout:
        layout_vertical = QVBoxLayout()
        layout_vertical.addWidget(self.graph_area_widget)
        layout_vertical.addWidget(group_box)

        self.setLayout(layout_vertical)

        # Wire signals to slots:
        self.signal_iso_t_time_changed.connect(self.new_iso_t_time)
        self.signal_iso_gen_index_changed.connect(self.new_iso_gen_index)
        self.signal_iso_det_index_changed.connect(self.new_iso_det_index)
        self.signal_delay_matrix_changed.connect(self.new_delay_matrix)
        self.checkbox_visibility_iso_time_plane.checkStateChanged.connect(self.checkbox_iso_t_visibility_toggled)
        self.checkbox_visibility_iso_gen_plane.checkStateChanged.connect(self.checkbox_iso_gen_visibility_toggled)
        self.checkbox_visibility_iso_det_plane.checkStateChanged.connect(self.checkbox_iso_det_visibility_toggled)
        self.signal_full_matrix_changed.connect(self.new_axes_ranges)

    def closeEvent(self, event):
        # Disconnect all slots from main window signals:
        self.signal_iso_t_time_changed.disconnect(self.new_iso_t_time)
        self.signal_iso_gen_index_changed.disconnect(self.new_iso_gen_index)
        self.signal_iso_det_index_changed.disconnect(self.new_iso_det_index)
        self.signal_delay_matrix_changed.disconnect(self.new_delay_matrix)
        self.checkbox_visibility_iso_time_plane.checkStateChanged.disconnect(self.checkbox_iso_t_visibility_toggled)
        self.checkbox_visibility_iso_gen_plane.checkStateChanged.disconnect(self.checkbox_iso_gen_visibility_toggled)
        self.checkbox_visibility_iso_det_plane.checkStateChanged.disconnect(self.checkbox_iso_det_visibility_toggled)
        self.signal_full_matrix_changed.disconnect(self.new_axes_ranges)
        # Emit signal to tell main window that this window has closed:
        self.signal_closed.emit()
        # Call original closed method of QWidget class:
        super().closeEvent(event)

    def new_iso_t_time(self, time_us):
        # Update the data of the iso_t series:
        # REMEMBER: We are using negative time coordinate values to achieve the look of y-axis inversion:
        new_iso_t_data = np.ones((2, 2)) * -time_us
        self.surface_data_proxy_iso_time.resetArrayNp(0, (self.n_elements-1),
                                                      0, (self.n_elements-1), new_iso_t_data)

    def new_iso_gen_index(self, index_gen):
        # Update the data of the iso_gen surface series:
        self.surface_data_proxy_iso_gen.resetArrayNp(0, (self.n_elements-1),
                                                     index_gen, 0, self.ydata_iso_gen)

    def new_iso_det_index(self, index_det):
        # Update the data of the iso_det surface series:
        self.surface_data_proxy_iso_det.resetArrayNp(index_det, 0,
                                                     0, (self.n_elements-1), self.ydata_iso_det)

    def new_delay_matrix(self, delay_matrix_s):
        if delay_matrix_s.size == 0:
            # Empty array given.
            # Make delay matrix series invisible:
            self.surface_series_delay_matrix.setVisible(False)
        else:
            # Set the delay matrix as the surface data for the delay matrix series via the data proxy:
            # IMPORTANT: in order to get the appearance of the y-axis increasing downwards, we will invert the sign of
            # the delay values.
            # IMPORTANT: in order to display the numpy array data in an 'image-like' transposition, we must transpose
            # the delay matrix.  This will finally make the Qt x-axis represent the detection index, and the Qt z-axis
            # represent the generation index.
            # It seems that the resetArrayNp method of the surface data proxy will not accept numpy 'views', so a copy
            # must be made.
            # To render numpy maskedArrays, we must fill the masked values with NaN using np.ma.filled()
            delay_matrix_negative_transposed_us = np.ma.filled(np.transpose(-delay_matrix_s / 10**-6).copy(), np.nan)
            self.surface_data_proxy_delay_matrix.resetArrayNp(0, 1, 0, 1,
                                                              delay_matrix_negative_transposed_us)
            if not self.surface_series_delay_matrix.isVisible():
                # Make visible:
                self.surface_series_delay_matrix.setVisible(True)

    def checkbox_iso_t_visibility_toggled(self):
        if self.checkbox_visibility_iso_time_plane.isChecked():
            self.surface_series_iso_time.setVisible(True)
        else:
            self.surface_series_iso_time.setVisible(False)

    def checkbox_iso_gen_visibility_toggled(self):
        if self.checkbox_visibility_iso_gen_plane.isChecked():
            self.surface_series_iso_gen.setVisible(True)
        else:
            self.surface_series_iso_gen.setVisible(False)

    def checkbox_iso_det_visibility_toggled(self):
        if self.checkbox_visibility_iso_det_plane.isChecked():
            self.surface_series_iso_det.setVisible(True)
        else:
            self.surface_series_iso_det.setVisible(False)

    def new_axes_ranges(self, tuple_n_el_t_min_t_max):
        self.n_elements = tuple_n_el_t_min_t_max[0]
        self.t_min_us = tuple_n_el_t_min_t_max[1]
        self.t_max_us = tuple_n_el_t_min_t_max[2]
        self._y_axis.setRange(-self.t_max_us, -self.t_min_us)
        self._x_axis.setRange(0, (self.n_elements - 1))
        self._z_axis.setRange(0, (self.n_elements - 1))
        # Update plane extents:
        self.ydata_iso_gen = np.array([[-self.t_min_us, -self.t_min_us],
                                       [-self.t_max_us, -self.t_max_us]])
        self.ydata_iso_det = np.array([[-self.t_min_us, -self.t_max_us],
                                       [-self.t_min_us, -self.t_max_us]])
