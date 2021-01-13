from main_window import *
from splash_screen import *
import os 
import sys

if __name__ == '__main__':
	splash_screen()
	app = QApplication(sys.argv) 
	app.setApplicationName("DeFi-Desktop")

	window = MainWindow()
	app.exec_()