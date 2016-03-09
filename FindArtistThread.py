from PyQt4 import QtCore
import urllib
import json
from MakeDict import MakeDict

__author__ = 'postrowski'

# -*-coding: utf-8-*-


class FindArtistThread(QtCore.QThread):

    def __init__(self, parent):
        super(FindArtistThread, self).__init__(parent)

        self.artist_id_dict = {}
        self.album_track_dict = {}
        self.album_cover_big_dict = {}

        self.artistList = parent.artistList
        self.albumList = parent.albumList
        self.songList = parent.songList
        self.searchEdit = parent.searchEdit

    def find_artist(self):
        """
            Find artists.
        """
        md = MakeDict()

        # clear lists
        self.artistList.clear()
        self.albumList.clear()
        self.songList.clear()

        # get input
        get_search_edit = QtCore.QString(unicode(self.searchEdit.text()))
        search_url = u'https://api.deezer.com/search?q={0}'.format(unicode(get_search_edit))

        # load json file; validate input
        json_url = ''
        data = {}
        try:
            json_url = urllib.urlopen(search_url)
            data = json.load(json_url)
        except IOError:
            self.artistList.setEnabled(False)
            self.albumList.setEnabled(False)
            self.songList.setEnabled(False)
            self.artistList.addItem("No Internet connection found.")
            self.albumList.addItem("No Internet connection found.")
            self.songList.addItem("No Internet connection found.")
            print("No Internet connection found.")

        # check index; validate input
        if not data or self.searchEdit.text().isEmpty():
            return None
        else:
            li = len(data["data"])

        # console information
        print(u"Search for: {0}".format(unicode(get_search_edit)))
        print search_url

        # get values from json file
        artist_name_list, artist_id_list, artist_tracklist_list = [], [], []
        album_title_list, album_tracklist_list, album_cover_big_list = [], [], []

        for i in range(li):
            artist_name = data["data"][i]["artist"]["name"]
            artist_name_list.append(artist_name)

            artist_id = data["data"][i]["artist"]["id"]
            artist_id_list.append(artist_id)

            artist_tracklist = data["data"][i]["artist"]["tracklist"]
            artist_tracklist_list.append(artist_tracklist)

            album_title = data["data"][i]["album"]["title"]
            album_title_list.append(album_title)

            album_tracklist = data["data"][i]["album"]["tracklist"]
            album_tracklist_list.append(album_tracklist)

            album_cover_big = data["data"][i]["album"]["cover_big"]
            album_cover_big_list.append(album_cover_big)

        json_url.close()

        # make dictionary {"artist name":[{"artist tracklist":"artist id"}], ...}
        self.artist_id_dict = md.make_dict(artist_name_list, artist_tracklist_list, artist_id_list)

        # make dictionary {"artist name":[{"album tracklist""album name"}], ...}
        self.album_track_dict = md.make_dict(artist_name_list, album_tracklist_list, album_title_list)

        # make dictionary {"artist name":[{"album_cover_big":"album name"}], ...}
        self.album_cover_big_dict = md.make_dict(artist_name_list, album_cover_big_list, album_title_list)

        # print artists to list widget
        [self.artistList.addItem(self.artist_id_dict.keys()[i]) for i in range(len(self.artist_id_dict))]

        return self.artist_id_dict, self.album_track_dict, self.album_cover_big_dict

    def run(self):
        self.find_artist()
        return
