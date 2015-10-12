#-*-coding: utf-8-*-

from FillListWidgets import FillListWidgets
from Menu import Menu
from ClickedQLabel import DoubleClickedQLabel

from DeezerIcon import DeezerIcon
from BottomPanel import BottomPanel

import sys, webbrowser
from PyQt4 import QtGui, QtCore, QtWebKit

class MainUI(QtGui.QMainWindow, BottomPanel, DeezerIcon):
	
	def __init__(self, parent = None):
	
		super(MainUI, self).__init__(parent)
		self.setupUI()
		
		Menu(self)
		FillListWidgets(self)
		
		self.timer.timeout.connect(self.hoverButton)
		self.iconLabel.signalDoubleClick.connect(self.clickButton)
		
		self.artList.itemDoubleClicked.connect(self.openClassicPlayer)
		self.albList.itemDoubleClicked.connect(self.openClassicPlayer)
		self.sngList.itemDoubleClicked.connect(self.openClassicPlayer)
		
		self.hideBottomPanelButton.clicked.connect(self.hideBottomPanelButtonClicked)
		self.showBottomPanelButton.clicked.connect(self.showBottomPanelButtonClicked)
		
	def setupUI(self):
		
		centralWidget = QtGui.QWidget()
		self.setCentralWidget(centralWidget)
		
	#--------------------widgets-------------------
		
		#-----------------search-------------------
		
		self.searchLabel = QtGui.QLabel()
		self.searchLabel.setText('Search')
		
		self.searchButton = QtGui.QPushButton()
		self.searchButton.setText('Search')
		
		self.searchEdit = QtGui.QLineEdit()
		self.searchEdit.setMinimumWidth(250)
		self.searchEdit.setToolTip('Enter artist name, and press Enter')
		
		#-----------------list---------------------
		
		self.artList = QtGui.QListWidget()
		self.artList.setMinimumHeight(200)
		self.artList.setToolTip('Choose the artist')

		self.albList = QtGui.QListWidget()
		self.albList.setMinimumHeight(200)
		self.albList.setToolTip('Choose the album')
		
		self.sngList = QtGui.QListWidget()
		self.sngList.setMinimumHeight(200)
		self.sngList.setToolTip('Choose the song')
		
		#--------------list-label-----------------
		
		self.artistLabel = QtGui.QLabel()
		self.artistLabel.setText('Artist')
		
		self.albumLabel = QtGui.QLabel()
		self.albumLabel.setText('Album')
		
		self.songLabel = QtGui.QLabel()
		self.songLabel.setText('Song')
		
		#-------------horizontal-line--------------
		
		self.hLine = QtGui.QFrame()
		self.hLine.setFrameShape(QtGui.QFrame.HLine)
		self.hLine.setFrameShadow(QtGui.QFrame.Sunken)
		
		#--------------------icon------------------
		
		self.timer = QtCore.QTimer()
		self.timer.start(10)	# timer initial state
		
		self.iconLabel = DoubleClickedQLabel(self)
		self.iconLabel.setToolTip('deezer.com')
		pixmap = QtGui.QPixmap('icon.ico')
		self.iconLabel.setPixmap(pixmap)
		self.iconLabel.setAlignment(QtCore.Qt.AlignRight)
	
		#----------------classic-player------------
		
		self.classicLabel = QtGui.QLabel()
		self.classicLabel.setVisible(False)
		self.classicLabel.setMinimumHeight(400)
		self.classicWebView = QtWebKit.QWebView(self.classicLabel)
		self.classicWebView.settings().setAttribute(QtWebKit.QWebSettings.PluginsEnabled, True)
		self.classicWebView.setVisible(False)
	
		self.hideBottomPanelButton = QtGui.QPushButton()
		self.hideBottomPanelButton.setVisible(False)
		self.hideBottomPanelButton.setText('^')
		self.hideBottomPanelButton.setFixedSize(50, 20)
		
		self.showBottomPanelButton = QtGui.QPushButton()
		self.showBottomPanelButton.setVisible(False)
		self.showBottomPanelButton.setText('~')
		self.showBottomPanelButton.setFixedSize(50, 20)
			
	#----------------window-geometry--------------------
		
		self.setGeometry(300, 300, 800, 300)
		self.setWindowTitle('Deezer player 1.1')
		self.setWindowIcon(QtGui.QIcon('icon.ico'))
		#self.setStyleSheet('background-color: #343434')
	
	#------------------grid-layout-----------------------
	
		subLayout_1 = QtGui.QGridLayout()
		subLayout_1.setSpacing(5)
		subLayout_1.addWidget(self.searchLabel, 1, 1, 1, 1, QtCore.Qt.AlignLeft)
		subLayout_1.addWidget(self.searchEdit, 1, 2, 1, 1, QtCore.Qt.AlignLeft)
		subLayout_1.addWidget(self.searchButton, 1, 3, 1, 1, QtCore.Qt.AlignLeft)
		
		subLayout_2 = QtGui.QGridLayout()
		subLayout_2.setSpacing(5)
		subLayout_2.addWidget(self.hLine, 1, 1, 1, 3)
		subLayout_2.addWidget(self.artistLabel, 2, 1, 1, 1)
		subLayout_2.addWidget(self.albumLabel, 2, 2, 1, 1)
		subLayout_2.addWidget(self.songLabel, 2, 3, 1, 1)
		subLayout_2.addWidget(self.artList, 3, 1, 1, 1)
		subLayout_2.addWidget(self.albList, 3, 2, 1, 1)
		subLayout_2.addWidget(self.sngList, 3, 3, 1, 1)
		
		subLayout_3 = QtGui.QGridLayout()
		subLayout_3.setSpacing(5)
		subLayout_3.addWidget(self.classicLabel, 4, 1, 1, 3)
		subLayout_3.addWidget(self.hideBottomPanelButton, 5, 1, 1, 1)
		subLayout_3.addWidget(self.showBottomPanelButton, 5, 1, 1, 1)
		
		grid = QtGui.QGridLayout()
		grid.addWidget(self.iconLabel, 1, 1, 1, 1, QtCore.Qt.AlignRight)
		grid.addLayout(subLayout_1, 1, 1, 1, 1, QtCore.Qt.AlignLeft)
		grid.addLayout(subLayout_2, 2, 1, 1, 1)
		grid.addLayout(subLayout_3, 3, 1, 1, 1)
		centralWidget.setLayout(grid)


