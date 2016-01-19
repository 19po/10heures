__author__ = 'postrowski'

# -*-coding: utf-8-*-

from PyQt4 import QtCore

import urllib
import json
from collections import OrderedDict, defaultdict


class Search(object):
    def __init__(self, parent):

        self.art_lists_1u = []
        # self.alb_lists_1u = []
        self.alb_lists_2u = []

        self.new_nd_name = {}
        # self.new_alb_lists = []
        # self.new_nd_track = {}
        # self.new_track_lists = []
        self.new_nd_name_2 = {}

        self.artList = parent.artList
        self.albList = parent.albList
        self.sngList = parent.sngList
        self.searchEdit = parent.searchEdit
        self.show_bottom_panel = parent.show_bottom_panel
        self.classicWebView = parent.classicWebView

    def find_art(self):

        get_search_edit = QtCore.QString(unicode(self.searchEdit.text()))
        print(u"Search for: {0}".format(unicode(get_search_edit)))

        self.artList.clear()
        self.albList.clear()
        self.sngList.clear()

        # self.artList.setStyleSheet("QListWidget::item {background-color: #898989}")

        search_url = u'https://api.deezer.com/search?q={0}'.format(unicode(get_search_edit))
        print search_url

        json_url = urllib.urlopen(search_url)
        data = json.load(json_url)

        # -------------get-values-from-json-file----------------

        art_id_list = []
        art_name_list = []
        art_picture_small_list = []
        art_tracklist_list = []

        alb_id_list = []
        alb_title_list = []
        alb_cover_small_list = []
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

            art_picture_small = data["data"][i]["artist"]["picture_small"]
            art_picture_small_list.append(art_picture_small)

            art_tracklist = data["data"][i]["artist"]["tracklist"]
            art_tracklist_list.append(art_tracklist)

            alb_id = data["data"][i]["album"]["id"]
            alb_id_list.append(alb_id)

            alb_title = data["data"][i]["album"]["title"]
            alb_title_list.append(alb_title)

            alb_cover_small = data["data"][i]["album"]["cover_small"]
            alb_cover_small_list.append(alb_cover_small)

            alb_tracklist = data["data"][i]["album"]["tracklist"]
            alb_tracklist_list.append(alb_tracklist)

            sng_id = data["data"][i]["id"]
            sng_id_list.append(sng_id)

            sng_title = data["data"][i]["title"]
            sng_title_list.append(sng_title)

            # list1: [('album', 'album tracklist')]
            art_alb_track_list = zip(alb_title_list, alb_tracklist_list)

            # list2: [('artist', ('album','album tracklist'))]
            art_alb_name_list = zip(art_name_list, art_alb_track_list)

        # print(art_alb_track_list)
        # print(art_alb_name_list)

        # append list2 keys and values
        nd_name = defaultdict(list)
        [nd_name[k].append(v) for k, v in art_alb_name_list]

        print(nd_name)

        # remove duplicates from list2
        nd_name_val_uni = [unique(nd_name.values()[i]) for i in range(len(nd_name.values()))]
        self.new_nd_name = zip(nd_name.keys(), nd_name_val_uni)

        print(self.new_nd_name)

        # new dict: {'art_name' : {'alb_title' : 'alb_tracklist'}}
        new_nd_name_val_dict = [dict(self.new_nd_name[i]) for i in range(len(self.new_nd_name))]

        self.new_nd_name_2 = dict(zip(nd_name.keys(), new_nd_name_val_dict))
        print(OrderedDict(self.new_nd_name_2))
        print(self.new_nd_name_2)

        # ---------remove-duplicates-from-lists---------------

        art_lists_1 = [art_id_list] + [art_name_list] + [art_picture_small_list] + [art_tracklist_list]
        i1 = len(art_lists_1) - 1
        self.art_lists_1u = [unique(art_lists_1[i1]) for art_lists_1[i1] in art_lists_1[:]]
        # art_id_list, art_name_list, art_picture_small_list, art_tracklist_list = self.art_lists_1u

        alb_lists_1 = [alb_id_list] + [alb_title_list] + [alb_cover_small_list]
        i2 = len(alb_lists_1) - 1
        self.alb_lists_1u = [unique(alb_lists_1[i2]) for alb_lists_1[i2] in alb_lists_1[:]]
        # alb_id_list, alb_title_list, alb_cover_small_list = self.alb_lists_1u

        sng_lists_1 = [sng_id_list] + [sng_title_list]
        i3 = len(sng_lists_1) - 1
        sng_lists_1u = [unique(sng_lists_1[i3]) for sng_lists_1[i3] in sng_lists_1[:]]
        # sng_id_list, sng_title_list = sng_lists_1u

        # --------------add-elements-to-lists-----------------

        [self.artList.addItem(i) for i in self.art_lists_1u[1]]
        [self.albList.addItem(i) for i in self.alb_lists_1u[1]]
        [self.sngList.addItem(i) for i in sng_lists_1u[1]]

        return self.art_lists_1u, self.alb_lists_1u, self.new_nd_name_2, self.new_nd_name

    def find_alb(self):

        get_artist = QtCore.QString(unicode(self.artList.currentRow()))
        get_artist_name = QtCore.QString(unicode(self.artList.currentItem().text()))

        get_art_tracklist = self.art_lists_1u[3][int(get_artist)]

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

        # update album and tracklist list with values from first search (find_artist)
        if str(unicode(get_artist_name)) in self.new_nd_name.keys():
        #     self.new_alb_lists = self.alb_lists_2u[1] + self.new_nd_name_2[str(unicode(get_artist_name))].keys()
            # alb_title_list + self.new_nd_name_2[str(unicode(get_artist_name))].keys()
            # alb_tracklist_list + self.new_nd_name_2[str(unicode(get_artist_name))].values()
            print(self.new_nd_name[str(unicode(get_artist_name))].keys())
            print(self.new_nd_name[str(unicode(get_artist_name))].values())

        # ---------remove-duplicates-from-lists---------------

        # update album and tracklist list with values from first search (find_artist)
        # alb_lists_2 = [alb_id_list] + [alb_title_list + self.new_nd_name_2[str(unicode(get_artist_name))].keys()] + [
        #     alb_tracklist_list + self.new_nd_name_2[str(unicode(get_artist_name))].values()]

        alb_lists_2 = [alb_id_list] + [alb_title_list] + [alb_tracklist_list]

        i2 = len(alb_lists_2) - 1
        self.alb_lists_2u = [unique(alb_lists_2[i2]) for alb_lists_2[i2] in alb_lists_2[:]]
        # alb_id_list, alb_title_list = alb_lists

        sng_lists_2 = [sng_id_list] + [sng_title_list]
        i3 = len(sng_lists_2) - 1
        sng_lists_2u = [unique(sng_lists_2[i3]) for sng_lists_2[i3] in sng_lists_2[:]]
        # sng_id_list, sng_title_list = sng_lists

        # --------------add-elements-to-lists-----------------

        [self.albList.addItem(i) for i in self.alb_lists_2u[1]]
        [self.sngList.addItem(i) for i in sng_lists_2u[1]]

        return self.alb_lists_2u  # , self.new_alb_lists

    def find_sng(self):

        get_album = QtCore.QString(unicode(self.albList.currentRow()))
        get_album_name = QtCore.QString(unicode(self.albList.currentItem().text()))

        get_alb_tracklist = self.alb_lists_2u[2][int(get_album)]

        print(u"Search for tracks from {0}.".format(unicode(get_album_name)))
        print(get_alb_tracklist)

        self.sngList.clear()

        json_url = urllib.urlopen(get_alb_tracklist)
        data = json.load(json_url)

        # -------------get-values-from-json-file----------------

        sng_id_list = []
        sng_title_list = []

        # check index
        li = (len(data["data"]))

        for i in range(li):
            sng_id = data["data"][i]["id"]
            sng_id_list.append(sng_id)

            sng_title = data["data"][i]["title"]
            sng_title_list.append(sng_title)

        # ---------remove-duplicates-from-list---------------

        sng_lists_3 = [sng_id_list] + [sng_title_list]
        i3 = len(sng_lists_3) - 1
        sng_lists_3u = [unique(sng_lists_3[i3]) for sng_lists_3[i3] in sng_lists_3[:]]
        # sng_id_list, sng_title_list = sng_lists

        # --------------add-elements-to-list-----------------

        [self.sngList.addItem(i) for i in sng_lists_3u[1]]

        # return sng_lists_3u

        # -----------------play album------------------------

    def play_album(self):

        get_alb = QtCore.QString(unicode(self.albList.currentRow()))
        get_album_name = QtCore.QString(unicode(self.albList.currentItem().text()))

        get_alb_id = self.alb_lists_1u[0][int(get_alb)] or self.alb_lists_1u[0][int(get_alb)]
        print(u"Play tracks from {0}.".format(unicode(get_album_name)))

        self.show_bottom_panel()

        artist_player_url = 'http://www.deezer.com/plugins/player?format=classic&autoplay=false&playlist=true&' \
                            'width=700&height=350&color=007FEB&layout=dark&size=medium&type=album&id=%s&' \
                            'title=&app_id=1' % get_alb_id
        self.classicWebView.setUrl(QtCore.QUrl(artist_player_url))


def unique(z):
    return list(OrderedDict.fromkeys(z))
