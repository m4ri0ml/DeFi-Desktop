import sys
import time
from PyQt5 import QtCore, QtGui, QtWidgets     # + QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtCore    import QTimer, Qt
from PyQt5.QtGui import QIcon, QPixmap


def splash_screen():
    app = QApplication(sys.argv)

    label = QLabel()
    pixmap = QPixmap('static/images/defibackground.jpg')
    label.setPixmap(pixmap)

    # SplashScreen - Indicates that the window is a splash screen. This is the default type for .QSplashScreen
    # FramelessWindowHint - Creates a borderless window. The user cannot move or resize the borderless window through the window system.
    label.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
    label.show()

    # Automatically exit after  5 seconds
    QTimer.singleShot(5000, app.quit) 
    app.exec_()