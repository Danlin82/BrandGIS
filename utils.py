from PyQt5.QtCore import QSettings, QVariant
from qgis.core import QgsApplication

def pluginSvgPath():
    print('hej')
    qgsProfilePath = QgsApplication.qgisSettingsDirPath()
    print(qgsProfilePath)
    newSvgPath = f'{qgsProfilePath}python/plugins/brand_gis/BrandgisSvg'
    qgsSvgaths = QSettings().value('svg/searchPathsForSVG')
    if newSvgPath in qgsSvgaths:
        print('svg path already in qgs settings')
        pass
    else:
        qgsSvgaths.append(newSvgPath)
        QSettings().setValue('svg/searchPathsForSVG', qgsSvgaths)
        print('svg path added to qgs settings')


#self.plugin_dir        

