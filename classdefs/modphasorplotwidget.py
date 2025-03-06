from PySide6.QtWidgets import QWidget, QVBoxLayout
import numpy as np

from classdefs.modqtmatplotlib import MplCanvas


class PhasorPlotWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)

        # Create an instance of the MplCanvas class:
        self.mpl_canvas = MplCanvas(self, width=4, height=4, dpi=100)

        # Add it to a layout:
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.mpl_canvas)
        self.setLayout(self.layout)

        # # Clear the default axes and create polar axes:
        # self.mpl_canvas.fig.clf()
        # self.mpl_canvas.ax = self.mpl_canvas.fig.subplots(subplot_kw={'projection': 'polar'})

        # Set style elements:
        # Set the axes to 'equal' to maintain an equal aspect ratio:
        my_grey = '0.3'
        fontsize_labels = 8
        self.mpl_canvas.fig.patch.set_alpha(0.0)
        self.mpl_canvas.ax.patch.set_alpha(0.0)
        self.mpl_canvas.setStyleSheet("background-color:transparent;")
        self.mpl_canvas.ax.tick_params(color=my_grey, labelcolor=my_grey)
        self.mpl_canvas.ax.spines[:].set_edgecolor(my_grey)
        self.mpl_canvas.ax.set_xlabel('Real', fontsize=fontsize_labels)
        self.mpl_canvas.ax.set_ylabel('Imaginary', fontsize=fontsize_labels)
        self.mpl_canvas.ax.xaxis.label.set_color(my_grey)
        self.mpl_canvas.ax.axhline(color=my_grey)
        self.mpl_canvas.ax.axvline(color=my_grey)
        self.mpl_canvas.ax.yaxis.label.set_color(my_grey)
        self.mpl_canvas.ax.tick_params(axis='both', which='major', labelsize=8, pad=1)
        self.mpl_canvas.ax.autoscale(enable=True, axis='both', tight=True)
        self.mpl_canvas.ax.set_aspect('equal')

    def plot_phase_arrows(self, complex_numbers, colors, max_amp):
        # Use annotate to plot an arrow on the phasor for each complex sample:
        [self.mpl_canvas.ax.annotate("", xy=(np.real(z), np.imag(z)), xytext=(0, 0),
                                     arrowprops=dict(arrowstyle="->", color=color))
         for z, color in zip(complex_numbers, colors)]
        # Re-scale axes to fit:
        if max_amp == 0:
            self.mpl_canvas.ax.set_ylim(bottom=-1, top=1)
            self.mpl_canvas.ax.set_xlim(left=-1, right=1)
        else:
            self.mpl_canvas.ax.set_ylim(bottom=-max_amp, top=max_amp)
            self.mpl_canvas.ax.set_xlim(left=-max_amp, right=max_amp)

    def clear_plot(self):
        self.mpl_canvas.ax.clear()
        self.mpl_canvas.ax.patch.set_alpha(0.0)
