from PySide6.QtCore import QAbstractListModel, Qt
from PySide6.QtGui import QIcon


class ListModelTFMImages(QAbstractListModel):
    def __init__(self):
        super().__init__()

        # Initialise the dictionary of listed images:
        # Each entry shall have a key of the worker_id, and a value equal to an instance of theListedTFMImage class.
        self.dict_listed_images = {}

        self.icon_processing = QIcon('graphicfiles/image_processing_amber.png')
        self.icon_completed = QIcon('graphicfiles/image_complete_green.png')

    def data(self, index, role):
        # Get the data for this ListedTFMImage:
        key = list(self.dict_listed_images.keys())[index.row()]
        listed_tfm_image = self.dict_listed_images[key]

        if role == Qt.DisplayRole:
            text = listed_tfm_image.get_display_string()
            return text

        if role == Qt.DecorationRole:
            if listed_tfm_image.complete:
                return self.icon_completed
            else:
                return self.icon_processing

    def rowCount(self, index):
        return len(self.dict_listed_images)
