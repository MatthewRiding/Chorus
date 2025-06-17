import numpy as np
from PySide6.QtWidgets import QVBoxLayout, QWidget

from classdefs.modqtmatplotlib import MplCanvas
from functions.modgetcheckerboardarray import get_checkerboard_array


class TFMGridPreviewWidget(QWidget):
    """A class used in the TFM parameters dialog to visualise the TFM grid relative to the linear, periodic array."""

    def __init__(self, n_tx, grid_width_x_default_mm, z_max_default_mm, n_pixels_z_default, *args, **kwargs):
        super(TFMGridPreviewWidget, self).__init__(*args, **kwargs)

        # Define instance variables, with default values:
        self.n_elements = n_tx

        # Create an instance of the MplCanvas class:
        self.mpl_canvas = MplCanvas(self, width=5, height=4, dpi=100)

        # Set style elements:
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

        # Plot an image of zeros to update later:
        def im_checkerboard(**dict_kwargs):
            checkerboard_array = get_checkerboard_array(grid_width_x_default_mm, z_max_default_mm,
                                                        n_pixels_z_default)
            c_map = 'viridis'
            extent = (-grid_width_x_default_mm/2, grid_width_x_default_mm/2, z_max_default_mm, 0)
            axes_image = self.mpl_canvas.ax.imshow(checkerboard_array, vmin=0, vmax=1, cmap=c_map,
                                                   interpolation='nearest', extent=extent, **dict_kwargs)
            return axes_image

        self.im_checkerboard = im_checkerboard()

        # Plot a set of points representing the array elements at the top of the axes:
        def default_array_plot():
            aperture_mm = 10
            x_elements_mm = np.linspace(0, aperture_mm, self.n_elements, endpoint=True) - (aperture_mm / 2)
            z_elements_mm = np.zeros(self.n_elements)
            line_array_elements, = self.mpl_canvas.ax.plot(x_elements_mm, z_elements_mm, ls='none', marker='s',
                                                           mec='none', mfc='magenta', markersize=2)
            return line_array_elements

        self.line_array_elements = default_array_plot()

        # Set the MplCanvas into a vertical layout:
        layout = QVBoxLayout()
        layout.addWidget(self.mpl_canvas)

        # Apply this layout to the main widget:
        self.setLayout(layout)

    def update_array_pitch(self, pitch_mm):
        aperture_mm = (self.n_elements - 1) * pitch_mm
        x_elements_mm = np.linspace(0, aperture_mm, self.n_elements, endpoint=True) - (aperture_mm / 2)
        self.line_array_elements.set_xdata(x_elements_mm)
        # Re-draw:
        self.mpl_canvas.draw()


    def update_checkerboard(self, grid_width_x_mm, grid_height_z_mm, n_pixels_z):
        checkerboard_array = get_checkerboard_array(grid_width_x_mm, grid_height_z_mm,
                                                    n_pixels_z)
        self.im_checkerboard.set_data(checkerboard_array)
        extent = (-grid_width_x_mm/2, grid_width_x_mm/2, grid_height_z_mm, 0)
        self.im_checkerboard.set_extent(extent)
        self.mpl_canvas.draw()
