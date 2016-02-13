__author__ = 'postrowski'

# -*-coding: utf-8-*-

from PyQt4 import QtCore

class BottomPanel(object):

    def __init__(self, parent):

        self.classicWebView = parent.classicWebView
        self.showBottomPanelButton = parent.showBottomPanelButton
        self.hideBottomPanelButton = parent.hideBottomPanelButton
        self.geometry = parent.geometry
        self.width = parent.width
        self.height = parent.height

        self.animation = parent.animation

    def show_bottom_panel(self):

        self.animation.setDuration(300)
        self.animation.setStartValue(QtCore.QRect(self.geometry().x(), self.geometry().y(),
                                                  self.width(), self.height()))
        self.animation.setEndValue(QtCore.QRect(self.geometry().x(), self.geometry().y(),
                                                self.width(), self.classicWebView.height()))
        self.animation.start()

    def hide_bottom_panel(self):

        self.animation.setDuration(300)
        self.animation.setStartValue(QtCore.QRect(self.geometry().x(), self.geometry().y(),
                                                  self.width(), self.height()))
        self.animation.setEndValue(QtCore.QRect(self.geometry().x(), self.geometry().y(),
                                                self.width(), - self.classicWebView.height()))
        self.animation.start()

    def hide_bottom_panel_button_clicked(self):

        self.hide_bottom_panel()
        self.hideBottomPanelButton.hide()
        self.showBottomPanelButton.show()
        self.classicWebView.hide()

    def show_bottom_panel_button_clicked(self):

        self.show_bottom_panel()
        self.hideBottomPanelButton.show()
        self.showBottomPanelButton.hide()
        self.classicWebView.show()
