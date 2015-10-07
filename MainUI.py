#-*-coding: utf-8-*-

from ArtistList import ArtistList
from Menu import Menu
from ClickedQLabel import ClickedQLabel

import sys
from PyQt4 import QtGui, QtCore, QtDeclarative, QtWebKit

from functools import partial

class MainUI(QtGui.QMainWindow):
	
	def __init__(self, parent = None):
	
		super(MainUI, self).__init__(parent)
		self.setupUI()
		Menu(self)
		ArtistList(self)
		self.timer.timeout.connect(self.hoverButton)
		self.iconLabel.signalDoubleClick.connect(self.clickButton)
		
		#self.connect(self.iconLabel, QtCore.SIGNAL('clicked()'), self.openUrl)
		#self.connect(self.iconLabel, QtCore.SIGNAL('clicked()'), self.openUrl)
		
	def setupUI(self):
			
	# widgets
		
		centralWidget = QtGui.QWidget()
		self.setCentralWidget(centralWidget)
	
		self.searchLabel = QtGui.QLabel()
		self.searchLabel.setText('Search')
		
		self.searchEdit = QtGui.QLineEdit()
		self.searchEdit.setMinimumWidth(300)
		self.searchEdit.setToolTip('Enter artist name, and press Enter')
		
		self.artList = QtGui.QListWidget()
		self.artList.setToolTip('Choose the artist')

		self.albList = QtGui.QListWidget()
		self.albList.setToolTip('Choose the album')
		
		self.sngList = QtGui.QListWidget()
		self.sngList.setToolTip('Choose the song')
		
		self.artistLabel = QtGui.QLabel()
		self.artistLabel.setText('Artist')
		
		self.albumLabel = QtGui.QLabel()
		self.albumLabel.setText('Album')
		
		self.songLabel = QtGui.QLabel()
		self.songLabel.setText('Song')
		
		self.hLine = QtGui.QFrame()
		self.hLine.setFrameShape(QtGui.QFrame.HLine)
		self.hLine.setFrameShadow(QtGui.QFrame.Sunken)
		
		self.timer = QtCore.QTimer()
		self.timer.start(10)	# stan początkowy, pierwsze wywołanie timera
		
		self.iconLabel = ClickedQLabel(self)
		self.iconLabel.setToolTip('deezer profile')
		pixmap = QtGui.QPixmap('icon.ico')
		self.iconLabel.setPixmap(pixmap)
		self.iconLabel.setAlignment(QtCore.Qt.AlignRight)
		
		# Create the QML user interface.
		#self.iconLabel = QtDeclarative.QDeclarativeView()
		#self.iconLabel.setToolTip('deezer.com')
		#self.iconLabel.setSource(QtCore.QUrl('icon.qml')) # wczytanie pliku qml
		#self.iconLabel.setResizeMode(QtDeclarative.QDeclarativeView.SizeViewToRootObject)
	
		#self.classicLabel = QtGui.QLabel()
		#self.classicHtml = QtWebKit.QWebView(self.classicLabel)
		#self.classicHtml.setMaximumSize(QtCore.QSize(520, 250))
		#classicUrl = "http://www.deezer.com/plugins/player?format=classic&autoplay=false&playlist=true&width=520&height=250&color=1990DB&layout=dark&size=medium&type=playlist&id=30595446&title=&app_id=1"
		#self.classicHtml.setUrl(QtCore.QUrl(classicUrl)) #default page
	
		#self.squareLabel = QtGui.QLabel()
		#self.squareHtml = QtWebKit.QWebView(self.squareLabel)
		#self.squareHtml.setMaximumSize(QtCore.QSize(250, 250))
		#squareUrl = "http://www.deezer.com/plugins/player?format=square&autoplay=false&playlist=true&width=250&height=250&color=1990DB&layout=dark&size=medium&type=playlist&id=30595446&title=&app_id=1"
		#self.squareHtml.setUrl(QtCore.QUrl(squareUrl)) #default page
		
		#self.hideButtonR = QtGui.QPushButton()
		#self.hideButtonR.setText('<<')
		#self.hideButtonR.setFixedSize(15, 400)
		
	# window geometry
	
		self.setGeometry(300, 300, 800, 300)
		self.setWindowTitle('Deezer player 1.1')
		self.setWindowIcon(QtGui.QIcon('icon.ico'))
		#self.setStyleSheet('background-color: #343434')
	
	# grid layout
	
		subLayout_1 = QtGui.QGridLayout()
		subLayout_1.setSpacing(5)
		subLayout_1.addWidget(self.searchLabel, 1, 1, 1, 1, QtCore.Qt.AlignLeft)
		subLayout_1.addWidget(self.searchEdit, 1, 2, 1, 1, QtCore.Qt.AlignLeft)
		
		subLayout_2 = QtGui.QGridLayout()
		subLayout_2.setSpacing(5)
		subLayout_2.addWidget(self.hLine, 1, 1, 1, 3)
		subLayout_2.addWidget(self.artistLabel, 2, 1, 1, 1)
		subLayout_2.addWidget(self.albumLabel, 2, 2, 1, 1)
		subLayout_2.addWidget(self.songLabel, 2, 3, 1, 1)
		subLayout_2.addWidget(self.artList, 3, 1, 1, 1)
		subLayout_2.addWidget(self.albList, 3, 2, 1, 1)
		subLayout_2.addWidget(self.sngList, 3, 3, 1, 1)
		#subLayout_2.addWidget(self.classicLabel, 4, 1, 50, 3)
		#subLayout_2.addWidget(self.squareLabel, 3, 5, 50, 50)
		#subLayout_2.addWidget(self.hideButtonR, 3, 4, 50, 1)
		
		grid = QtGui.QGridLayout()
		grid.addWidget(self.iconLabel, 1, 1, 1, 1, QtCore.Qt.AlignRight)
		grid.addLayout(subLayout_1, 1, 1, 1, 1, QtCore.Qt.AlignLeft)
		grid.addLayout(subLayout_2, 2, 1, 1, 1)
		centralWidget.setLayout(grid)   

	def openUrl(self):
		#url = QtCore.QUrl('http://www.deezer.com/profile/511519725')
		url = QtCore.QUrl('http://www.deezer.com/plugins/player?format=square&autoplay=false&playlist=true&width=700&height=290&color=1990DB&layout=dark&size=medium&type=playlist&id=30595446&title=&app_id=1')
		self.squareHtml.load(url)
		self.squareHtml.show()
		
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
		else:
			pixmap = QtGui.QPixmap('icon.ico')
			self.iconLabel.setPixmap(pixmap)


