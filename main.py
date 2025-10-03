import sys
from PySide6.QtWidgets import QApplication

from classdefs.modmainwindow import ChorusMainWindow

if __name__=='__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = ChorusMainWindow()
    window.show()
    app.exec()
