from PySide6.QtCore import QRunnable, Slot
import traceback
import sys
import uuid

from classdefs.modtfmworkersignals import TFMWorkerSignals
from functions.modcomputetfmcomplex import compute_tfm_complex


class TFMWorker(QRunnable):
    """
    A worker class inheriting QRunnable to be used in the Qt parallel processing system by 'starting' in a QThreadpool.
    Method 'run' computes a complex TFM intensity image using the given FullMatrix and TFMConstructor.
    This class emits 'result' and 'finished' signals after parallel processing.
    """
    def __init__(self, full_matrix, tfm_constructor):
        super(TFMWorker, self).__init__()

        self.full_matrix = full_matrix
        self.tfm_constructor = tfm_constructor

        # Generate a unique worker ID for this instance using the Python uuid module:
        # We will save the id as an instance variable in the form of a 32-element hexadecimal string.
        self.worker_id = uuid.uuid4().hex

        # Get the Qt signals needed for the TFM function and this runnable to transmit data back to the main GUI:
        self.signals = TFMWorkerSignals()

    @Slot()
    def run(self):
        """Calls the function 'compute_tfm_complex', passing the FullMatrix and TFMConstructor attached to this instance."""
        # Retrieve args/kwargs here; and fire processing using them
        try:
            # Run the generic TFM function, feeding it the specific delay law function that has been selected by the
            # user:
            intensity_image_complex, fmc_3d_filtered = compute_tfm_complex(self.worker_id, self.full_matrix,
                                                                           self.tfm_constructor, self.signals.progress)
        except:
            traceback.print_exc()
            # Get the Python error tuple:
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            # The 'compute_TFM' function ran successfully.
            # Use the 'result' signal to transmit the TFM image back to the main GUI:
            self.signals.result.emit((self.worker_id, intensity_image_complex, fmc_3d_filtered))
        finally:
            # After transmitting the result back to the main GUI, emit the 'finished' signal:
            self.signals.finished.emit(self.worker_id)
