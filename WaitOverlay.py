from PyQt4 import QtCore, QtGui

__author__ = 'postrowski'

# -*-coding: utf-8-*-


class WaitOverlay(QtGui.QWidget):
    def __init__(self):

        super(WaitOverlay, self).__init__()

        self.painter = QtGui.QPainter()
        self.timer = self.startTimer(30)
        self.counter = 5
        self.c = 0

    @staticmethod
    def switch(x):
        """
            Switch rectangle by key.
        :param x: dictionary key
        :return: rectangle
        """
        return {
            '1': 'painter.drawRect((self.width() / 2) - 29, (self.height() / 2), 10, -16)',
            '2': 'painter.drawRect((self.width() / 2) - 17, (self.height() / 2), 10, -10)',
            '3': 'painter.drawRect((self.width() / 2) - 5, (self.height() / 2), 10, -23)',
            '4': 'painter.drawRect((self.width() / 2) + 7, (self.height() / 2), 10, -16)',
            '5': 'painter.drawRect((self.width() / 2) + 19, (self.height() / 2), 10, -26)',
            '6': 'painter.drawRect((self.width() / 2) + 31, (self.height() / 2), 10, -16)'
        }[x]

    def paintEvent(self, event):
        """
            Paint overlay.
        :param event: event
        :return: None
        """
        painter = QtGui.QPainter()
        painter.begin(self)

        # background color
        painter.fillRect(event.rect(), QtGui.QBrush(QtGui.QColor('#c0c0c0')))

        # rectangle color
        painter.setBrush(QtGui.QColor('#a0a0a0'))

        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setPen(QtGui.QPen(QtCore.Qt.NoPen))

        eval(self.switch('1'))
        eval(self.switch('2'))
        eval(self.switch('3'))
        eval(self.switch('4'))
        eval(self.switch('5'))
        eval(self.switch('6'))
        self.draw(painter)
        painter.end()

    def draw(self, painter):
        """
            Draw overlay.
        :param painter: painter
        :return: None
        """
        # rectangle color
        painter.setBrush(QtGui.QColor('#303030'))

        for i in range(self.counter):
            if self.c is 1:
                eval(self.switch('1'))
            elif self.c is 2:
                eval(self.switch('1'))
                eval(self.switch('2'))
            elif self.c is 3:
                eval(self.switch('1'))
                eval(self.switch('2'))
                eval(self.switch('3'))
            elif self.c is 4:
                eval(self.switch('1'))
                eval(self.switch('2'))
                eval(self.switch('3'))
                eval(self.switch('4'))
            elif self.c is 5:
                eval(self.switch('1'))
                eval(self.switch('2'))
                eval(self.switch('3'))
                eval(self.switch('4'))
                eval(self.switch('5'))
            elif self.c is 6:
                eval(self.switch('1'))
                eval(self.switch('2'))
                eval(self.switch('3'))
                eval(self.switch('4'))
                eval(self.switch('5'))
                eval(self.switch('6'))

    def timerEvent(self, event):
        """
            Timer event.
        :param event: event
        :return: None
        """
        # loop counting to 5
        self.counter += 1
        if self.counter is 7:
            self.counter = 0

        # loop number
        if self.counter is 5:
            self.c += 1
            self.update()

        # rerun loop
        if self.c is 7:
            self.counter = 5
            self.c = 0

        # # end loop
        # if self.c is 7:
        #     self.killTimer(self.timer)
        #     self.hide()
