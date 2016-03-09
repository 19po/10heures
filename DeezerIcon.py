from PyQt4 import QtGui
import webbrowser

__author__ = 'postrowski'

# -*-coding: utf-8-*-


class DeezerIcon(object):

    def __init__(self, parent):

        self.iconLabel = parent.iconLabel
        self.timer = parent.timer

    def hover_button(self):

        if self.iconLabel.underMouse():
            self.timer.start(10)
            pixmap = QtGui.QPixmap("images/icon_hover.svg")
            self.iconLabel.setPixmap(pixmap)
        else:
            pixmap = QtGui.QPixmap("images/icon.svg")
            self.iconLabel.setPixmap(pixmap)

    def click_button(self):

        if self.iconLabel.underMouse():
            self.timer.start(200)
            pixmap = QtGui.QPixmap("images/icon_clicked.svg")
            self.iconLabel.setPixmap(pixmap)
            webbrowser.open(str("http://www.deezer.com"), new=1, autoraise=True)
        else:
            pixmap = QtGui.QPixmap("images/icon.svg")
            self.iconLabel.setPixmap(pixmap)
