#!/usr/bin/env python
# coding=utf-8
"""Example Qt4 Application"""
__author__ = 'tim@linfiniti.com'
__revision__ = '$Format:%H$'
__date__ = '27/05/2013'
__copyright__ = 'Copyright 2013, Tim Sutton'

import sys
from PyQt4 import Qt, QtGui
from dialog_base import Ui_DialogBase


class Dialog(QtGui.QWidget, Ui_DialogBase):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.show()

    def on_pushButton_clicked(self):
        """Wow - an autoconnected slot!"""
        self.label.setText('Hello, World!')

if __name__ == "__main__":
    app = Qt.QApplication(sys.argv)
    dialog = Dialog()
    app.exec_()
