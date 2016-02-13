__author__ = 'postrowski'

# -*-coding: utf-8-*-

from PyQt4 import QtGui, QtCore, QtWebKit

from Menu import Menu
from ClickedQLabel import DoubleClickedQLabel
from DeezerIcon import DeezerIcon
from BottomPanel import BottomPanel
from Search import Search
from WaitOverlay import WaitOverlay

class MainUI(QtGui.QMainWindow, BottomPanel, DeezerIcon, Search):

    def __init__(self, parent=None):

        super(MainUI, self).__init__(parent)

        self.searchButton = QtGui.QPushButton()
        self.playButton = QtGui.QPushButton()
        self.showBottomPanelButton = QtGui.QPushButton()
        self.hideBottomPanelButton = QtGui.QPushButton()

        self.iconLabel = DoubleClickedQLabel(self)
        self.searchLabel = QtGui.QLabel()
        self.albumLabel = QtGui.QLabel()
        self.artistLabel = QtGui.QLabel()
        self.songLabel = QtGui.QLabel()

        self.songList = QtGui.QListWidget()
        self.artistList = QtGui.QListWidget()
        self.albumList = QtGui.QListWidget()

        self.searchEdit = QtGui.QLineEdit()
        self.timer = QtCore.QTimer()
        self.hLine = QtGui.QFrame()
        self.classicWebView = QtWebKit.QWebView()
        self.coverWebView = QtWebKit.QWebView()

        self.animation = QtCore.QPropertyAnimation(self, "geometry")

        # self.overlay = WaitOverlay(self)
        # self.overlay.hide()
        # self.artistList.itemActivated.connect(self.overlay.show)

        self.setup_ui()
        Menu(self)

        # ------------------------------------------------------------

        # deezer button timer on hover and on double click
        self.timer.timeout.connect(self.hover_button)
        self.iconLabel.signalDoubleClick.connect(self.click_button)

        # play album on button single click and press Enter
        self.playButton.clicked.connect(self.play_album)
        self.playButton.pressed.connect(self.play_album)

        # hide and show player (Bottom panel) on button single click
        self.hideBottomPanelButton.clicked.connect(self.hide_bottom_panel_button_clicked)
        self.showBottomPanelButton.clicked.connect(self.show_bottom_panel_button_clicked)
        self.playButton.pressed.connect(self.show_bottom_panel_button_clicked)

        # find artist names on button single click and on item press Enter
        self.searchButton.clicked.connect(self.find_artist)
        self.searchEdit.returnPressed.connect(self.find_artist)

        # find album titles on item single click and on item press Enter
        self.artistList.itemClicked.connect(self.find_album)
        self.artistList.itemActivated.connect(self.find_album)

        # find song titles on item single click and on item press Enter
        self.albumList.itemClicked.connect(self.find_song)
        self.albumList.itemActivated.connect(self.find_song)

        # show album cover on item single click and on item press Enter
        self.albumList.itemClicked.connect(self.show_cover)
        self.albumList.itemActivated.connect(self.show_cover)

    def setup_ui(self):

        """
        setup method
        """
        central_widget = QtGui.QWidget()
        self.setCentralWidget(central_widget)

        # -------------------buttons--------------------

        self.searchButton.setText("Search")
        self.searchButton.setAutoDefault(True)  # button focus

        self.playButton.setText("Play album")
        self.playButton.setAutoDefault(True)  # button focus

        self.hideBottomPanelButton.setVisible(False)
        self.hideBottomPanelButton.setText("^")
        self.hideBottomPanelButton.setFixedSize(50, 20)
        self.hideBottomPanelButton.setAutoDefault(True)  # button focus

        self.showBottomPanelButton.setVisible(False)
        self.showBottomPanelButton.setText("~")
        self.showBottomPanelButton.setFixedSize(50, 20)
        self.showBottomPanelButton.setAutoDefault(True)  # button focus

        # -------------------labels-------------------

        self.iconLabel.setToolTip("deezer.com")
        pixmap = QtGui.QPixmap("icon.svg")
        self.iconLabel.setPixmap(pixmap)
        self.iconLabel.setAlignment(QtCore.Qt.AlignRight)

        self.searchLabel.setText("Search")

        self.artistLabel.setText("Artist")
        self.albumLabel.setText("Album")
        self.songLabel.setText("Song")

        # -------------------lists--------------------
        self.artistList.setMinimumHeight(300)
        self.artistList.setToolTip("Choose the artist")
        self.albumList.setMinimumHeight(300)
        self.albumList.setToolTip("Choose the album")
        self.songList.setMinimumHeight(300)
        self.songList.setToolTip("Choose the song")

        # -------------------others-------------------

        self.searchEdit.setMinimumWidth(250)
        self.searchEdit.setToolTip("Enter artist name, and press Enter")

        self.timer.start(10)  # timer initial state

        self.hLine.setFrameShape(QtGui.QFrame.HLine)
        self.hLine.setFrameShadow(QtGui.QFrame.Sunken)

        self.classicWebView.hide()
        self.classicWebView.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        self.classicWebView.settings().setAttribute(QtWebKit.QWebSettings.PluginsEnabled, True)
        self.classicWebView.settings().setMaximumPagesInCache(0)

        self.coverWebView.setFixedSize(300, 300)
        self.coverWebView.settings().setMaximumPagesInCache(0)

        # ----------------window-geometry--------------------

        self.setGeometry(300, 100, 1200, 400)
        self.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        self.setWindowTitle("10heures player")
        self.setWindowIcon(QtGui.QIcon("icon.svg"))

        # ------------------grid-layout-----------------------

        sub_layout_1 = QtGui.QGridLayout()
        sub_layout_1.setSpacing(5)
        sub_layout_1.addWidget(self.searchLabel, 1, 1, 1, 1, QtCore.Qt.AlignLeft)
        sub_layout_1.addWidget(self.searchEdit, 1, 2, 1, 1, QtCore.Qt.AlignLeft)
        sub_layout_1.addWidget(self.searchButton, 1, 3, 1, 1, QtCore.Qt.AlignLeft)
        sub_layout_1.addWidget(self.playButton, 1, 4, 1, 1, QtCore.Qt.AlignLeft)

        sub_layout_2 = QtGui.QGridLayout()
        sub_layout_2.setSpacing(5)
        sub_layout_2.addWidget(self.hLine, 1, 1, 1, 4)
        sub_layout_2.addWidget(self.artistLabel, 2, 1, 1, 1)
        sub_layout_2.addWidget(self.albumLabel, 2, 2, 1, 1)
        sub_layout_2.addWidget(self.songLabel, 2, 3, 1, 1)
        sub_layout_2.addWidget(self.artistList, 3, 1, 1, 1)
        #sub_layout_2.addWidget(self.overlay, 3, 1, 1, 1)
        sub_layout_2.addWidget(self.albumList, 3, 2, 1, 1)
        sub_layout_2.addWidget(self.songList, 3, 3, 1, 1)
        sub_layout_2.addWidget(self.coverWebView, 3, 4, 1, 1)

        sub_layout_3 = QtGui.QGridLayout()
        sub_layout_3.setSpacing(5)
        sub_layout_3.addWidget(self.classicWebView, 4, 1, 1, 1)
        sub_layout_3.addWidget(self.hideBottomPanelButton, 5, 1, 1, 1, QtCore.Qt.AlignLeft)
        sub_layout_3.addWidget(self.showBottomPanelButton, 5, 1, 1, 1, QtCore.Qt.AlignLeft)

        grid = QtGui.QGridLayout()
        grid.addWidget(self.iconLabel, 1, 1, 1, 1, QtCore.Qt.AlignRight)
        grid.addLayout(sub_layout_1, 1, 1, 1, 1, QtCore.Qt.AlignLeft)
        grid.addLayout(sub_layout_2, 2, 1, 1, 1)
        grid.addLayout(sub_layout_3, 3, 1, 1, 1)
        central_widget.setLayout(grid)

        # ------------tab-order-----------------

        self.setTabOrder(self.searchEdit, self.searchButton)
        self.setTabOrder(self.searchButton, self.artistList)
        self.setTabOrder(self.artistList, self.albumList)
        self.setTabOrder(self.albumList, self.songList)
        self.setTabOrder(self.songList, self.showBottomPanelButton)
        self.setTabOrder(self.showBottomPanelButton, self.hideBottomPanelButton)
        self.setTabOrder(self.hideBottomPanelButton, self.playButton)
