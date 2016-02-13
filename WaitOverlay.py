__author__ = 'postrowski'

# -*-coding: utf-8-*-

from PyQt4 import QtCore, QtGui
from Search import Search

class WaitOverlay(QtGui.QWidget):
    def __init__(self, parent=None):

        QtGui.QWidget.__init__(self)
        self.painter = QtGui.QPainter()
        self.t = 120  # animation time
        self.counter = 0
        self.timer = self.startTimer(self.t / 1.6)  # <= t/2

    def paintEvent(self, event):

        self.painter.begin(self)
        self.painter.fillRect(event.rect(), QtGui.QBrush(QtGui.QColor('#c0c0c0')))
        self.draw()
        self.painter.end()

    def draw(self):

        self.painter.setRenderHint(QtGui.QPainter.Antialiasing)
        self.painter.setPen(QtGui.QPen(QtCore.Qt.NoPen))

        for i in range(3):  # color change speed: range(x); smaller x means faster
            if (self.counter / 2) % (i + 1) is i:  # i is integral: (x.0)
                self.painter.setBrush(QtGui.QColor('#303030'))
            else:  # i is floating: (x.5)
                self.painter.setBrush(QtGui.QColor('#a0a0a0'))

        self.painter.drawRect((self.width() / 2) - 29, (self.height() / 2), 10, -16)
        self.painter.drawRect((self.width() / 2) - 17, (self.height() / 2), 10, -10)
        self.painter.drawRect((self.width() / 2) - 5, (self.height() / 2), 10, -23)
        self.painter.drawRect((self.width() / 2) + 7, (self.height() / 2), 10, -16)
        self.painter.drawRect((self.width() / 2) + 19, (self.height() / 2), 10, -26)
        self.painter.drawRect((self.width() / 2) + 31, (self.height() / 2), 10, -16)

    def timerEvent(self, event):

        self.counter += 1
        self.update()  # repaint
        if self.counter is self.t:  # animation time
            self.killTimer(self.timer)
            self.hide()
