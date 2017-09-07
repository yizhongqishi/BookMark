# /usr/bin/env python
# -*- coding : utf-8 -*-
import os
import sys
import time
from PyQt5 import QtGui

from PyQt5 import QtCore
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import *



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi()



    def setupUi(self):
        self.resize(1366, 768)
        self.setWindowState(Qt.WindowMaximized)

        mainlayout = QHBoxLayout()
        layout1 = QVBoxLayout()
        najiu

        self.setLayout(mainlayout)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())