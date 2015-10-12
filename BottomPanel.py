#-*-coding: utf-8-*-

from PyQt4 import QtGui, QtCore

class BottomPanel(object):
	
	"""
	Bottom player methods.
	"""
	
	def showBottomPanel(self):

		self.classicLabel.show()
		self.classicWebView.show()
		self.hideBottomPanelButton.show()
		
		self.classicWebView.resize(self.classicLabel.width(), self.classicLabel.height())
				
	def hideBottomPanel(self):
		
		self.classicLabel.hide()
		
		self.animation = QtCore.QPropertyAnimation(self, "geometry")
		self.animation.setDuration(100)
		self.animation.setStartValue(QtCore.QRect(self.geometry().x(), self.geometry().y(),
									 self.width(), self.height()))
		self.animation.setEndValue(QtCore.QRect(self.geometry().x(), self.geometry().y(),
									self.width(), self.height()-self.classicLabel.height()))
		self.animation.start()
		
	def hideBottomPanelButtonClicked(self):
		
		self.hideBottomPanel()
		self.hideBottomPanelButton.hide()
		self.showBottomPanelButton.show()
		
	def showBottomPanelButtonClicked(self):
		
		self.showBottomPanel()
		self.hideBottomPanelButton.show()
		self.showBottomPanelButton.hide()
	
	def openClassicPlayer(self):
		
		self.showBottomPanel()
		classicPlayerUrl = "http://www.deezer.com/plugins/player?format=classic&autoplay=false&playlist=true&width=800&height=400&color=1990DB&layout=dark&size=medium&type=playlist&id=30595446&title=&app_id=1"
		self.classicWebView.setUrl(QtCore.QUrl(classicPlayerUrl))

