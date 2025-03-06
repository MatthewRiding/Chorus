import pickle
import matplotlib

matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi, layout="constrained")
        self.ax = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)

        self.setParent(parent)

class MplCanvasCopycat(FigureCanvasQTAgg):
    def __init__(self, parent=None, fig_to_copy=None):
        self.fig = pickle.loads(pickle.dumps(fig_to_copy))
        # Assuming only one axis in the figure:
        self.ax = self.fig.axes[0]
        super(MplCanvasCopycat, self).__init__(self.fig)

        self.setParent(parent)
