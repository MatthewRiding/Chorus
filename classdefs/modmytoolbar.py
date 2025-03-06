from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar


class MyToolBar(NavigationToolbar):
    def __init__(self, mpl_canvas, parent, slot_save=None):

        # Replace requested methods:
        if slot_save:
            self.save_figure = slot_save

        super().__init__(mpl_canvas, parent)
