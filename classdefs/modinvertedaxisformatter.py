from PySide6.QtGraphs import QValue3DAxisFormatter

class InvertedYAxisFormatter(QValue3DAxisFormatter):
    """
    Use this subclass of QValue3DAxisFormatter to overwrite the stringForValue method.  The new stringForValue
    method will flip the sign of the tick label relative to its actual numeric value.  This seems necessary to achieve
    the 'inverted' y-axis appearance and behaviour that I want.  The actual numeric time coordinates of all surfaces
    have had their signs inverted (so an event at 5us is plotted at -5us) but the axis labels have then also been sign
    inverted, giving the overall appearance of a reversed y-axis.
    """
    def __init__(self):
        super().__init__()

    def stringForValue(self, value, format_specifier):
        return f'{value * -1:.2f}'
