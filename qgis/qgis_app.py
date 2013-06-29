#!/usr/bin/env python
# coding=utf-8
"""Example Qt4 Application"""
__author__ = 'tim@linfiniti.com'
__revision__ = '$Format:%H$'
__date__ = '27/05/2013'
__copyright__ = 'Copyright 2013, Tim Sutton'

import sys
import os
from PyQt4 import QtGui
from qgis.core import (
    QgsApplication,
    QgsRasterLayer,
    QgsProviderRegistry,
    QgsMapLayerRegistry)
from qgis.gui import QgsMapCanvas

from dialog_base import Ui_DialogBase


class Dialog(QtGui.QWidget, Ui_DialogBase):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.widget = QgsMapCanvas()
        self.show()

    def on_pushButton_clicked(self):
        """Wow - an autoconnected slot!"""
	print 'Click!'
        myPath = os.path.join(
            os.path.dirname(__file__),
            'landsat.tif')
        print myPath
        layer = QgsRasterLayer(myPath, 'A Layer')
        QgsMapLayerRegistry.instance().addMapLayers([layer])
        layer.setGrayBandName(layer.bandName(1))
        layer.setDrawingStyle(QgsRasterLayer.SingleBandPseudoColor)
        layer.setColorShadingAlgorithm(QgsRasterLayer.PseudoColorShader)
        layer.saveDefaultStyle() 
        self.widget.zoomToFullExtent()
        print self.widget.extent().toString()
        print layer.extent().toString()
	self.widget.refresh()

if __name__ == "__main__":
    gui_flag = True  # our app has a gui
    app = QgsApplication(sys.argv, gui_flag)
    # Note: This block is not needed for  QGIS > 1.8 which will
    # automatically check the QGIS_PREFIX_PATH var so it is here
    # for backwards compatibility only
    #if 'QGIS_PREFIX_PATH' in os.environ:
    #    myPath = os.environ['QGIS_PREFIX_PATH']
    #else:
    #    myPath = '/Applications/QGIS.app/contents/MacOS'
    # True == check our path for providers
    #app.setPrefixPath(myPath, True)
    app.initQgis()
    print app.showSettings()
    for item in QgsProviderRegistry.instance().providerList():
        print str(item)

    dialog = Dialog()
    app.exec_()
    app.exitQgis()
