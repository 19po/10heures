#-*-coding: utf-8-*-

import sys
from MainUI import MainUI
from PyQt4 import QtGui, QtCore

if __name__ == '__main__':

	app = QtGui.QApplication(sys.argv)
	ui = MainUI()
	ui.show()
	app.exec_()
	sys.exit()

