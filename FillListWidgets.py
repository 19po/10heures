__author__ = 'postrowski'

# -*-coding: utf-8-*-

def setup_sng_list(parent):

    parent.sngList.addItem("Item 1")
    parent.sngList.addItem("Item 2")

def setup_art_list(parent):

    parent.artList.addItem("Item 1")
    parent.artList.addItem("Item 2")

class FillListWidgets(object):

    def __init__(self, parent):

        setup_sng_list(parent)
        setup_art_list(parent)

