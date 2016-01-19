__author__ = 'postrowski'

# -*-coding: utf-8-*-

from PyQt4 import QtGui, QtCore, QtWebKit

from Menu import Menu
from ClickedQLabel import DoubleClickedQLabel
from DeezerIcon import DeezerIcon
from BottomPanel import BottomPanel
from Search import Search

class MainUI(QtGui.QMainWindow, BottomPanel, DeezerIcon, Search):
    x = BottomPanel

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
        self.classicLabel = QtGui.QLabel()

        self.sngList = QtGui.QListWidget()
        self.artList = QtGui.QListWidget()
        self.albList = QtGui.QListWidget()

        self.searchEdit = QtGui.QLineEdit()
        self.timer = QtCore.QTimer()
        self.hLine = QtGui.QFrame()
        self.classicWebView = QtWebKit.QWebView(self.classicLabel)
        self.animation = QtCore.QPropertyAnimation(self, "geometry")

        self.setup_ui()
        Menu(self)

        self.timer.timeout.connect(self.hover_button)
        self.iconLabel.signalDoubleClick.connect(self.click_button)

        self.playButton.clicked.connect(self.open_classic_player)

        self.hideBottomPanelButton.clicked.connect(self.hide_bottom_panel_button_clicked)
        self.showBottomPanelButton.clicked.connect(self.show_bottom_panel_button_clicked)

        self.searchButton.clicked.connect(self.find_art)
        self.searchEdit.returnPressed.connect(self.find_art)

        self.artList.itemDoubleClicked.connect(self.find_alb)
        self.albList.itemDoubleClicked.connect(self.find_sng)

        # self.playButton.clicked.connect(self.play_album)

    def setup_ui(self):

        """
        setup method
        """

        central_widget = QtGui.QWidget()
        self.setCentralWidget(central_widget)

        # --------------------widgets-------------------

        # -------------------buttons--------------------

        self.searchButton.setText("Search")

        self.playButton.setText("Play album")

        self.hideBottomPanelButton.setVisible(False)
        self.hideBottomPanelButton.setText("^")
        self.hideBottomPanelButton.setFixedSize(50, 20)

        self.showBottomPanelButton.setVisible(False)
        self.showBottomPanelButton.setText("~")
        self.showBottomPanelButton.setFixedSize(50, 20)

        # -------------------labels-------------------

        self.iconLabel.setToolTip("deezer.com")
        pixmap = QtGui.QPixmap("icon.ico")
        self.iconLabel.setPixmap(pixmap)
        self.iconLabel.setAlignment(QtCore.Qt.AlignRight)

        self.searchLabel.setText("Search")

        self.artistLabel.setText("Artist")
        self.albumLabel.setText("Album")
        self.songLabel.setText("Song")

        self.classicLabel.setVisible(False)
        self.classicLabel.setMinimumHeight(400)
        self.classicWebView.settings().setAttribute(QtWebKit.QWebSettings.PluginsEnabled, True)
        self.classicWebView.setVisible(False)

        # -------------------lists--------------------

        self.artList.setMinimumHeight(200)
        self.artList.setToolTip("Choose the artist")

        self.albList.setMinimumHeight(200)
        self.albList.setToolTip("Choose the album")

        self.sngList.setMinimumHeight(200)
        self.sngList.setToolTip("Choose the song")

        # -------------------others-------------------

        self.searchEdit.setMinimumWidth(250)
        self.searchEdit.setToolTip("Enter artist name, and press Enter")

        self.timer.start(10)  # timer initial state

        self.hLine.setFrameShape(QtGui.QFrame.HLine)
        self.hLine.setFrameShadow(QtGui.QFrame.Sunken)

        # ----------------window-geometry--------------------

        self.setGeometry(300, 300, 800, 300)
        self.setWindowTitle("Deezer player")
        self.setWindowIcon(QtGui.QIcon("icon.ico"))
        # self.setStyleSheet('background-color: #343434')

        # ------------------grid-layout-----------------------

        sub_layout_1 = QtGui.QGridLayout()
        sub_layout_1.setSpacing(5)
        sub_layout_1.addWidget(self.searchLabel, 1, 1, 1, 1, QtCore.Qt.AlignLeft)
        sub_layout_1.addWidget(self.searchEdit, 1, 2, 1, 1, QtCore.Qt.AlignLeft)
        sub_layout_1.addWidget(self.searchButton, 1, 3, 1, 1, QtCore.Qt.AlignLeft)
        sub_layout_1.addWidget(self.playButton, 1, 4, 1, 1, QtCore.Qt.AlignLeft)

        sub_layout_2 = QtGui.QGridLayout()
        sub_layout_2.setSpacing(5)
        sub_layout_2.addWidget(self.hLine, 1, 1, 1, 3)
        sub_layout_2.addWidget(self.artistLabel, 2, 1, 1, 1)
        sub_layout_2.addWidget(self.albumLabel, 2, 2, 1, 1)
        sub_layout_2.addWidget(self.songLabel, 2, 3, 1, 1)
        sub_layout_2.addWidget(self.artList, 3, 1, 1, 1)
        sub_layout_2.addWidget(self.albList, 3, 2, 1, 1)
        sub_layout_2.addWidget(self.sngList, 3, 3, 1, 1)

        sub_layout_3 = QtGui.QGridLayout()
        sub_layout_3.setSpacing(5)
        sub_layout_3.addWidget(self.classicLabel, 4, 1, 1, 3)
        sub_layout_3.addWidget(self.hideBottomPanelButton, 5, 1, 1, 1)
        sub_layout_3.addWidget(self.showBottomPanelButton, 5, 1, 1, 1)

        grid = QtGui.QGridLayout()
        grid.addWidget(self.iconLabel, 1, 1, 1, 1, QtCore.Qt.AlignRight)
        grid.addLayout(sub_layout_1, 1, 1, 1, 1, QtCore.Qt.AlignLeft)
        grid.addLayout(sub_layout_2, 2, 1, 1, 1)
        grid.addLayout(sub_layout_3, 3, 1, 1, 1)
        central_widget.setLayout(grid)
