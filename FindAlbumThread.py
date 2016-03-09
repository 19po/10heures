from PyQt4 import QtCore
import urllib
import json
from MakeDict import MakeDict

__author__ = 'postrowski'

# -*-coding: utf-8-*-


class FindAlbumThread(QtCore.QThread):

    def __init__(self, parent):
        super(FindAlbumThread, self).__init__(parent)

        self.album_dict = {}

        self.artistList = parent.artistList
        self.albumList = parent.albumList
        self.songList = parent.songList
        self.searchEdit = parent.searchEdit

        self.artist_id_dict = parent.artist.artist_id_dict
        self.album_track_dict = parent.artist.album_track_dict
        self.album_cover_big_dict = parent.artist.album_cover_big_dict

    def update_album(self, a_dict):
        """
            Method make list with new album names and adds it to album list widget.
            :param a_dict: input dictionary
        """
        # get album names from dict
        a = []
        for i in range(len(a_dict)):
            for j in range(len(a_dict.values()[i])):
                a.append(a_dict.values()[i][j].keys())
        new_a = sum(a, [])  # remove one dimension
        # add album names to list widget
        [self.albumList.addItem(new_a[i]) for i in range(len(new_a))]

    def find_album(self):
        """
            Find artist albums.
        """
        md = MakeDict()

        self.albumList.clear()
        self.songList.clear()

        # get checked album title
        get_artist_name = QtCore.QString(unicode(self.artistList.currentItem().text()))

        # ...and get his tracklist
        get_artist_tracklist = self.artist_id_dict[unicode(get_artist_name)][0].keys()[0]

        # console information
        print(u"Search for {0} albums.".format(unicode(get_artist_name)))
        print(get_artist_tracklist)

        # open json file
        json_url = urllib.urlopen(get_artist_tracklist)
        data = json.load(json_url)

        # get values from json file
        artist_name_list, artist_id_list, artist_tracklist_list = [], [], []
        album_title_list, album_tracklist_list, album_cover_big_list = [], [], []

        for i in range(len(data["data"])):
            artist_name = data["data"][i]["artist"]["name"]
            artist_name_list.append(artist_name)

            artist_id = data["data"][i]["artist"]["id"]
            artist_id_list.append(artist_id)

            artist_tracklist = data["data"][i]["artist"]["tracklist"]
            artist_tracklist_list.append(artist_tracklist)

            album_title = data["data"][i]["album"]["title"]
            album_title_list.append(album_title)

            album_tracklist = data['data'][i]['album']['tracklist']
            album_tracklist_list.append(album_tracklist)

            album_cover_big = data['data'][i]['album']['cover_big']
            album_cover_big_list.append(album_cover_big)

        json_url.close()

        # extra album check
        # same artist names, but different ids'

        # make current dictionary {"artist":[{"artist tracklist":"artist id"}]}
        current_art_id_dict = md.make_dict(artist_name_list, artist_tracklist_list, artist_id_list)
        # merge inner dictionaries {"artist":[{"artist tracklist":"artist id"}]} from previous and current search...
        # ...make dictionary for current chosen artist {"artist tracklist":"artist id", ...}...
        new_art_id_dict = dict(current_art_id_dict[unicode(get_artist_name)][0].items() +
                               self.artist_id_dict[unicode(get_artist_name)][0].items())
        # delete tracklist used previous (from new_art_id_dict)
        del new_art_id_dict[''.join(get_artist_tracklist)]  # list to string

        # update tracklist, album and cover

        # make empty lists for new album names
        album_title_list2, album_tracklist_list2, album_cover_big_list2 = [], [], []

        # check if new_art_id_dict is not empty list
        if new_art_id_dict:
            json_url2 = urllib.urlopen(new_art_id_dict.keys()[0])
            # open json file
            data2 = json.load(json_url2)

            # get values from json file
            for i in range(len(data2["data"])):
                album_title2 = data2["data"][i]["album"]["title"]
                album_title_list2.append(album_title2)

                album_tracklist2 = data2['data'][i]['album']['tracklist']
                album_tracklist_list2.append(album_tracklist2)

                album_cover_big2 = data2['data'][i]['album']['cover_big']
                album_cover_big_list2.append(album_cover_big2)

            json_url2.close()

        # get chosen artist albums titles from previous search
        prev_album = self.album_track_dict[unicode(get_artist_name)][0].values()

        # get chosen artist album tracklist from previous search
        prev_album_tracklist = self.album_track_dict[unicode(get_artist_name)][0].keys()

        # get chosen artist album cover from previous search
        prev_album_cover = self.album_cover_big_dict[unicode(get_artist_name)][0].keys()

        # make and/or update new_album_title list with album names from previous and current search

        # check if album_title_list2 is not empty list
        if album_title_list2:
            # make dictionary {"album tracklist":[{"album title":"album cover"}], ...}
            self.album_dict = md.make_dict(prev_album_tracklist + album_tracklist_list + album_tracklist_list2,
                                        prev_album + album_title_list + album_title_list2,
                                        prev_album_cover + album_cover_big_list + album_cover_big_list2)
            # update album names and print it to list widget
            self.update_album(self.album_dict)

        else:
            # make dictionary {"album tracklist":[{"album title":"album cover"}], ...}
            self.album_dict = md.make_dict(prev_album_tracklist + album_tracklist_list,
                                        prev_album + album_title_list,
                                        prev_album_cover + album_cover_big_list)
            # update album names and print it to list widget
            self.update_album(self.album_dict)

        return self.album_dict

    def run(self):
        self.find_album()
        return
