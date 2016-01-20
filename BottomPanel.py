__author__ = 'postrowski'

# -*-coding: utf-8-*-

from PyQt4 import QtCore

class BottomPanel(object):

    def __init__(self, parent):

        self.classicLabel = parent.classicLabel
        self.classicWebView = parent.classicWebView
        self.hideBottomPanelButton = parent.hideBottomPanelButton
        self.geometry = parent.geometry
        self.width = parent.width
        self.height = parent.height
        self.showBottomPanelButton = parent.showBottomPanelButton
        self.animation = parent.animation

    def show_bottom_panel(self):

        self.classicLabel.show()
        self.classicWebView.show()
        self.hideBottomPanelButton.show()

        self.classicWebView.resize(self.classicLabel.width(), self.classicLabel.height())

    def hide_bottom_panel(self):

        self.classicLabel.hide()

        self.animation.setDuration(100)
        self.animation.setStartValue(QtCore.QRect(self.geometry().x(), self.geometry().y(),
                                                  self.width(), self.height()))
        self.animation.setEndValue(QtCore.QRect(self.geometry().x(), self.geometry().y(),
                                                self.width(), self.height() - self.classicLabel.height()))
        self.animation.start()

    def hide_bottom_panel_button_clicked(self):

        self.hide_bottom_panel()
        self.hideBottomPanelButton.hide()
        self.showBottomPanelButton.show()

    def show_bottom_panel_button_clicked(self):

        self.show_bottom_panel()
        self.hideBottomPanelButton.show()
        self.showBottomPanelButton.hide()
