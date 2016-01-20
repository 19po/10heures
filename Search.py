__author__ = 'postrowski'

# -*-coding: utf-8-*-

from PyQt4 import QtCore

import urllib
import json
from collections import OrderedDict


class Search(object):
    def __init__(self, parent):

        self.art_lists_1u = []
        self.alb_lists_1u = []
        self.alb_lists_old_1u = []
        self.alb_lists_new_2u = []

        self.artList = parent.artList
        self.albList = parent.albList
        self.sngList = parent.sngList
        self.searchEdit = parent.searchEdit
        self.show_bottom_panel = parent.show_bottom_panel
        self.classicWebView = parent.classicWebView

    # -----------find-artist-names------------

    def find_art(self):

        # information to user: list is not ready to play album
        self.albList.setStyleSheet("QListWidget {background-color: #FFFFFF}")

        get_search_edit = QtCore.QString(unicode(self.searchEdit.text()))
        print(u"Search for: {0}".format(unicode(get_search_edit)))

        self.artList.clear()
        self.albList.clear()
        self.sngList.clear()

        search_url = u'https://api.deezer.com/search?q={0}'.format(unicode(get_search_edit))
        print search_url

        json_url = urllib.urlopen(search_url)
        data = json.load(json_url)

        # -------------get-values-from-json-file----------------

        art_id_list = []
        art_name_list = []
        # art_picture_small_list = []
        art_tracklist_list = []

        alb_id_list = []
        alb_title_list = []
        # alb_cover_small_list = []
        alb_tracklist_list = []

        sng_id_list = []
        sng_title_list = []

        # check index
        li = (len(data["data"]))

        for i in range(li):
            art_id = data["data"][i]["artist"]["id"]
            art_id_list.append(art_id)

            art_name = data["data"][i]["artist"]["name"]
            art_name_list.append(art_name)

            # art_picture_small = data["data"][i]["artist"]["picture_small"]
            # art_picture_small_list.append(art_picture_small)

            art_tracklist = data["data"][i]["artist"]["tracklist"]
            art_tracklist_list.append(art_tracklist)

            alb_id = data["data"][i]["album"]["id"]
            alb_id_list.append(alb_id)

            alb_title = data["data"][i]["album"]["title"]
            alb_title_list.append(alb_title)

            # alb_cover_small = data["data"][i]["album"]["cover_small"]
            # alb_cover_small_list.append(alb_cover_small)

            alb_tracklist = data["data"][i]["album"]["tracklist"]
            alb_tracklist_list.append(alb_tracklist)

            sng_id = data["data"][i]["id"]
            sng_id_list.append(sng_id)

            sng_title = data["data"][i]["title"]
            sng_title_list.append(sng_title)

        # ---------remove-duplicates-from-lists---------------

        art_lists_1 = [art_id_list] + [art_name_list] + [art_tracklist_list]
        i1 = len(art_lists_1) - 1
        self.art_lists_1u = [unique(art_lists_1[i1]) for art_lists_1[i1] in art_lists_1[:]]

        alb_lists_1 = [alb_id_list] + [alb_title_list]
        i2 = len(alb_lists_1) - 1
        self.alb_lists_1u = [unique(alb_lists_1[i2]) for alb_lists_1[i2] in alb_lists_1[:]]

        sng_lists_1 = [sng_id_list] + [sng_title_list]
        i3 = len(sng_lists_1) - 1
        sng_lists_1u = [unique(sng_lists_1[i3]) for sng_lists_1[i3] in sng_lists_1[:]]

        # -----------old-album-titles-to-previous-album-search----------

        alb_lists_old_1 = [alb_id_list] + [alb_title_list] + [alb_tracklist_list]
        old = len(alb_lists_old_1) - 1
        self.alb_lists_old_1u = [unique(alb_lists_old_1[old]) for alb_lists_old_1[old] in alb_lists_old_1[:]]

        # --------------add-elements-to-lists-----------------

        [self.artList.addItem(i) for i in self.art_lists_1u[1]]
        [self.albList.addItem(i) for i in self.alb_lists_1u[1]]
        [self.sngList.addItem(i) for i in sng_lists_1u[1]]

        return self.art_lists_1u, self.alb_lists_1u, self.alb_lists_old_1u  # , self.new_nd_name_2, self.new_nd_name

    # ------------find-album-titles-------------

    def find_alb(self):

        # information to user: list is ready to play album
        self.albList.setStyleSheet("QListWidget {background-color: rgba(10, 20, 128, 30%)}")

        get_artist = QtCore.QString(unicode(self.artList.currentRow()))
        get_artist_name = QtCore.QString(unicode(self.artList.currentItem().text()))

        get_art_tracklist = self.art_lists_1u[2][int(get_artist)]

        print(u"Search for {0} albums.".format(unicode(get_artist_name)))
        print(get_art_tracklist)

        self.albList.clear()
        self.sngList.clear()

        json_url = urllib.urlopen(get_art_tracklist)
        data = json.load(json_url)

        # -------------get-values-from-json-file----------------

        alb_id_list = []
        alb_title_list = []
        alb_tracklist_list = []
        # alb_cover_big_list = []

        sng_id_list = []
        sng_title_list = []

        # check index
        li = (len(data["data"]))

        for i in range(li):
            alb_id = data["data"][i]["album"]["id"]
            alb_id_list.append(alb_id)

            alb_title = data["data"][i]["album"]["title"]
            alb_title_list.append(alb_title)

            alb_tracklist = data['data'][i]['album']['tracklist']
            alb_tracklist_list.append(alb_tracklist)

            # alb_cover_big = data['data'][i]['album']['cover_big']
            # alb_cover_big_list.append(alb_cover_big)

            sng_id = data["data"][i]["id"]
            sng_id_list.append(sng_id)

            sng_title = data["data"][i]["title"]
            sng_title_list.append(sng_title)

        # ---------remove-duplicates-from-lists---------------

        alb_lists_2 = [alb_id_list] + [alb_title_list] + [alb_tracklist_list]
        i2 = len(alb_lists_2) - 1
        self.alb_lists_2u = [unique(alb_lists_2[i2]) for alb_lists_2[i2] in alb_lists_2[:]]

        sng_lists_2 = [sng_id_list] + [sng_title_list]
        i3 = len(sng_lists_2) - 1
        sng_lists_2u = [unique(sng_lists_2[i3]) for sng_lists_2[i3] in sng_lists_2[:]]

        # join album titles from artist search and this search; delete duplicates

        alb_lists_new_2 = [self.alb_lists_2u[i] + self.alb_lists_old_1u[i] for i in range(0,3)]
        i4 = len(alb_lists_new_2) - 1
        self.alb_lists_new_2u = [unique(alb_lists_new_2[i4]) for alb_lists_new_2[i4] in alb_lists_new_2[:]]

        # --------------add-elements-to-lists-----------------

        [self.albList.addItem(i) for i in self.alb_lists_new_2u[1]]
        [self.sngList.addItem(i) for i in sng_lists_2u[1]]

        return self.alb_lists_new_2u

    # -------------find-song-titles--------------

    def find_sng(self):

        """
        Find album songs.
        Method check active current row in List Widget (albList), get his index (get_alb) and his name (get_alb_name).
        Then using index (get_alb) get his website link (get_alb_tracklist) from list (alb_lists_2u).
        Clear List Widget (sngList) for new data. Open website link with json (data) file. Make list of songs titles
        (sng_title_list) and paste it to List Widget (sngList).
        """
        get_alb = QtCore.QString(unicode(self.albList.currentRow()))
        get_alb_name = QtCore.QString(unicode(self.albList.currentItem().text()))

        get_alb_tracklist = self.alb_lists_new_2u[2][int(get_alb)]

        print(u"Search for tracks from {0}.".format(unicode(get_alb_name)))
        print(get_alb_tracklist)

        self.sngList.clear()

        json_url = urllib.urlopen(get_alb_tracklist)
        data = json.load(json_url)

        # -------------get-values-from-json-file----------------

        # sng_id_list = []
        sng_title_list = []

        # check index
        li = (len(data["data"]))

        for i in range(li):
            # sng_id = data["data"][i]["id"]
            # sng_id_list.append(sng_id)

            sng_title = data["data"][i]["title"]
            sng_title_list.append(sng_title)

        # ---------remove-duplicates-from-list---------------

        # sng_lists_3 = [sng_id_list] + [sng_title_list]
        sng_lists_3 = [sng_title_list]
        i3 = len(sng_lists_3) - 1
        sng_lists_3u = [unique(sng_lists_3[i3]) for sng_lists_3[i3] in sng_lists_3[:]]

        # --------------add-elements-to-list-----------------

        [self.sngList.addItem(i) for i in sng_lists_3u[0]]

    # -----------------play-album------------------------

    def play_album(self):

        """
        Play chosen album.
        Method check active current row in List Widget (albList), get his index (get_alb) and his name (get_alb_name).
        Then using index (get_alb) get his id (get_alb_id) from list (alb_lists_2u). Supplements url (artist_player_url)
        with album id (get_alb_id) and display playlist (class BottomPanel).
        """
        get_alb = QtCore.QString(unicode(self.albList.currentRow()))
        get_alb_name = QtCore.QString(unicode(self.albList.currentItem().text()))

        get_alb_id = self.alb_lists_new_2u[0][int(get_alb)]
        print(u"Play tracks from {0}.".format(unicode(get_alb_name)))

        artist_player_url = 'http://www.deezer.com/plugins/player?format=classic&autoplay=false&playlist=true&' \
                            'width=700&height=350&color=007FEB&layout=dark&size=medium&type=album&id={0}&' \
                            'title=&app_id=1'.format(get_alb_id)
        self.classicWebView.setUrl(QtCore.QUrl(artist_player_url))

        self.show_bottom_panel()


def unique(z):
    """
    Function remove duplicates from list.
    :param z: input list
    :return: output list without duplicates
    """
    return list(OrderedDict.fromkeys(z))
