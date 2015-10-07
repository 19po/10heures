#-*-coding: utf-8-*-

from PyQt4 import QtGui, QtCore

class IconClicked(QtGui.QLabel): 
	
	signalDoubleClick = QtCore.pyqtSignal()
		
	def mouseDoubleClickEvent(self, e): 
		sig = self.emit(QtCore.SIGNAL('clicked()'))
		sig = self.signalDoubleClick.emit()
	

	#def buttonClicked(self):
	#	print('Deezer profile - open')
	#	QtGui.QDesktopServices.openUrl(QtCore.QUrl('http://www.google.com'))
	
	#def openUrl(self, MainUI):
	#	url = QtGui.QDesktopServices.openUrl(QtCore.QUrl('http://www.google.com'))
	#	MainUI.urlLabel.openExternalLinks(url)

class Pixmapa():

	def __init__(self, MainUI):
		self.hoverButton(MainUI)
		self.clickButton(MainUI)
		
	def hoverButton(self, MainUI):
		if MainUI.iconLabel.underMouse() is True:
			self.timer.start(10)
			self.pixmap = QtGui.QPixmap('icon_hover.ico')
			MainUI.iconLabel.setPixmap(self.pixmap)
		else:
			self.pixmap = QtGui.QPixmap('icon.ico')
			MainUI.iconLabel.setPixmap(self.pixmap)
			
	def clickButton(self, MainUI):
		if MainUI.iconLabel.underMouse() is True:
			self.timer.start(200)
			self.pixmap = QtGui.QPixmap('icon_click.ico')
			MainUI.iconLabel.setPixmap(self.pixmap)
		else:
			self.pixmap = QtGui.QPixmap('icon.ico')
			MainUI.iconLabel.setPixmap(self.pixmap)

