import numpy as np
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QLabel, QFrame
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
import colorcet as cc

from classdefs.modqtmatplotlib import MplCanvas
from corevariables.moddelayplotparams import delay_plot_params_dict
from classdefs.modblitmanager import BlitManager


class BScanViewWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(BScanViewWidget, self).__init__(*args, **kwargs)

        # Create an instance of the MplCanvas class:
        self.mpl_canvas = MplCanvas(parent=self, width=4, height=2, dpi=100)

        # Create the interactive matplotlib toolbar, passing the MplCanvas as the first parameter, then the parent (
        # self, the QWidget) as the second parameter:
        toolbar = NavigationToolbar(self.mpl_canvas, self)

        # Add the toolbar to a horizontal layout with a label to describe the plot:
        layout_title_and_tools = QHBoxLayout()
        layout_title_and_tools.setContentsMargins(0, 0, 0, 0)
        self.label_title = QLabel()
        self.label_title.setStyleSheet("font: 14pt Segoe UI")
        v_line = QFrame()
        v_line.setFrameShape(QFrame.Shape.VLine)
        v_line.setFrameShadow(QFrame.Shadow.Sunken)
        layout_title_and_tools.addWidget(self.label_title)
        layout_title_and_tools.addWidget(v_line)
        layout_title_and_tools.addWidget(toolbar)

        # Stack the h layout and the MplCanvas into a vertical layout:
        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addLayout(layout_title_and_tools)
        layout.addWidget(self.mpl_canvas)
        self.setLayout(layout)

        # Set style elements:
        my_grey = '0.3'
        fontsize_labels = 8
        self.mpl_canvas.fig.patch.set_alpha(0.0)
        self.mpl_canvas.ax.patch.set_alpha(0.0)
        self.mpl_canvas.setStyleSheet("background-color:transparent;")
        self.mpl_canvas.ax.tick_params(color=my_grey, labelcolor=my_grey)
        self.mpl_canvas.ax.spines[:].set_edgecolor(my_grey)
        self.mpl_canvas.ax.set_xlabel('Generation index', fontsize=fontsize_labels)
        self.mpl_canvas.ax.set_ylabel('Time (μs)', fontsize=fontsize_labels)
        self.mpl_canvas.ax.xaxis.label.set_color(my_grey)
        self.mpl_canvas.ax.yaxis.label.set_color(my_grey)
        self.mpl_canvas.ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
        self.mpl_canvas.ax.tick_params(axis='both', which='major', labelsize=8, pad=1)
        self.mpl_canvas.ax.xaxis.set_label_position('top')
        self.mpl_canvas.ax.autoscale(enable=True, axis='both', tight=True)

        # Plot an image of zeros to update later:
        def empty_image_plot(**dict_kwargs):
            data_array = np.zeros([10, 10])
            c_map = cc.m_CET_D7
            axes_image = self.mpl_canvas.ax.imshow(data_array, cmap=c_map, interpolation='nearest', aspect='auto', **dict_kwargs)
            return axes_image

        self.axes_image = empty_image_plot()

        # Plot an 'hline' to mark the time being shown in the iso-time plot:
        self.time_line = self.mpl_canvas.ax.axhline(0, linestyle=(0, (6, 8)), linewidth=1, color=(1, 1, 1, 0.5))

        # Plot an invisible line that will be updated to display the delay law for a selected pixel:
        self.plotref_delay_line, = self.mpl_canvas.ax.plot([], [], visible=False, **delay_plot_params_dict)

        # Implement matplotlib figure event handling to enable pixel selection:
        # Connect the method 'motion_hover' to the 'motion_notify_event' in the MatPlotLib event handler:
        # self.mpl_canvas.fig.canvas.mpl_connect('motion_notify_event', self.motion_hover)

        # Create a BlitManager instance to manage blitting:
        self.blit_manager = BlitManager(self.mpl_canvas, [self.axes_image,
                                                          self.time_line,
                                                          self.plotref_delay_line])

    def motion_hover(self, event):
        # MatPlotLib mouse motion event response:
        if event.inaxes == self.mpl_canvas.ax:
            print(round(event.xdata), round(event.ydata))

    def update_b_scan_display(self, displacements_b_scan_nm):
        # Display new B-scan displacements on the plot:
        self.axes_image.set_data(displacements_b_scan_nm)

    def update_axes(self, n_tx, t_min, t_max):
        # Set image extent:
        self.axes_image.set_extent((0, n_tx-1, t_max, t_min))
        # Set delay line x_data:
        element_indices_vector = np.arange(n_tx)
        self.plotref_delay_line.set_xdata(element_indices_vector)

    def update_time_line(self, time_us):
        self.time_line.set_ydata([time_us])

    def update_delays(self, delays_vector_s):
        self.plotref_delay_line.set_ydata(delays_vector_s / 10**-6)

    def toggle_delay_visibility(self):
        if self.plotref_delay_line.get_visible():
            # The delay is visible: Make it invisible:
            self.plotref_delay_line.set_visible(False)
        else:
            # The delay is invisible: Make it visible:
            self.plotref_delay_line.set_visible(True)

    def clear_delay_times_and_hide(self):
        self.plotref_delay_line.set_ydata([])
        self.plotref_delay_line.set_visible(False)

    def make_delays_visible(self):
        self.plotref_delay_line.set_visible(True)
