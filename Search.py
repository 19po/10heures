__author__ = 'postrowski'

# -*-coding: utf-8-*-

from PyQt4 import QtCore

import urllib
import json
from collections import OrderedDict
import re


class Search(object):
    def __init__(self, parent):

        self.artist_id_dict = {}
        self.album_track_dict = {}
        self.album_cover_big_dict = {}

        self.album_dict = {}
        self.get_album_tracklist = ''

        self.artistList = parent.artList
        self.albumList = parent.albList
        self.songList = parent.sngList
        self.searchEdit = parent.searchEdit
        self.classicWebView = parent.classicWebView
        self.searchButton = parent.searchButton
        self.playButton = parent.playButton
        self.coverWebView = parent.coverWebView

    def find_artist(self):
        """
        Find artists
        """
        self.artistList.clear()
        self.albumList.clear()
        self.songList.clear()
        self.searchButton.setDefault(False)  # button focus

        # information to user: list is not ready to play album
        self.albumList.setStyleSheet("QListWidget {background-color: None}")

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
        self.artist_id_dict = make_dict(artist_name_list, artist_tracklist_list, artist_id_list)

        # make dictionary {"artist name":[{"album tracklist""album name"}], ...}
        self.album_track_dict = make_dict(artist_name_list, album_tracklist_list, album_title_list)

        # make dictionary {"artist name":[{"album_cover_big":"album name"}], ...}
        self.album_cover_big_dict = make_dict(artist_name_list, album_cover_big_list, album_title_list)

        # print artists to list widget
        [self.artistList.addItem(self.artist_id_dict.keys()[i]) for i in range(len(self.artist_id_dict))]

        return self.artist_id_dict, self.album_track_dict, self.album_cover_big_dict

    def find_album(self):
        """
        Find artist albums.
        """
        self.albumList.clear()
        self.songList.clear()

        # information to user: list is ready to play album
        self.albumList.setStyleSheet("QListWidget {background-color: rgba(10, 20, 128, 30%)}")

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
        current_art_id_dict = make_dict(artist_name_list, artist_tracklist_list, artist_id_list)
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
            self.album_dict = make_dict(prev_album_tracklist + album_tracklist_list + album_tracklist_list2,
                                        prev_album + album_title_list + album_title_list2,
                                        prev_album_cover + album_cover_big_list + album_cover_big_list2)
            # update album names and print it to list widget
            self.update_album(self.album_dict)

        else:
            # make dictionary {"album tracklist":[{"album title":"album cover"}], ...}
            self.album_dict = make_dict(prev_album_tracklist + album_tracklist_list,
                                        prev_album + album_title_list,
                                        prev_album_cover + album_cover_big_list)
            # update album names and print it to list widget
            self.update_album(self.album_dict)

        return self.album_dict

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

    def play_album(self):

        """
        Play chosen album.
        """
        # change size of classicWebView (single or album)
        if self.songList.count() is 1:
            self.classicWebView.setMinimumHeight(92)
        else:
            self.classicWebView.setMinimumHeight(400)

        # self.playButton.setDefault(False)  # button focus
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
        alb_id = re.search('album/(.*)/tracks', self.get_album_tracklist).group(1)

        # open deezer widget
        player_url = 'http://www.deezer.com/plugins/player?format=classic&autoplay=false&playlist=true&' \
                     'width=700&height=350&color=007FEB&layout=dark&size=medium&type=album&id={0}&' \
                     'title=&app_id=1'.format(alb_id)
        self.classicWebView.setUrl(QtCore.QUrl(player_url))

    def show_cover(self):
        """
        Show album cover.
        """
        # get checked album title...
        get_alb_name = QtCore.QString(unicode(self.albumList.currentItem().text()))
        # ...and get his cover
        get_alb_cover = self.album_dict[self.get_album_tracklist][0].values()[0]

        print(u"Cover url {0}.".format(get_alb_cover))
        self.coverWebView.load(QtCore.QUrl(get_alb_cover))

    def update_album(self, a_dict):
        """
            Method make list with new album names and adds it to album list widget.
        """
        # get album names from dict
        a = []
        for i in range(len(a_dict)):
            for j in range(len(a_dict.values()[i])):
                a.append(a_dict.values()[i][j].keys())
        new_a = sum(a, [])  # remove one dimension
        # add album names to list widget
        [self.albumList.addItem(new_a[i]) for i in range(len(new_a))]

def make_dict(list1, list2, list3):
    """
    Function makes a dictionary.
    :param list1: input list (keys())
    :param list2: input list (nested keys())
    :param list3: input list (nested values())
    :return: output dictionary ({"list1":[{"list2":"list3"}], ...})
    """
    # make dictionary {"list1":[{"list2":"list3"}], ...}
    out_dict = {i: [] for i in set(list1)}
    [out_dict[x].append(y) for (x, y) in zip(list1, zip(list2, list3))]
    # ...make inner dictionary...
    in_dict = [dict(out_dict.values()[i]) for i in range(len(out_dict))]
    # ...join outer and inner dictionary
    new_dict = {i: [j] for (i, j) in zip(out_dict.keys(), in_dict)}
    return new_dict

def unique(z):
    """
    Function removes duplicates from list.
    :param z: input list
    :return: output list without duplicates
    """
    return list(OrderedDict.fromkeys(z))
