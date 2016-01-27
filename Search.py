__author__ = 'postrowski'

# -*-coding: utf-8-*-

from PyQt4 import QtCore

import urllib
import json
from collections import OrderedDict
import re

class Search(object):
    def __init__(self, parent):

        self.art_dict_u = {}
        self.alb_dict = {}
        self.alb_track_dict = {}

        self.artList = parent.artList
        self.albList = parent.albList
        self.sngList = parent.sngList
        self.searchEdit = parent.searchEdit
        self.show_bottom_panel = parent.show_bottom_panel
        self.classicWebView = parent.classicWebView

    # -----------find-artist-names------------

    def find_artist(self):
        """
        Find artists
        """

        self.artList.clear()
        self.albList.clear()
        self.sngList.clear()

        # information to user: list is not ready to play album
        self.albList.setStyleSheet("QListWidget {background-color: None}")

        # get input
        get_search_edit = QtCore.QString(unicode(self.searchEdit.text()))
        search_url = u'https://api.deezer.com/search?q={0}'.format(unicode(get_search_edit))
        print search_url

        # console information
        print(u"Search for: {0}".format(unicode(get_search_edit)))

        # open json file
        json_url = urllib.urlopen(search_url)
        data = json.load(json_url)

        # check index
        li = (len(data["data"]))

        # get values from json file
        art_name_list, art_tracklist_list = [], []  # art_picture_small_list = []
        alb_title_list, alb_tracklist_list = [], []  # alb_cover_small_list = []

        for i in range(li):
            art_name = data["data"][i]["artist"]["name"]
            art_name_list.append(art_name)

            # art_picture_small = data["data"][i]["artist"]["picture_small"]
            # art_picture_small_list.append(art_picture_small)

            art_tracklist = data["data"][i]["artist"]["tracklist"]
            art_tracklist_list.append(art_tracklist)

            alb_title = data["data"][i]["album"]["title"]
            alb_title_list.append(alb_title)

            # alb_cover_small = data["data"][i]["album"]["cover_small"]
            # alb_cover_small_list.append(alb_cover_small)

            alb_tracklist = data["data"][i]["album"]["tracklist"]
            alb_tracklist_list.append(alb_tracklist)

        # make dictionary {"artist name": ["artist tracklist", ...], ...}
        art_dict = {i: [] for i in set(art_name_list)}
        [art_dict[x].append(y) for (x, y) in zip(art_name_list, art_tracklist_list)]
        # ...and remove duplicates from values
        self.art_dict_u = {i: j for (i, j) in zip(art_dict.keys(), [unique(art_dict.values()[i]) for i in
                                                                    range(len(art_dict.values()))])}

        # make {"art name":[{"album name" : "album tracklist", ...}], ...}
        out_dict = {i: [] for i in set(art_name_list)}
        [out_dict[x].append(y) for (x, y) in zip(art_name_list, zip(alb_title_list, alb_tracklist_list))]
        # ...make inner dictionary...
        in_dict = [dict(out_dict.values()[i]) for i in range(len(out_dict))]
        # ...join outer and inner dictionary
        self.alb_dict = {i: [j] for (i, j) in zip(out_dict.keys(), in_dict)}

        [self.artList.addItem(self.alb_dict.keys()[i]) for i in range(len(self.alb_dict))]

        return self.art_dict_u, self.alb_dict

    # ------------find-album-titles-------------

    def find_album(self):
        """
        Find artist albums.
        """

        self.albList.clear()
        self.sngList.clear()

        # information to user: list is ready to play album
        self.albList.setStyleSheet("QListWidget {background-color: rgba(10, 20, 128, 30%)}")

        # get checked album title
        get_artist_name = QtCore.QString(unicode(self.artList.currentItem().text()))
        # ...and get his tracklist
        get_art_tracklist = self.art_dict_u[unicode(get_artist_name)][0]

        # console information
        print(u"Search for {0} albums.".format(unicode(get_artist_name)))
        print(''.join(get_art_tracklist))  # list to string

        # open json file
        json_url = urllib.urlopen(''.join(get_art_tracklist))  # list to string
        data = json.load(json_url)

        # check index
        li = (len(data["data"]))

        # get values from json file
        alb_title_list, alb_tracklist_list = [], []  # alb_cover_big_list = []
        for i in range(li):
            alb_title = data["data"][i]["album"]["title"]
            alb_title_list.append(alb_title)

            alb_tracklist = data['data'][i]['album']['tracklist']
            alb_tracklist_list.append(alb_tracklist)

            # alb_cover_big = data['data'][i]['album']['cover_big']
            # alb_cover_big_list.append(alb_cover_big)

        # get chosen artist albums from previous search
        prev_album = self.alb_dict[str(get_artist_name)][0].keys()
        # ...merge and remove duplicates previous and current albums
        album = []
        for i in range(len([prev_album + alb_title_list])):
            album = unique([prev_album + alb_title_list][i])

        # get chosen artist album tracklist from previous search
        prev_alb_track = self.alb_dict[str(get_artist_name)][0].values()
        # ...merge and remove duplicates previous and current albums
        album_track = ''
        for i in range(len([prev_alb_track + alb_tracklist_list])):
            album_track = unique([prev_alb_track + alb_tracklist_list][i])

        # paste albums to list
        [self.albList.addItem(album[i]) for i in range(len(album))]

        # make dictionary {"album title" : "album tracklist"}
        self.alb_track_dict = {i: j for (i, j) in zip(album, album_track)}

        return self.alb_track_dict

    def find_song(self):
        """
        Find album songs.
        """

        self.sngList.clear()

        # get checked album title
        get_alb_name = QtCore.QString(unicode(self.albList.currentItem().text()))
        # ...and get his tracklist
        get_alb_tracklist = self.alb_track_dict[unicode(get_alb_name)]

        # console information
        print(u"Search for tracks from {0}.".format(unicode(get_alb_name)))
        print(get_alb_tracklist)

        # open json file
        json_url = urllib.urlopen(get_alb_tracklist)
        data = json.load(json_url)

        # check index
        li = (len(data["data"]))

        # get values from json file
        sng_title_list = []
        for i in range(li):
            sng_title = data["data"][i]["title"]
            sng_title_list.append(sng_title)

        # paste songs to list
        [self.sngList.addItem(sng_title_list[i]) for i in range(len(sng_title_list))]

    def play_album(self):

        """
        Play chosen album.
        """
        # get checked song title
        get_alb_name = QtCore.QString(unicode(self.albList.currentItem().text()))
        # .. and get his tracklist
        get_alb_id = self.alb_track_dict[unicode(get_alb_name)]

        # console information
        print(u"Play tracks from {0}.".format(unicode(get_alb_name)))

        # find album id in tracklist
        alb_id = re.search('(.*)album/(.*)/tracks(.*)', get_alb_id).group(2)

        # open deezer widget
        artist_player_url = 'http://www.deezer.com/plugins/player?format=classic&autoplay=false&playlist=true&' \
                            'width=700&height=350&color=007FEB&layout=dark&size=medium&type=album&id={0}&' \
                            'title=&app_id=1'.format(alb_id)
        self.classicWebView.setUrl(QtCore.QUrl(artist_player_url))

        self.show_bottom_panel()

def unique(z):
    """
    Function remove duplicates from list.
    :param z: input list
    :return: output list without duplicates
    """
    return list(OrderedDict.fromkeys(z))
