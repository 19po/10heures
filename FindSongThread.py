from PyQt4 import QtCore
import urllib
import json

__author__ = 'postrowski'

# -*-coding: utf-8-*-


class FindSongThread(QtCore.QThread):

    def __init__(self, parent):
        super(FindSongThread, self).__init__(parent)

        self.get_album_tracklist = ''

        self.albumList = parent.albumList
        self.songList = parent.songList

        self.album_dict = parent.album.album_dict

    def find_song(self):
        """
            Find album songs.
        """
        self.songList.clear()

        # get checked album title...
        get_alb_name = QtCore.QString(unicode(self.albumList.currentItem().text()))
        # ...and get his tracklist (two or more same album names; need to iterate by indexes)
        row = self.albumList.currentRow()
        self.get_album_tracklist = ''.join([y for x, y in enumerate(self.album_dict.keys()) if row is x])

        # console information
        print(u"Search for tracks from {0}.".format(unicode(get_alb_name)))
        print(self.get_album_tracklist)

        # open json file
        json_url = urllib.urlopen(self.get_album_tracklist)
        data = json.load(json_url)

        # get values from json file
        sng_title_list = []

        for i in range(len(data["data"])):
            sng_title = data["data"][i]["title"]
            sng_title_list.append(sng_title)

        json_url.close()

        # paste songs to list
        [self.songList.addItem(sng_title_list[i]) for i in range(len(sng_title_list))]

        return self.get_album_tracklist

    def run(self):
        self.find_song()
        return
