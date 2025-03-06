from PySide6.QtWidgets import QVBoxLayout, QWidget
import colorcet as cc
import numpy as np
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar

from classdefs.modqtmatplotlib import MplCanvas
from classdefs.modblitmanager import BlitManager


class PCMWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(PCMWidget, self).__init__(*args, **kwargs)

        # Create an instance of the MplCanvas class:
        self.mpl_canvas = MplCanvas(self, width=4, height=4, dpi=100)

        # Set style elements:
        # Set the axes to 'equal' to maintain an equal aspect ratio:
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
        def empty_image_plot(**dict_kwargs):
            data_array = np.zeros([64, 64])
            c_map = cc.m_CET_D7
            axes_image = self.mpl_canvas.ax.imshow(data_array, cmap=c_map, interpolation='nearest', **dict_kwargs)
            return axes_image

        self.axes_image = empty_image_plot()

        # Create two empty line plots, to be used to mark the generation elements at the critical angle relative to
        # the selected pixel:
        def empty_crit_line_plot():
            line_plotref = self.mpl_canvas.ax.axvline(0, linestyle='dashed', linewidth=1, color='k', visible=False)
            return line_plotref
        self.crit_angle_line_lower = empty_crit_line_plot()
        self.crit_angle_line_upper = empty_crit_line_plot()

        # Create a pair of empty vlines to highlight the 'mouse angle' selected interactively by the user:
        def empty_mouse_angle_line_plot():
            line_plotref = self.mpl_canvas.ax.axvline(x=0, linestyle='dashed', linewidth=1, color=[1, 1, 1],
                                                       visible=True)
            return line_plotref
        self.line_mouse_angle_lower = empty_mouse_angle_line_plot()
        self.line_mouse_angle_upper = empty_mouse_angle_line_plot()

        # Create the interactive matplotlib toolbar, passing the Mplcanvas as the first parameter, then the parent (
        # self, the QWidget) as the second parameter:
        toolbar = NavigationToolbar(self.mpl_canvas, self)

        # Stack the toolbar and the Mplcanvas into a vertical layout:
        layout = QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(self.mpl_canvas)

        # Apply this layout to the main widget:
        self.setLayout(layout)

        # Create a BlitManager instance to allow blitting of the animated artists:
        self.blit_manager = BlitManager(self.mpl_canvas, [self.line_mouse_angle_lower,
                                                          self.line_mouse_angle_upper,
                                                          self.crit_angle_line_lower,
                                                          self.crit_angle_line_upper])

    def reposition_crit_angle_lines(self, gen_index_crit_lower, gen_index_crit_upper):
        self.crit_angle_line_lower.set_xdata([gen_index_crit_lower])
        self.crit_angle_line_upper.set_xdata([gen_index_crit_upper])

    def reposition_mouse_angle_lines(self, gen_index_lower, gen_index_upper):
        self.line_mouse_angle_lower.set_xdata([gen_index_lower])
        self.line_mouse_angle_upper.set_xdata([gen_index_upper])
