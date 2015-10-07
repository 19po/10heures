#-*-coding: utf-8-*-

from PyQt4 import QtGui, QtCore

class Menu(object):
	def __init__(self, MainUI):
		
		self.menu(MainUI)
		
	def menu(self, MainUI):
	
		menuBar = MainUI.menuBar()
		menuMenu = menuBar.addMenu('&Menu')
		
		menuHistory = menuMenu.addMenu('History')
		todayAction = QtGui.QAction('Today', MainUI)
		menuHistory.addAction(todayAction)
		monthAction = QtGui.QAction('Month', MainUI)
		menuHistory.addAction(monthAction)
		yearAction = QtGui.QAction('Year', MainUI)
		menuHistory.addAction(yearAction)
		
		menuStat = menuMenu.addMenu('Statistics')
		favouritesAction = QtGui.QAction('Favourites', MainUI)
		menuStat.addAction(favouritesAction)

		closeAction = QtGui.QAction('Close', MainUI)
		closeAction.setShortcut('Ctrl+Q')
		menuMenu.addAction(closeAction)
		closeAction.triggered.connect(MainUI.close)

