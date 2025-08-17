import numpy as np
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QFrame, QLabel
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
import colorcet as cc

from classdefs.modqtmatplotlib import MplCanvas
from corevariables.moddelayplotparams import delay_plot_params_dict
from functions.modfindascanswithclosestdelays import find_a_scans_with_closest_delays
from classdefs.modblitmanager import BlitManager


class IsoTimePlotWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(IsoTimePlotWidget, self).__init__(*args, **kwargs)

        # Create an instance of the MplCanvas class:
        self.mpl_canvas = MplCanvas(self, width=4, height=4, dpi=100)

        # Set style elements:
        my_grey = '0.3'
        fontsize_labels = 8
        self.mpl_canvas.fig.patch.set_alpha(0.0)
        self.mpl_canvas.ax.patch.set_alpha(0.0)
        self.mpl_canvas.setStyleSheet("background-color:transparent;")
        self.mpl_canvas.ax.tick_params(color=my_grey, labelcolor=my_grey)
        self.mpl_canvas.ax.spines[:].set_edgecolor(my_grey)
        self.mpl_canvas.ax.set_xlabel('Generation index', fontsize=fontsize_labels)
        self.mpl_canvas.ax.set_ylabel('Detection index', fontsize=fontsize_labels)
        self.mpl_canvas.ax.xaxis.label.set_color(my_grey)
        self.mpl_canvas.ax.yaxis.label.set_color(my_grey)
        self.mpl_canvas.ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
        self.mpl_canvas.ax.tick_params(axis='both', which='major', labelsize=8, pad=1)
        self.mpl_canvas.ax.xaxis.set_label_position('top')
        self.mpl_canvas.ax.autoscale(enable=True, axis='both', tight=True)

        # Plot an image of zeros to update later:
        n_tx_initial = 64

        def empty_image_plot(**dict_kwargs):
            data_array = np.zeros([n_tx_initial, n_tx_initial])
            c_map = cc.m_CET_D7
            axes_image = self.mpl_canvas.ax.imshow(data_array, cmap=c_map, interpolation='nearest', aspect='equal',
                                                   **dict_kwargs)
            return axes_image

        self.axes_image = empty_image_plot()

        # Plot a line to mark the detection index being shown in the iso-det B-scan:
        self.det_line = self.mpl_canvas.ax.axhline(0, linestyle=(0, (6, 8)), linewidth=1, color=(1, 1, 1, 0.5))

        # Plot a line to mark the generation index being shown in the iso-gen B-scan:
        self.gen_line = self.mpl_canvas.ax.axvline(0, linestyle=(0, (6, 8)), linewidth=1, color=(1, 1, 1, 0.5))

        # Create an empty plot to use to highlight the A-scans whose delays are closest to the current slice time,
        # invisible for now:
        self.plotref_nearest_a_scans_line, = self.mpl_canvas.ax.plot([], [], visible=False, **delay_plot_params_dict)

        # Create the interactive matplotlib toolbar, passing the MplCanvas as the first parameter, then the parent (
        # self, the QWidget) as the second parameter:
        toolbar = NavigationToolbar(self.mpl_canvas, self)

        # Add the toolbar to a horizontal layout with a label to describe the plot:
        layout_title_and_tools = QHBoxLayout()
        layout_title_and_tools.setContentsMargins(0, 0, 0, 0)
        self.label_title = QLabel()
        self.label_title.setStyleSheet("font: 14pt Segoe UI")
        self.label_title.setText('  Iso-time  ')
        v_line = QFrame()
        v_line.setFrameShape(QFrame.Shape.VLine)
        v_line.setFrameShadow(QFrame.Shadow.Sunken)
        layout_title_and_tools.addWidget(self.label_title)
        layout_title_and_tools.addWidget(v_line)
        layout_title_and_tools.addWidget(toolbar)

        # Stack the h_layout and the MplCanvas into a vertical layout:
        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addLayout(layout_title_and_tools)
        layout.addWidget(self.mpl_canvas)

        # Apply this layout to the main widget:
        self.setLayout(layout)

        # Create a BlitManager instance to manage blitting:
        self.blit_manager = BlitManager(self.mpl_canvas, [self.axes_image,
                                                          self.det_line,
                                                          self.gen_line,
                                                          self.plotref_nearest_a_scans_line])

    def update_iso_time_slice_display(self, displacements_iso_time_slice_nm):
        self.axes_image.set_data(displacements_iso_time_slice_nm)

    def update_axes(self, n_tx):
        self.axes_image.set_extent((0, n_tx-1, n_tx-1, 0))

    def update_det_line(self, det_index):
        self.det_line.set_ydata([det_index, det_index])

    def update_gen_line(self, gen_index):
        self.gen_line.set_xdata([gen_index, gen_index])

    def update_nearest_a_scans(self, delay_matrix_s, time_viewing_us):
        # Perform the binary-erosion method to find the appropriate A-scans to highlight at this viewing time:
        gen_indices_closest, det_indices_closest = find_a_scans_with_closest_delays(delay_matrix_s, time_viewing_us)

        # Update the data of the delay line:
        self.plotref_nearest_a_scans_line.set_data(gen_indices_closest, det_indices_closest)

    def toggle_nearest_a_scans_visibility(self):
        if self.plotref_nearest_a_scans_line.get_visible():
            # The plot is visible: Turn it invisible:
            self.plotref_nearest_a_scans_line.set_visible(False)
        else:
            # The plot is invisible: Make it visible:
            self.plotref_nearest_a_scans_line.set_visible(True)

    def make_nearest_a_scans_visible(self):
        self.plotref_nearest_a_scans_line.set_visible(True)

    def clear_nearest_a_scan_highlights_and_hide(self):
        self.plotref_nearest_a_scans_line.set_data([], [])
        self.plotref_nearest_a_scans_line.set_visible(False)
