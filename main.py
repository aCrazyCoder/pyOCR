# -*- coding: utf-8 -*-

# The main function


import sys
from PyQt5.QtWidgets import QApplication
from mainInterface import mainInterface

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = mainInterface()
    w.show()
    sys.exit(app.exec_())
