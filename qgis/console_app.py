#!/usr/bin/env python
# coding=utf-8
"""Example Qt4 Console Application"""
__author__ = 'tim@linfiniti.com'
__revision__ = '$Format:%H$'
__date__ = '27/05/2013'
__copyright__ = 'Copyright 2013, Tim Sutton'

import sys
import os

from qgis.core import (
    QgsApplication,
    QgsVectorLayer,
    QgsProviderRegistry)


if __name__ == "__main__":
    gui_flag = True  # our app has a gui
    app = QgsApplication(sys.argv, gui_flag)

    # Some OSX specific setup
    #path = '/Applications/QGIS.app/contents/MacOS'
    #os.environ['QGIS_PREFIX_PATH'] = path
    #app.setPluginPath('/Applications/QGIS.app/contents/PlugIns/qgis/')

    # Initilise QGIS and show its state
    app.initQgis()
    print app.showSettings()
    for item in QgsProviderRegistry.instance().providerList():
        print str(item)

    base_dir = os.path.dirname(__file__)
    layer_file = 'vector.shp'
    full_path = os.path.join(base_dir, layer_file)

    layer = QgsVectorLayer(full_path, 'some points', 'ogr')
    if layer.isValid():
        feature_count = layer.dataProvider().featureCount()
        print 'Your layer has %i features' % feature_count
    else:
        print 'Sorry layer is not valid!'
