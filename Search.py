from PyQt4 import QtCore
import re
from FindArtistThread import FindArtistThread
from FindAlbumThread import FindAlbumThread
from FindSongThread import FindSongThread
from WaitOverlay import WaitOverlay
import webbrowser

__author__ = 'postrowski'

# -*-coding: utf-8-*-


class Search(QtCore.QObject):

    def __init__(self, parent):

        super(Search, self).__init__(parent)

        self.artistList = parent.artistList
        self.albumList = parent.albumList
        self.songList = parent.songList
        self.searchEdit = parent.searchEdit
        self.classicWebView = parent.classicWebView
        self.coverWebView = parent.coverWebView
        self.hideButton = parent.hideButton
        self.showButton = parent.showButton
        self.sub_layout_2 = parent.sub_layout_2
        self.pageButton = parent.pageButton
        self.coverWebView = parent.coverWebView

        self.overlay = WaitOverlay()

    def add_widget_1(self):

        self.sub_layout_2.addWidget(self.overlay, 3, 1, 1, 1)

    def add_widget_2(self):

        self.sub_layout_2.addWidget(self.overlay, 3, 2, 1, 1)

    def add_widget_3(self):

        self.sub_layout_2.addWidget(self.overlay, 3, 3, 1, 1)

    def add_widget_4(self):

        self.sub_layout_2.addWidget(self.overlay, 3, 4, 1, 1)

    def remove_widget(self):

        self.sub_layout_2.removeWidget(self.overlay)

    def run_artist_thread(self):

        # clear QWebView
        self.coverWebView.load(QtCore.QUrl())

        self.artist = FindArtistThread(self)

        self.artist.started.connect(self.overlay.show)
        self.artist.started.connect(self.add_widget_1)

        self.artist.finished.connect(self.remove_widget)
        self.artist.finished.connect(self.overlay.hide)
        self.artist.finished.connect(self.artist.deleteLater)

        self.albumList.setStyleSheet("QListWidget {background-color: None}")
        self.artist.start()

        return self.artist.artist_id_dict, self.artist.album_track_dict, self.artist.album_cover_big_dict

    def run_album_thread(self):

        self.album = FindAlbumThread(self)

        self.album.started.connect(self.overlay.show)
        self.album.started.connect(self.add_widget_2)

        self.album.finished.connect(self.remove_widget)
        self.album.finished.connect(self.overlay.hide)
        self.album.finished.connect(self.album.deleteLater)

        self.albumList.setStyleSheet("QListWidget {background-color: rgba(10, 20, 128, 30%)}")

        self.album.start()

        return self.album.album_dict

    def run_song_thread(self):

        self.song = FindSongThread(self)

        self.song.started.connect(self.overlay.show)
        self.song.started.connect(self.add_widget_3)

        self.song.finished.connect(self.remove_widget)
        self.song.finished.connect(self.overlay.hide)
        self.song.finished.connect(self.song.deleteLater)

        self.song.finished.connect(self.show_cover)

        self.song.start()

        return self.song.get_album_tracklist

    def show_cover(self):
        """
            Show album cover.
        """
        self.overlay.show()
        self.add_widget_4()

        get_album_tracklist = self.song.get_album_tracklist
        album_dict = self.album.album_dict
        # get checked album title...
        # get_alb_name = QtCore.QString(unicode(self.albumList.currentItem().text()))
        # ...and get his cover
        get_alb_cover = album_dict[get_album_tracklist][0].values()[0]

        print(u"Cover url {0}.".format(get_alb_cover))
        self.coverWebView.load(QtCore.QUrl(get_alb_cover))

    def cover_loaded(self):

        self.remove_widget()
        self.overlay.hide()

    def play_album(self):
        """
            Play chosen album.
        :return:
        """
        # show button
        self.pageButton.show()

        # change size of classicWebView (None, single, album)
        if self.songList.count() is 0:
            pass
        elif self.songList.count() is 1:
            self.hideButton.show()
            self.classicWebView.setFixedHeight(92)
            self.classicWebView.show()
        else:
            self.hideButton.show()
            self.classicWebView.setFixedHeight(400)
            self.classicWebView.show()

        # get checked song title...
        # validate input: if nothing in albumList is checked
        item = self.albumList.count()
        if not [i for i in range(item) if self.albumList.isItemSelected(self.albumList.item(i))]:
            return None
        else:
            get_alb_name = QtCore.QString(unicode(self.albumList.currentItem().text()))

        # console information
        print(u"Play tracks from {0}.".format(unicode(get_alb_name)))

        # find album id in tracklist
        get_album_tracklist = self.song.get_album_tracklist
        self.alb_id = re.search('album/(.*)/tracks', get_album_tracklist).group(1)

        # open deezer widget
        player_url = 'http://www.deezer.com/plugins/player?format=classic&autoplay=false&playlist=true&' \
                     'width=700&height=350&color=007FEB&layout=dark&size=medium&type=album&id={0}&' \
                     'title=&app_id=1'.format(self.alb_id)
        self.classicWebView.setUrl(QtCore.QUrl(player_url))

        return self.alb_id

    def hide_button_clicked(self):

        self.showButton.show()
        self.classicWebView.hide()

    def show_button_clicked(self):

        self.showButton.hide()
        self.classicWebView.show()

    def listen_on(self):

        print(u"Listen album on deezer.com")
        link = 'http://www.deezer.com/album/{0}'.format(self.alb_id)
        webbrowser.open(link, new=1, autoraise=True)