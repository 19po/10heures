__author__ = 'postrowski'

# -*-coding: utf-8-*-

from PyQt4 import QtCore

import urllib
import json
from collections import OrderedDict

class Searching(object):

    def __init__(self, parent):
        self.search(parent)
        #self.pp(parent)
        self.artist(parent)
        self.album(parent)
        self.play_album(parent)

    @staticmethod
    def pp(kot, li):
        print kot, li

    @staticmethod
    def unique(z):
        return list(OrderedDict.fromkeys(z))

    @staticmethod
    def load_json(search_url):
        json_url = urllib.urlopen(search_url)
        data = json.load(json_url)
        return data

    def search(self, parent, data=None):

        # get_search_edit = QtCore.QString(unicode(parent.searchEdit(parent).text()))
        get_search_edit = parent.searchEdit.text()
        print(u"Search for: {0}".format(unicode(get_search_edit)))

        parent.artList.clear()
        parent.albList.clear()
        parent.sngList.clear()

        search_url = u'https://api.deezer.com/search?q={0}'.format(unicode(get_search_edit))
        print search_url

        self.load_json(search_url)

        #json_url = urllib.urlopen(search_url)
        #data = json.load(json_url)

        # -------------get-values-from-json-file----------------

        art_id_list = []
        art_name_list = []
        art_picture_small_list = []
        art_tracklist_list = []

        alb_id_list = []
        alb_title_list = []
        alb_cover_small_list = []

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

            sng_id = data["data"][i]["id"]
            sng_id_list.append(sng_id)

            sng_title = data["data"][i]["title"]
            sng_title_list.append(sng_title)

        # ---------remove-duplicates-from-lists---------------

        global art1_lists
        art1_lists = [art_id_list] + [art_name_list] + [art_picture_small_list] + [art_tracklist_list]
        i1 = len(art1_lists) - 1
        art_lists = [self.unique(art1_lists[i1]) for art1_lists[i1] in art1_lists[:]]
        # art_id_list, art_name_list, art_picture_small_list, art_tracklist_list = art_lists

        # global  alb_lists
        alb_lists = [alb_id_list] + [alb_title_list] + [alb_cover_small_list]
        i2 = len(alb_lists) - 1
        alb_lists = [self.unique(alb_lists[i2]) for alb_lists[i2] in alb_lists[:]]
        # alb_id_list, alb_title_list, alb_cover_small_list = alb_lists

        sng_lists = [sng_id_list] + [sng_title_list]
        i3 = len(sng_lists) - 1
        sng_lists = [self.unique(sng_lists[i3]) for sng_lists[i3] in sng_lists[:]]
        # sng_id_list, sng_title_list = sng_lists

        # --------------add-elements-to-lists-----------------

        [parent.artList.addItem(i) for i in art1_lists[1]]
        [parent.albList.addItem(i) for i in alb_lists[1]]
        [parent.sngList.addItem(i) for i in sng_lists[1]]

    def artist(self, parent):

        get_artist = QtCore.QString(unicode(parent.artList.currentRow()))
        get_artist_name = QtCore.QString(unicode(parent.artList.currentItem().text()))

        get_art_tracklist = art1_lists[3][int(get_artist)]

        print(u"Search for {0}'s albums.".format(unicode(get_artist_name)))

        parent.albList.clear()
        parent.sngList.clear()

        self.load_json(get_art_tracklist)

        #json_url = urllib.urlopen(get_art_tracklist)
        #data = json.load(json_url)

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

        global alb2_lists
        alb2_lists = [alb_id_list] + [alb_title_list] + [alb_tracklist_list]
        i2 = len(alb2_lists) - 1
        alb_lists = [self.unique(alb2_lists[i2]) for alb2_lists[i2] in alb2_lists[:]]
        # alb_id_list, alb_title_list = alb_lists

        sng_lists = [sng_id_list] + [sng_title_list]
        i3 = len(sng_lists) - 1
        sng_lists = [self.unique(sng_lists[i3]) for sng_lists[i3] in sng_lists[:]]
        # sng_id_list, sng_title_list = sng_lists

        # --------------add-elements-to-lists-----------------

        [parent.albList.addItem(i) for i in alb_lists[1]]
        [parent.sngList.addItem(i) for i in sng_lists[1]]

    def album(self, parent):

        get_album = QtCore.QString(unicode(parent.albList.currentRow()))
        get_album_name = QtCore.QString(unicode(parent.albList.currentItem().text()))

        get_alb_tracklist = alb2_lists[2][int(get_album)]

        print(u"Search for tracks from {0}.".format(unicode(get_album_name)))

        parent.sngList.clear()

        self.load_json(get_alb_tracklist)

        #json_url = urllib.urlopen(get_album_tracklist)
        #data = json.load(json_url)

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

        sng_lists = [sng_id_list] + [sng_title_list]
        i3 = len(sng_lists) - 1
        sng_lists = [self.unique(sng_lists[i3]) for sng_lists[i3] in sng_lists[:]]
        # sng_id_list, sng_title_list = sng_lists

        # --------------add-elements-to-list-----------------

        [parent.sngList.addItem(i) for i in sng_lists[1]]

    def play_album(self, parent):

        get_alb = QtCore.QString(unicode(parent.albList.currentRow()))
        get_album_name = QtCore.QString(unicode(parent.albList.currentItem().text()))

        get_alb_id = alb2_lists[0][int(get_alb)]
        print(u"Play tracks from {0}.".format(unicode(get_album_name)))

        parent.show_bottom_panel()

        artist_player_url = 'http://www.deezer.com/plugins/player?format=classic&autoplay=false&playlist=true&' \
                            'width=700&height=350&color=007FEB&layout=dark&size=medium&type=album&id=%s&' \
                            'title=&app_id=1' % get_alb_id
        parent.classicWebView.setUrl(QtCore.QUrl(artist_player_url))
