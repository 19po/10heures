__author__ = 'postrowski'
# -*-coding: utf-8-*-

import sys
from PyQt4 import QtGui

from MainUI import MainUI

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec_()
    sys.exit()
