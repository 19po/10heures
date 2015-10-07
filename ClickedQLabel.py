#-*-coding: utf-8-*-

from PyQt4 import QtGui, QtCore

class ClickedQLabel(QtGui.QLabel): 
	
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


