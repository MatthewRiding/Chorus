from PySide6.QtWidgets import QWidget, QVBoxLayout
import numpy as np

from classdefs.modqtmatplotlib import MplCanvas
from classdefs.modblitmanager import BlitManager

class SumVSMaskAngleWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)

        # Create an instance of the MplCanvas class:
        self.mpl_canvas = MplCanvas(self, width=4, height=4, dpi=100)

        # Add it to a layout:
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.mpl_canvas)
        self.setLayout(self.layout)

        # Set style elements:
        my_grey = '0.3'
        fontsize_labels = 8
        self.mpl_canvas.fig.patch.set_color([0.1, 0.1, 0.1, 1])
        self.mpl_canvas.ax.patch.set_alpha(0.0)
        self.mpl_canvas.setStyleSheet("background-color:transparent;")
        self.mpl_canvas.ax.tick_params(color=my_grey, labelcolor=my_grey)
        self.mpl_canvas.ax.spines[:].set_edgecolor(my_grey)
        self.mpl_canvas.ax.set_xlabel('Mask angle (°)', fontsize=fontsize_labels)
        self.mpl_canvas.ax.set_ylabel('Placeholder y', fontsize=fontsize_labels)
        self.mpl_canvas.ax.xaxis.label.set_color(my_grey)
        self.mpl_canvas.ax.yaxis.label.set_color(my_grey)
        self.mpl_canvas.ax.axhline(color=my_grey)
        self.mpl_canvas.ax.tick_params(axis='both', which='major', labelsize=8, pad=1)
        self.mpl_canvas.ax.autoscale(enable=True, axis='both', tight=True)

        # Create a line plot for the cumulative amplitude:
        self.plotref_cumamp, = self.mpl_canvas.ax.plot([], [], color=[1, 1, 1], visible=False)
        # Create a line plot for the 1st derivative of the cumulative amplitude:
        self.plotref_derivative, = self.mpl_canvas.ax.plot([], [], color='cyan', visible=False)

        # Create a black dashed line to mark the critical angle:
        self.line_crit_angle = self.mpl_canvas.ax.axvline(0, linestyle='dashed', linewidth=1, color='k',
                                                          visible=False)

        # Create a white dashed line to mark the mouse angle:
        self.line_mouse_angle = self.mpl_canvas.ax.axvline(0, linestyle='dashed', linewidth=1, color=[1, 1, 1],
                                                           visible=True)

        # Create a text instance to display the mouse angle:
        self.text_mouse_angle = self.mpl_canvas.ax.text(0, 0, '', color=[1, 1, 1], fontsize=fontsize_labels,
                                                        va='bottom')

        # Create a BlitManager instance and add the vlines:
        self.blit_manager = BlitManager(self.mpl_canvas, [self.line_crit_angle,
                                                          self.line_mouse_angle,
                                                          self.text_mouse_angle])

    def update_data(self, gen_angles_ordered, cumsum, y_label):
        # Assign new data to line plot:
        self.plotref_cumamp.set_data(gen_angles_ordered, cumsum)
        # Update y-axis label depending on which sum type was used:
        self.mpl_canvas.ax.set_ylabel(y_label)
        # Calculate 1st derivative of new cumsum and send to derivative plotref:
        self.plotref_derivative.set_data(gen_angles_ordered, np.ediff1d(cumsum, to_begin=0))
        # Set lines as visible:
        self.plotref_cumamp.set_visible(True)
        self.plotref_derivative.set_visible(True)
        # Autoscale axes:
        self.mpl_canvas.ax.relim()
        self.mpl_canvas.ax.autoscale_view()

    def reposition_crit_angle_line(self, angle_critical_degrees):
        # Send data to line plot:
        self.line_crit_angle.set_xdata([angle_critical_degrees])

    def reposition_mouse_angle_line_and_text(self, mouse_angle_degrees):
        # Send data to line plot:
        self.line_mouse_angle.set_xdata([mouse_angle_degrees])
        # Send data to text:
        self.text_mouse_angle.set_x(mouse_angle_degrees)
        self.text_mouse_angle.set_text(f' {mouse_angle_degrees:.1f}°')
