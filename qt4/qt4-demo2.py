#!/usr/bin/env python
# coding=utf-8
"""Example Qt4 Application"""
__author__ = 'tim@linfiniti.com'
__revision__ = '$Format:%H$'
__date__ = '27/05/2013'
__copyright__ = 'Copyright 2013, Tim Sutton'

import sys
from PyQt4 import Qt, QtGui


class HelloApp(Qt.QApplication):

    def __init__(self, args):
        Qt.QApplication.__init__(self, args)
        self.widget = QtGui.QWidget(None)
        self.layout = QtGui.QVBoxLayout(self.widget)
        self.button = QtGui.QPushButton("Click me", self.widget)
        self.label = QtGui.QLabel('Waiting...', self.widget)
        self.widget.setLayout(self.layout)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)
        # Call our slot (callback) when ever the button is pressed.
        self.connect(self.button, Qt.SIGNAL("clicked()"), self.slot)
        self.widget.show()

    def slot(self):
        self.label.setText('Hello, World!')

if __name__ == "__main__":
    app = HelloApp(sys.argv)
    app.exec_()
