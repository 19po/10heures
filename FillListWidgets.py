#-*-coding: utf-8-*-

from PyQt4 import QtGui, QtCore
#import ff

class FillListWidgets(object):
	
	def __init__(self, MainUI):
									# po utworzeniu instancji klasy w klasie parent:
		#self.ArtistList = []		# metoda setupArtList() może zostać wywołana w klasie parent
		self.setupArtList(MainUI)	# metoda setupArtList() zostanie wywołana w klasie parent
		self.setupSngList(MainUI)
		
	def setupArtList(self, MainUI):
		
		MainUI.artList.addItem("Item 1")
		MainUI.artList.addItem("Item 2")
	
	def setupSngList(self, MainUI):	
		MainUI.sngList.addItem("Item 3")
		
		#MainUI.artList.addItem("Item 3")
		#print('Wywołana z klasy MainUI:\ngłosi się klasa ArtistList')

