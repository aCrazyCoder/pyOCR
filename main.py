# -*- coding: utf-8 -*-

# The main function


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import Qt
from implement import Implement

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QMainWindow()
    i = Implement(w)
    w.setWindowFlags(Qt.FramelessWindowHint)
    w.show()
    sys.exit(app.exec_())
