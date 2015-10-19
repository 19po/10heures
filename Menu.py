__author__ = 'postrowski'

# -*-coding: utf-8-*-

from PyQt4 import QtGui


def menu(parent):
    menu_bar = parent.menuBar()
    menu_menu = menu_bar.addMenu("&Menu")

    menu_history = menu_menu.addMenu("History")
    today_action = QtGui.QAction("Today", parent)
    menu_history.addAction(today_action)
    month_action = QtGui.QAction("Month", parent)
    menu_history.addAction(month_action)
    year_action = QtGui.QAction("Year", parent)
    menu_history.addAction(year_action)

    menu_stat = menu_menu.addMenu("Statistics")
    favourites_action = QtGui.QAction("Favourites", parent)
    menu_stat.addAction(favourites_action)

    close_action = QtGui.QAction("Close", parent)
    close_action.setShortcut("Ctrl+Q")
    menu_menu.addAction(close_action)
    close_action.triggered.connect(parent.close)


class Menu(object):

    def __init__(self, parent):

        menu(parent)

