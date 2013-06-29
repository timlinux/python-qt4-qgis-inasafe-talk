path = '/tmp/landsat.tif'
layer = QgsRasterLayer(path, 'Landsat')
QgsMapLayerRegistry.instance().addMapLayers([layer])
