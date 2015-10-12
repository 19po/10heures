#-*-coding: utf-8-*-

from PyQt4 import QtGui, QtCore
import webbrowser

class DeezerIcon(object):
		
	"""
	Deezer icon methods.
	"""
	
	def hoverButton(self):
		
		if self.iconLabel.underMouse() is True:
			self.timer.start(10)
			pixmap = QtGui.QPixmap('icon_hover.ico')
			self.iconLabel.setPixmap(pixmap)
		else:
			pixmap = QtGui.QPixmap('icon.ico')
			self.iconLabel.setPixmap(pixmap)
		
	def clickButton(self):
		
		if self.iconLabel.underMouse() is True:
			self.timer.start(200)
			pixmap = QtGui.QPixmap('icon_click.ico')
			self.iconLabel.setPixmap(pixmap)
			
			url = "http://www.deezer.com"
			webbrowser.open(str(url), new=1, autoraise=True)
		else:
			pixmap = QtGui.QPixmap('icon.ico')
			self.iconLabel.setPixmap(pixmap)	

