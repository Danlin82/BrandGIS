from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QComboBox, QLabel

from qgis.core import *
from qgis.gui import *
from datetime import datetime, timedelta
from urllib.request import urlopen
import json
from .layerStyle import smhiLayerStyle


class smhiForcast(QgsMapTool):
    def __init__(self, iface):
        QgsMapTool.__init__(self, iface.mapCanvas())
        self.canvas = iface.mapCanvas()
        self.iface = iface

    def getDirectionShortname(self, degrees):
        r'''
        Input: Numeric value representing degrees 0/360 is North.
            - getDirShortname(23) => NNO
            - Swedish short name for NordNordOst
        ---------------------------------------------
        Output: Short name for direction
            - If input is a sting then output is 'No data'
            . if input is not in range 0-360 then output is 'No data'
        '''
        degrees = float(degrees)

        if type(degrees) == str:
            return 'No data'
        
        else:

            if degrees <= 360 and degrees >= 0:

                directionsText = {'0.0':'Norr',
                                '22.5':'Nord-Nordost',
                                '45.0':'Nordost',
                                '67.5':'Ost-Nordost',
                                '90.0':'Ost',
                                '112.5':'Ost-Sydost',
                                '135.0':'Sydost',
                                '157.5':'Syd-Sydost',
                                '180.0':'Syd',
                                '202.5':'Syd-Sydväst',
                                '225.0':'Sydväst',
                                '247.5':'Väst-Sydväst',
                                '270.0':'Väst',
                                '292.5':'Väst-Nordväst',
                                '315.0':'Nordväst',
                                '337.5':'Nord-Nordväst',
                                '360.0':'Norr'
                                }
                directionsDegrees = [float(x) for x in directionsText.keys()] ## Creates a list of Keys from dictonary
                closest =  min(directionsDegrees,key=lambda x:abs(x-degrees)) ## Get closest key
                
                return directionsText[str(closest)] ## Get short name from dict
            else:
                return 'No data'


    def timeToSmhiTime(self, timeString):
        try:
            x = datetime.strptime(timeString, '%Y-%m-%d %H:%M')
            return x.strftime('%Y-%m-%dT%H:%M:%SZ')
        except:
            return None
        
    def get_nearest_time(self, time_list):
        try:
            l = []
            for x in time_list:
                l.append(datetime.strptime(x, '%Y-%m-%d %H:%M'))

            current_time = datetime.now()
            nearest_time = min(l, key=lambda t: abs(t - current_time))
            return nearest_time.strftime('%Y-%m-%d %H:%M')
        except:
            pass

    def getSmhiValidTimes(self):
        '''
        Input: longitude, latitude (Cordinates in wgs84, EPSG:4326).
        Output: Response from Smhi API, Meteorological Forecasts
        '''
        
        urlApi = f'api/category/pmp3g/version/2/validtime.json'
        urlSmhi = 'https://opendata-download-metfcst.smhi.se/'

        response = None
        timeDict = {}

        try:
            response = urlopen(f'{urlSmhi}{urlApi}')
        except Exception as ex:
            print(ex, ': Kan inte hämta prognos, getSmhiValidTimes()')
            return timeDict
        else:
            body = response.read()
            forcast = json.loads(body)
            
            for x in forcast['validTime']:
                y = datetime.strptime(x,'%Y-%m-%dT%H:%M:%SZ')
                timeDict[y.strftime('%Y-%m-%d %H:%M')] = x

        finally:
            if response is not None:
                response.close()
                return timeDict
        
    def getSmhiWeather(self, longitude, latitude, validTime):
        '''
        Input: longitude, latitude (Cordinates in wgs84, EPSG:4326).
        Output: Response from Smhi API, Meteorological Forecasts
        '''
        
        urlApi = f'api/category/pmp3g/version/2/geotype/point/lon/{longitude}/lat/{latitude}/data.json'
        urlSmhi = 'https://opendata-download-metfcst.smhi.se/'

        response = None
        wheaterDict = {}
        try:
            response = urlopen(f'{urlSmhi}{urlApi}')

        except Exception as ex:
            
            print(ex, ': Kan inte hämta prognos, getSmhiWeather()')
            return wheaterDict
        
        else:
            body = response.read()
            forcast = json.loads(body)
            vind = ''
            by = ''
            aT = datetime.strptime(forcast['approvedTime'],'%Y-%m-%dT%H:%M:%SZ')
            wheaterDict['approvedTime'] = aT.strftime('%Y-%m-%d %H:%M:%S')
            for x in forcast['timeSeries']:
               if x['validTime'] == validTime:
                    y = datetime.strptime(x['validTime'],'%Y-%m-%dT%H:%M:%SZ')
                    wheaterDict['validTime'] = y.strftime('%Y-%m-%d %H:%M')

                    for para in x['parameters']:
                        if para['name'] == 'wd':
                            wheaterDict[para['name']] = str(round(para['values'][0]))
                            wheaterDict['vindriktning'] = self.getDirectionShortname(para['values'][0])
                        elif para['name'] == 'ws':
                            wheaterDict[para['name']] = str(round(para['values'][0]))
                            vind = str(round(para['values'][0]))
                        elif para['name'] == 'gust':
                            wheaterDict[para['name']] = str(round(para['values'][0]))
                            by = str(round(para['values'][0]))
                        elif para['name'] == 't':
                            wheaterDict['lufttemperatur'] = str(round(para['values'][0]))+' C'
                        elif para['name'] == 'r':
                            wheaterDict['relativ luftfuktighet'] = str(round(para['values'][0]))+' %'
                        elif para['name'] == 'msl':
                            wheaterDict['lufttryck'] = str(round(para['values'][0]))+' hPa'
                        elif para['name'] == 'pmean':
                            wheaterDict['genomsnittlig nederbörd'] = str(round(para['values'][0]))+' mm/h'
 

            wheaterDict['vindtext'] = f'{vind}({by})'
            return wheaterDict

    def openProject(self):

        self.dialog = QDialog()
        layout = QVBoxLayout(self.dialog)
        self.dialog.setWindowTitle("Smhi prognos")

        

        label3 = QLabel("Välj tid för aktuell prognos:")
        self.combo3 = QComboBox()
        self.combo3.addItems(self.items3)
        layout.addWidget(label3)
        layout.addWidget(self.combo3)
        self.combo3.setCurrentText(self.get_nearest_time(self.items3))
        
        

        button = QPushButton("Hämta från Smhi")
        layout.addWidget(button)
        button.setEnabled(self.smhiConnection)
        button.clicked.connect(self.on_button_clicked)
        self.createLayer = False
        
        self.dialog.exec_()

    def on_button_clicked(self):
        self.createLayer = True
        self.dialog.accept()


    # Denna metod anropas när användaren klickar på kartan
    def canvasReleaseEvent(self, event):

        items3Querry = self.getSmhiValidTimes()
        if len(items3Querry) == 0:
            self.items3 = ['Inget internet']
            self.smhiConnection = False
        else:
            self.items3 = items3Querry
            self.smhiConnection = True
        # Öppna dialogen för att välja vindriktning, vindhastighet och tid
        self.openProject()

        
        if self.smhiConnection is True and self.createLayer is True:
            
            projectInst = QgsProject.instance()
            now = datetime.now()
            smhiLayer = QgsVectorLayer('Point?crs=EPSG:3006', f'Hämtad prognos kl {now.strftime("%H:%M")} Smhi', 'memory')
            data_provider = smhiLayer.dataProvider()
            data_provider.addAttributes([QgsField('approvedTime', QVariant.String),
                                        QgsField('validTime', QVariant.String), 
                                        QgsField('vindriktning', QVariant.String),
                                        QgsField('vindtext',  QVariant.String),
                                        QgsField('wd',  QVariant.String),
                                        QgsField('ws',  QVariant.String),
                                        QgsField('gust',  QVariant.String),
                                        QgsField('lufttemperatur',  QVariant.String),
                                        QgsField('relativ luftfuktighet',  QVariant.String),
                                        QgsField('lufttryck',  QVariant.String),
                                        QgsField('genomsnittlig nederbörd',  QVariant.String),
                                        QgsField('wkt',  QVariant.String)

                                        ])
            smhiLayer.updateFields()

            ptMapXY = self.toMapCoordinates(event.pos())
            geomMap = QgsGeometry(QgsPoint(ptMapXY.x(),ptMapXY.y()))
            geomWgs84 = QgsGeometry(geomMap)
            sourceCrs = projectInst.crs()
            crsWgs84 = QgsCoordinateReferenceSystem("EPSG:4326")
            trWgs84 = QgsCoordinateTransform(sourceCrs, crsWgs84, projectInst)
            geomWgs84.transform(trWgs84)

            w = self.getSmhiWeather(round(geomWgs84.asPoint().x(),4), round(geomWgs84.asPoint().y(),4), self.timeToSmhiTime(self.combo3.currentText()))

            # Hämta koordinaterna för där användaren klickade
            punkt = self.toLayerCoordinates(smhiLayer, event.pos())
            qgsPunkt = QgsPoint(punkt.x(), punkt.y())

            startpunkt_objekt = QgsFeature()
            startpunkt_objekt.setGeometry(qgsPunkt)
            startpunkt_objekt.setAttributes([w['approvedTime'],
                                            w['validTime'],
                                            w['vindriktning'],
                                            w['vindtext'],
                                            w['wd'],
                                            w['ws'],
                                            w['gust'],
                                            w['lufttemperatur'],
                                            w['relativ luftfuktighet'],
                                            w['lufttryck'],
                                            w['genomsnittlig nederbörd'],
                                            qgsPunkt.asWkt()
                                            ])

            smhiLayer.dataProvider().addFeature(startpunkt_objekt)
            smhiLayer.triggerRepaint()

            # Lägg till lagret i QGIS
            smhiLayer.importNamedStyle(smhiLayerStyle(w['ws']))
            root = projectInst.layerTreeRoot()
            projectInst.addMapLayer(smhiLayer, False)
            root.insertLayer(0,smhiLayer)
            self.iface.setActiveLayer(smhiLayer)
            self.iface.mapCanvas().unsetMapTool(self)
        else:
            self.iface.mapCanvas().unsetMapTool(self)
            pass
