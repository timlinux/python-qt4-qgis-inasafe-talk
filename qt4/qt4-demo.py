# coding=utf-8
"""Example Qt4 Application"""

__author__ = 'tim@linfiniti.com'
__revision__ = '$Format:%H$'
__date__ = '27/05/2013'
__copyright__ = 'Copyright 2013, Tim Sutton'

import sys

from PyQt4 import Qt, QtGui

if __name__ == '__main__':
    app = Qt.QApplication(sys.argv)
    label = QtGui.QLabel('Hello world')
    label.show()
    sys.exit(app.exec_())
