#-*-coding: utf-8-*-

from FillListWidgets import FillListWidgets
from Menu import Menu
from ClickedQLabel import DoubleClickedQLabel, ReleaseClickedQLabel

import sys, webbrowser#, os
from PyQt4 import QtGui, QtCore, QtWebKit


class MainUI(QtGui.QMainWindow):
	
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
			
	# widgets

		centralWidget = QtGui.QWidget()
		centralWidget.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Ignored)
		self.setCentralWidget(centralWidget)
		
		self.searchLabel = QtGui.QLabel()
		self.searchLabel.setText('Search')
		
		self.searchEdit = QtGui.QLineEdit()
		self.searchEdit.setMinimumWidth(250)
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
		
		#--------icon-------------
		
		self.timer = QtCore.QTimer()
		self.timer.start(10)	# stan początkowy, pierwsze wywołanie timera
		
		self.iconLabel = DoubleClickedQLabel(self)
		self.iconLabel.setToolTip('deezer profile')
		pixmap = QtGui.QPixmap('icon.ico')
		self.iconLabel.setPixmap(pixmap)
		self.iconLabel.setAlignment(QtCore.Qt.AlignRight)
		
		# Create the QML user interface.
		#self.iconLabel = QtDeclarative.QDeclarativeView()
		#self.iconLabel.setToolTip('deezer.com')
		#self.iconLabel.setSource(QtCore.QUrl('icon.qml')) # wczytanie pliku qml
		#self.iconLabel.setResizeMode(QtDeclarative.QDeclarativeView.SizeViewToRootObject)
	
		#----------------classic palyer-----------------
		
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
			
	# window geometry
		
		self.w = 800
		self.h = 300 
		self.setGeometry(300, 300, self.w, self.h)
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
		subLayout_2.addWidget(self.classicLabel, 4, 1, 1, 3)
		subLayout_2.addWidget(self.hideBottomPanelButton, 5, 1, 1, 1)
		subLayout_2.addWidget(self.showBottomPanelButton, 5, 1, 1, 1)
		
		grid = QtGui.QGridLayout()
		grid.addWidget(self.iconLabel, 1, 1, 1, 1, QtCore.Qt.AlignRight)
		grid.addLayout(subLayout_1, 1, 1, 1, 1, QtCore.Qt.AlignLeft)
		grid.addLayout(subLayout_2, 2, 1, 1, 1)
		centralWidget.setLayout(grid)

	#---------------------deezer icon--------------------
		
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
			
			url = "http://www.deezer.com/"
			webbrowser.open(str(url), new=1, autoraise=True)
		else:
			pixmap = QtGui.QPixmap('icon.ico')
			self.iconLabel.setPixmap(pixmap)	
	
	#---------------------classic player--------------------
	
	def showBottomPanel(self):
		
		self.classicLabel.show()
		self.classicWebView.show()
		self.hideBottomPanelButton.show()
		
		self.classicWebView.resize(self.classicLabel.width(), self.classicLabel.height())
		
		self.animation = QtCore.QPropertyAnimation(self, "geometry")
		self.animation.setDuration(200)
		self.animation.setStartValue(QtCore.QRect(self.geometry().x(), self.geometry().y(),
									 self.width(), self.height()))
		self.animation.setEndValue(QtCore.QRect(self.geometry().x(), self.geometry().y(),
									self.width(), 700))
		self.animation.start()
			
	def hideBottomPanel(self):
		
		self.classicLabel.hide()
		
		self.animation = QtCore.QPropertyAnimation(self, "geometry")
		self.animation.setDuration(500)
		self.animation.setStartValue(QtCore.QRect(self.geometry().x(), self.geometry().y(),
									 self.width(), self.height()))
		self.animation.setEasingCurve(QtCore.QEasingCurve.OutBack)
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


