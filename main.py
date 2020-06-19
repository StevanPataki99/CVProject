from PySide2.QtWidgets import QApplication, QSplashScreen
from PySide2.QtGui import QPixmap
from customWidgets.main_window import MainWindow
import sys
import time


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pixmap = QPixmap("img/xlnk-transparent.png")
    splash = QSplashScreen(pixmap)
    splash.show()
    time.sleep(1)
    window = MainWindow()
    app.exec_()
    app.exit()
