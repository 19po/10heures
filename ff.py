#-*-coding: utf-8-*-

from PyQt4 import QtGui, QtCore

class ff():

	def __init__(self, ArtistList):

		self.setupFf(ArtistList)
		
	def setupFf(self, ArtistList):
	
		ArtistList.artList.addItem("Item 3")
		print('Wywołana z klasy MainUI:\ngłosi się klasa ff')

