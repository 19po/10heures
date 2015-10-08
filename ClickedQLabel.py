#-*-coding: utf-8-*-

from PyQt4 import QtGui, QtCore

class DoubleClickedQLabel(QtGui.QLabel): 
	
	signalDoubleClick = QtCore.pyqtSignal()
	
	def mouseDoubleClickEvent(self, event):
		super(DoubleClickedQLabel, self).mouseDoubleClickEvent(event)
		self.signalDoubleClick.emit()
		
class ReleaseClickedQLabel(QtGui.QLabel): 
	
	signalReleaseClick = QtCore.pyqtSignal()
	
	def mouseReleaseEvent(self, event):
		super(ReleaseClickedQLabel, self).mouseReleaseEvent(event)
		self.signalReleaseClick.emit()

	#def buttonClicked(self):
	#	print('Deezer profile - open')
	#	QtGui.QDesktopServices.openUrl(QtCore.QUrl('http://www.google.com'))
	
	#def openUrl(self, MainUI):
	#	url = QtGui.QDesktopServices.openUrl(QtCore.QUrl('http://www.google.com'))
	#	MainUI.urlLabel.openExternalLinks(url)

