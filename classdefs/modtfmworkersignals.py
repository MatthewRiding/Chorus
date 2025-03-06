from PySide6.QtCore import QObject, Signal


class TFMWorkerSignals(QObject):
    # Create Qt signals as class variables for the WorkerSignals class:
    # Notice we are in the class definition level, not the __init__ constructor.
    # These are class variables, not instance variables.

    # The 'finished' signal returns the worker id (a hexadecimal string) only, so that the main GUI can show that the
    # associated worker has finished running.
    finished = Signal(str)

    # The 'result' signal will return:
    # 1. The worker ID.
    # 2. The finished TFM image.
    # These two objects will be returned as the elements of a tuple.
    result = Signal(tuple)

    # The 'progress' signal will transmit:
    # 1. A unique worker ID, to allow updates from a given worker instance to be distinguished from those from others.
    # 2. A string reporting progress for display in the main GUI.
    # These two objects will be returned as the elements of a tuple.
    progress = Signal(tuple)

    # We can define an 'error' signal to transmit Python Exception tuples to the main GUI:
    error = Signal(tuple)
