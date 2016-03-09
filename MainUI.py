from PyQt4 import QtGui, QtCore, QtWebKit
from Menu import Menu
from ClickedQLabel import DoubleClickedQLabel
from DeezerIcon import DeezerIcon
from Search import Search

__author__ = 'postrowski'

# -*-coding: utf-8-*-


class MainUI(QtGui.QMainWindow, DeezerIcon):

    def __init__(self, parent=None):

        super(MainUI, self).__init__(parent)

        self.searchButton = QtGui.QPushButton()
        self.playButton = QtGui.QPushButton()
        self.showButton = QtGui.QPushButton()
        self.hideButton = QtGui.QPushButton()
        self.pageButton = QtGui.QPushButton()

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

        self.setup_ui()
        Menu(self)
        self.search = Search(self)

        # ------------------------------------------------------------

        # deezer button timer on hover and on double click
        self.timer.timeout.connect(self.hover_button)
        self.iconLabel.signalDoubleClick.connect(self.click_button)

        # hide and show player (Bottom panel) on button single click
        self.hideButton.clicked.connect(self.search.hide_button_clicked)
        self.showButton.clicked.connect(self.search.show_button_clicked)

        # play album on button single click and press Enter
        self.playButton.clicked.connect(self.search.play_album)
        self.playButton.pressed.connect(self.search.play_album)

        # find artist names on button single click and on item press Enter
        self.searchButton.clicked.connect(self.search.run_artist_thread)
        self.searchEdit.returnPressed.connect(self.search.run_artist_thread)

        # find album titles on item single click and on item press Enter
        self.artistList.itemClicked.connect(self.search.run_album_thread)
        self.artistList.itemActivated.connect(self.search.run_album_thread)

        # find song titles and show album cover on item single click and on item press Enter
        self.albumList.itemClicked.connect(self.search.run_song_thread)
        self.albumList.itemActivated.connect(self.search.run_song_thread)
        self.coverWebView.loadFinished.connect(self.search.cover_loaded)

        # go to album page on deezer.com on single click and press Enter
        self.pageButton.clicked.connect(self.search.listen_on)
        self.pageButton.pressed.connect(self.search.listen_on)

    def setup_ui(self):

        """
            Setup widgets.
        """
        self.central_widget = QtGui.QWidget()
        self.setCentralWidget(self.central_widget)

        # button
        self.searchButton.setText("Search")
        self.searchButton.setAutoDefault(True)  # button focus

        self.playButton.setText("Play album")
        self.playButton.setAutoDefault(True)  # button focus

        self.hideButton.hide()
        self.hideButton.setText("hide")
        self.hideButton.setAutoDefault(True)  # button focus

        self.showButton.hide()
        self.showButton.setText("show")
        self.showButton.setAutoDefault(True)  # button focus

        self.pageButton.hide()
        self.pageButton.setText("listen")
        self.pageButton.setToolTip("Listen album on deezer.com")
        self.pageButton.setAutoDefault(True)  # button focus

        # label
        self.iconLabel.setToolTip("deezer.com")
        pixmap = QtGui.QPixmap("icon.svg")
        self.iconLabel.setPixmap(pixmap)
        self.iconLabel.setAlignment(QtCore.Qt.AlignRight)

        self.searchLabel.setText("Search")

        self.artistLabel.setText("Artist")
        self.albumLabel.setText("Album")
        self.songLabel.setText("Song")

        # list
        self.artistList.setMinimumHeight(300)
        self.artistList.setToolTip("Choose the artist")
        self.albumList.setMinimumHeight(300)
        self.albumList.setToolTip("Choose the album")
        self.songList.setMinimumHeight(300)
        self.songList.setToolTip("Choose the song")

        # --
        self.searchEdit.setMinimumWidth(250)
        self.searchEdit.setToolTip("Enter artist name, and press Enter")

        self.timer.start(10)  # timer initial state

        self.hLine.setFrameShape(QtGui.QFrame.HLine)
        self.hLine.setFrameShadow(QtGui.QFrame.Sunken)

        # web view
        self.classicWebView.hide()
        self.classicWebView.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        self.classicWebView.settings().setAttribute(QtWebKit.QWebSettings.PluginsEnabled, True)
        self.classicWebView.settings().setMaximumPagesInCache(0)

        self.coverWebView.setFixedSize(300, 300)
        self.coverWebView.settings().setMaximumPagesInCache(0)

        # window geometry
        self.setGeometry(300, 100, 1200, 400)
        self.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        self.setWindowTitle("10heures player")
        self.setWindowIcon(QtGui.QIcon("images/icon.svg"))

        # grid layout
        sub_layout_1 = QtGui.QGridLayout()
        sub_layout_1.setSpacing(5)
        sub_layout_1.addWidget(self.searchLabel, 1, 1, 1, 1, QtCore.Qt.AlignLeft)
        sub_layout_1.addWidget(self.searchEdit, 1, 2, 1, 1, QtCore.Qt.AlignLeft)
        sub_layout_1.addWidget(self.searchButton, 1, 3, 1, 1, QtCore.Qt.AlignLeft)
        sub_layout_1.addWidget(self.playButton, 1, 4, 1, 1, QtCore.Qt.AlignLeft)

        self.sub_layout_2 = QtGui.QGridLayout()
        self.sub_layout_2.setSpacing(5)
        self.sub_layout_2.addWidget(self.hLine, 1, 1, 1, 4)
        self.sub_layout_2.addWidget(self.artistLabel, 2, 1, 1, 1)
        self.sub_layout_2.addWidget(self.albumLabel, 2, 2, 1, 1)
        self.sub_layout_2.addWidget(self.songLabel, 2, 3, 1, 1)
        self.sub_layout_2.addWidget(self.artistList, 3, 1, 1, 1)
        self.sub_layout_2.addWidget(self.albumList, 3, 2, 1, 1)
        self.sub_layout_2.addWidget(self.songList, 3, 3, 1, 1)
        self.sub_layout_2.addWidget(self.coverWebView, 3, 4, 1, 1)

        sub_layout_3 = QtGui.QGridLayout()
        sub_layout_3.setSpacing(5)
        sub_layout_3.addWidget(self.classicWebView, 4, 1, 1, 1)

        sub_layout_4 = QtGui.QGridLayout()
        sub_layout_4.setSpacing(5)
        sub_layout_4.addWidget(self.hideButton, 5, 1, 1, 1, QtCore.Qt.AlignLeft)
        sub_layout_4.addWidget(self.showButton, 5, 1, 1, 1, QtCore.Qt.AlignLeft)
        sub_layout_4.addWidget(self.pageButton, 5, 2, 1, 1, QtCore.Qt.AlignLeft)

        grid = QtGui.QGridLayout()
        grid.addWidget(self.iconLabel, 1, 1, 1, 1, QtCore.Qt.AlignRight)
        grid.addLayout(sub_layout_1, 1, 1, 1, 1, QtCore.Qt.AlignLeft)
        grid.addLayout(self.sub_layout_2, 2, 1, 1, 1)
        grid.addLayout(sub_layout_3, 3, 1, 1, 1)
        grid.addLayout(sub_layout_4, 4, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.central_widget.setLayout(grid)

        # tab order
        self.setTabOrder(self.searchEdit, self.searchButton)
        self.setTabOrder(self.searchButton, self.artistList)
        self.setTabOrder(self.artistList, self.albumList)
        self.setTabOrder(self.albumList, self.songList)
        self.setTabOrder(self.songList, self.showButton)
        self.setTabOrder(self.showButton, self.hideButton)
        self.setTabOrder(self.hideButton, self.pageButton)
        self.setTabOrder(self.pageButton, self.playButton)
