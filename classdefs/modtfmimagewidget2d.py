import numpy as np
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QFrame, QLabel
from PySide6.QtCore import Signal
from classdefs.modmytoolbar import MyToolBar

from classdefs.modqtmatplotlib import MplCanvas
from classdefs.modblitmanager import BlitManager
from qtdesigner.dialogs.moddialogprettyprint import DialogPrettyPrint
from classdefs.modtfmconstructor import TFMConstructor


class TFMImageWidget2D(QWidget):
    # Define custom signals:
    pixel_clicked = Signal(tuple)

    def __init__(self, *args, **kwargs):
        super(TFMImageWidget2D, self).__init__(*args, **kwargs)

        # Define instance variables:
        # self.tfm_constructor = TFMConstructor('Placeholder image name',
        #                                       None,
        #                                       None,
        #                                       None,
        #                                       '',
        #                                       None,
        #                                       None,
        #                                       None,
        #                                       None,
        #                                       None,
        #                                       0,
        #                                       0,
        #                                       None,
        #                                       None,
        #                                       '')
        self.tfm_constructor = None

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
        def empty_image_plot(**dict_kwargs):
            data_array = np.zeros([200, 300])
            c_map = 'viridis'
            axes_image = self.mpl_canvas.ax.imshow(data_array, vmin=0, vmax=0, cmap=c_map, interpolation='nearest',
                                                   **dict_kwargs)
            return axes_image

        self.axes_image = empty_image_plot()

        # Create an empty plot that will mark the selected pixel:
        self.plotref_selected_pixel, = self.mpl_canvas.ax.plot([], [],
                                                               markeredgewidth=0,
                                                               markersize=6,
                                                               color=[1, 1, 1],
                                                               linestyle='None',
                                                               marker=6)

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
        layout = QVBoxLayout()
        layout.addLayout(layout_title_and_tools)
        layout.addWidget(self.mpl_canvas)

        # Apply this layout to the main widget:
        self.setLayout(layout)

        # Connect to the 'button_press_event':
        self.mpl_canvas.fig.canvas.mpl_connect('button_press_event', self.button_press_response)

        # Create an instance of BlitManager to manage blitting:
        self.blit_manager = BlitManager(self.mpl_canvas, [self.axes_image,
                                                          self.plotref_selected_pixel])

    def button_press_response(self, event):
        # Plot the white caret marker at the location that has been clicked:
        self.plotref_selected_pixel.set_data([event.xdata], [event.ydata])
        self.blit_manager.blit_all_animated_artists()

        # Emit the 'pixel_clicked' event to prompt the B-scan and iso-t widgets to display the associated delay law:
        x_coord_m = event.xdata * 10 ** -3
        z_coord_m = event.ydata * 10 ** -3
        self.pixel_clicked.emit((x_coord_m, z_coord_m))

    def update_axes_centred(self, grid_size_x_mm, grid_size_z_mm):
        # Set axis limits to reflect the size of the chosen TFM grid:
        self.axes_image.set_extent((-grid_size_x_mm / 2, grid_size_x_mm / 2, grid_size_z_mm, 0))

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
                                                title_string=self.tfm_constructor.image_name_string)
        dialog_pretty_print.exec()
