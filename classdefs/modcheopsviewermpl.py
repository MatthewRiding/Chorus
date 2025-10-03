from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Signal, Qt
import numpy as np
from matplotlib import colormaps

from classdefs.modqtmatplotlib import MplCanvas
from functions.modcreatetimeplanecoords import create_time_plane_coords
from functions.modcreatecheopsmesh import create_cheops_meshes


class CheopsViewer(QWidget):
    # Create signal as class attribute:
    cheops_viewer_closed = Signal()

    def __init__(self, n_tx, t_min_us, t_max_us, time_us, delay_matrix_s):
        super().__init__()

        self.time_us = time_us
        self.n_tx = n_tx
        self.pyramid_visible = False
        self.surf_cheops_pyramid = None

        # Set window title:
        self.setWindowTitle('Cheops viewer')

        # Set attributes:
        self.setAttribute(Qt.WA_DeleteOnClose)

        # Set window flags:
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        # Create an MplCanvas instance & set it into a layout:
        self.mpl_canvas = MplCanvas()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.mpl_canvas)
        self.setLayout(self.layout)

        # Create a 3D plot representing the full matrix:
        self.mpl_canvas.fig.clf()
        self.mpl_canvas.ax = self.mpl_canvas.fig.subplots(subplot_kw={"projection": "3d"})

        # Set the aspect ratio of the Axes3d:
        self.mpl_canvas.ax.set_box_aspect((1, 1, 2.5))

        # Customise mpl_canvas:
        my_grey = '0.3'
        fontsize_labels = 8
        self.mpl_canvas.fig.patch.set_alpha(0.0)
        self.mpl_canvas.ax.patch.set_alpha(0.0)
        self.mpl_canvas.setStyleSheet("background-color:transparent;")
        self.mpl_canvas.ax.tick_params(color=my_grey, labelcolor=my_grey)
        self.mpl_canvas.ax.spines[:].set_edgecolor(my_grey)
        self.mpl_canvas.ax.set_xlabel('Generation index', fontsize=fontsize_labels)
        self.mpl_canvas.ax.set_ylabel('Detection index', fontsize=fontsize_labels)
        self.mpl_canvas.ax.set_zlabel('Time (μs)', fontsize=fontsize_labels)
        self.mpl_canvas.ax.xaxis.label.set_color(my_grey)
        self.mpl_canvas.ax.yaxis.label.set_color(my_grey)
        self.mpl_canvas.ax.zaxis.label.set_color(my_grey)
        self.mpl_canvas.ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
        self.mpl_canvas.ax.tick_params(axis='both', which='major', labelsize=8, pad=1)

        # Plot a plane corresponding to the currently selected time:
        x_coords, y_coords, z_coords = create_time_plane_coords(n_tx, time_us)
        self.surf_time_plane = self.mpl_canvas.ax.plot_surface(x_coords, y_coords, z_coords, alpha=1, color='lime')

        if delay_matrix_s is None:
            # Create a flat Cheops plane but make it invisible:
            gen_indices_mesh, det_indices_mesh = create_cheops_meshes(self.n_tx)
            default_delay_surface = np.ones((self.n_tx, self.n_tx))
            self.surf_cheops_pyramid = self.mpl_canvas.ax.plot_surface(gen_indices_mesh, det_indices_mesh,
                                                                       default_delay_surface, visible=False)
        else:
            self.update_cheops_pyramid(delay_matrix_s)

        # Set axis limits:
        self.mpl_canvas.ax.set_xlim(0, n_tx - 1)
        self.mpl_canvas.ax.set_ylim(0, n_tx - 1)
        self.mpl_canvas.ax.set_zlim(t_min_us, t_max_us)

        # Invert z-axis:
        self.mpl_canvas.ax.invert_zaxis()
        # Invert y-axis for 'image-like' display:
        self.mpl_canvas.ax.invert_yaxis()

        # Set widget size:
        self.resize(470, 600)

    def closeEvent(self, event):
        self.cheops_viewer_closed.emit()
        super().closeEvent(event)

    def update_time_plane(self, time_us):
        self.time_us = time_us
        x_coords, y_coords, z_coords = create_time_plane_coords(self.n_tx, time_us)
        self.surf_time_plane.remove()
        self.surf_time_plane = self.mpl_canvas.ax.plot_surface(x_coords, y_coords, z_coords, alpha=1, color='lime')

    def update_axes(self, n_tx, t_min_us, t_max_us):
        self.n_tx = n_tx

        self.mpl_canvas.ax.set_xlim(0, n_tx - 1)
        self.mpl_canvas.ax.set_ylim(0, n_tx - 1)
        self.mpl_canvas.ax.set_zlim(t_max_us, t_min_us)

        # Re-size the plane marking the currently selected time:
        self.update_time_plane(self.time_us)

    def update_cheops_pyramid(self, delay_matrix_s):
        delay_matrix_us = delay_matrix_s / 10**-6
        if self.surf_cheops_pyramid:
            self.surf_cheops_pyramid.remove()
        gen_indices_mesh, det_indices_mesh = create_cheops_meshes(self.n_tx)
        self.surf_cheops_pyramid = self.mpl_canvas.ax.plot_surface(gen_indices_mesh, det_indices_mesh, delay_matrix_us,
                                                                   cmap=colormaps['Greys'])

    def hide_cheops_pyramid(self):
        self.surf_cheops_pyramid.set_visible(False)
