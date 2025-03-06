import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT, FigureCanvasQTAgg
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.figure import Figure
import numpy as np


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self):
        # Before calling a super method, we first need to make a Matplotlib figure to pass as an argument to the
        # constructor of the superclass 'FigureCanvasQTAgg':
        self.fig = Figure(layout="constrained")
        self.ax = self.fig.add_subplot(111)
        super().__init__(self.fig)


class MplWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create an instance of the MplCanvas class:
        self.mpl_canvas = MplCanvas()

        # Plot an image:
        data_array = np.zeros([64, 64])
        axes_image = self.mpl_canvas.ax.imshow(data_array, interpolation='nearest', aspect='equal')

        # Create a toolbar instance:
        tool_bar = NavigationToolbar2QT(self.mpl_canvas)

        # Create a vertical layout, add the toolbar & canvas, then set the vertical layout as the layout for the
        # parent widget:
        layout = QVBoxLayout()
        layout.addWidget(tool_bar)
        layout.addWidget(self.mpl_canvas)
        self.setLayout(layout)

        # Customise MplCanvas instance:
        self.mpl_canvas.ax.set_xlabel('Generation index')
        self.mpl_canvas.ax.set_ylabel('Time (μs)')
        self.mpl_canvas.ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
        self.mpl_canvas.ax.xaxis.set_label_position('top')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MplWidget()
    window.show()
    app.exec()
