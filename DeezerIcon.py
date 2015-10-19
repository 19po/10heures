__author__ = 'postrowski'

# -*-coding: utf-8-*-

from PyQt4 import QtGui
import webbrowser


class DeezerIcon(object):

    def __init__(self, parent):

        self.iconLabel = parent.iconLabel
        self.timer = parent.timer

    def hover_button(self):

        if self.iconLabel.underMouse() is True:
            self.timer.start(10)
            pixmap = QtGui.QPixmap("icon_hover.ico")
            self.iconLabel.setPixmap(pixmap)
        else:
            pixmap = QtGui.QPixmap("icon.ico")
            self.iconLabel.setPixmap(pixmap)

    def click_button(self):

        if self.iconLabel.underMouse() is True:
            self.timer.start(200)
            pixmap = QtGui.QPixmap("icon_click.ico")
            self.iconLabel.setPixmap(pixmap)
            url = 'http://www.deezer.com'
            webbrowser.open(str(url), new=1, autoraise=True)
        else:
            pixmap = QtGui.QPixmap("icon.ico")
            self.iconLabel.setPixmap(pixmap)
