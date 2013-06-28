# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_base.ui'
#
# Created: Fri Jun 28 11:00:57 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogBase(object):
    def setupUi(self, DialogBase):
        DialogBase.setObjectName(_fromUtf8("DialogBase"))
        DialogBase.resize(286, 164)
        self.gridLayout = QtGui.QGridLayout(DialogBase)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton = QtGui.QPushButton(DialogBase)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.widget = QtGui.QWidget(DialogBase)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(DialogBase)
        QtCore.QMetaObject.connectSlotsByName(DialogBase)

    def retranslateUi(self, DialogBase):
        DialogBase.setWindowTitle(QtGui.QApplication.translate("DialogBase", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("DialogBase", "Add layer", None, QtGui.QApplication.UnicodeUTF8))

