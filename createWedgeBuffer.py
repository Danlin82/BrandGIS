from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QComboBox, QLabel

from qgis.core import *
from qgis.gui import *

from datetime import datetime, timedelta

from .layerStyle import wedgeLayerStyle

# Denna klass är en QgsMapTool som används för att skapa en buffert i form av en kil
# som representerar spridningen av en brand baserat på vindriktning, vindhastighet och tid.
class fireWedge(QgsMapTool):
    def __init__(self, iface):
        QgsMapTool.__init__(self, iface.mapCanvas())
        self.canvas = iface.mapCanvas()
        self.iface = iface

    # Denna metod returnerar en lista med möjliga vindhastigheter
    def spridningHastighet(self, returnType=None, speed=None):
        sh ={'3':300,
             '6':600,
             '8':900,
             '11':1200,
             '14':1500,
             '17':1800,
             '19':2100,
             '22':2400,
             '25':2700
             }
        if returnType is None and speed is None:
            sList = []
            for x in sh.keys():
                sList.append(f'{x} m/s')
            return sList
        elif returnType =='speed' and speed is not None:
           splitList = speed.split(' ')
           for x, y in sh.items():
                if x == splitList[0]:
                    return y

    # Denna metod returnerar en lista med möjliga vindriktningar
    def arrowDirection(self, dir=None):
        directionsarrow = {
            'N': 129107,
            'NNO': 8226,
            'NO': 129111,
            'ONO': 8226,
            'O': 129104,
            'OSO': 8226,
            'SO': 129108,
            'SSO': 8226,
            'S': 129105,
            'SSV': 8226,
            'SV': 129109,
            'VSV': 8226,
            'V': 129106,
            'VNV': 8226,
            'NV': 129110,
            'NNV': 8226}

        if dir is None:
            dwList = []
            for x, y in directionsarrow.items():
               dwList.append(f'{chr(y)} {x}')
            return dwList
   
        elif dir is not None and type(dir) is str:
            return f'{chr(directionsarrow[dir])} {dir}'
        else:
            return chr(8226)

    # Denna metod returnerar en lista med möjliga vindriktningar i text
    def windDir(self, returnType=None,dir=None):
        directionsText = {
            '0.0': 'N',
            '22.5': 'NNO',
            '45.0': 'NO',
            '67.5': 'ONO',
            '90.0': 'O',
            '112.5': 'OSO',
            '135.0': 'SO',
            '157.5': 'SSO',
            '180.0': 'S',
            '202.5': 'SSV',
            '225.0': 'SV',
            '247.5': 'VSV',
            '270.0': 'V',
            '292.5': 'VNV',
            '315.0': 'NV',
            '337.5': 'NNV',
            '360.0': 'N'
        }

        if returnType is None and dir is None:
            listX = []
            for x in directionsText.values():
                listX.append(x)

            lX = listX[0:-1]
            return lX
        
        elif returnType == 'dir':
           for x, y in directionsText.items():
                if y == dir:
                    # Adding 180 to get the correct direction
                    return float(x)+180
        elif returnType == 'reverseDict':
            return {v: k for k, v in directionsText.items()}
        
        elif returnType == 'dict':
            return directionsText
    
    # Denna metod returnerar en lista med möjliga tider
    def timeStamp(self):
        times = ['1','2','3','4','5','6','7','8','9','10']
        timesList = []
        now = datetime.now()
       
        for x in times:
            newTime = now + timedelta(hours=int(x))
            timesList.append(f'{x} h, {newTime.strftime("%Y-%m-%d %H:%M")}')
        return timesList
           

        
    # Denna metod öppnar en dialog där användaren kan välja vindriktning, vindhastighet och tid
    def openProject(self):

        items1 = self.arrowDirection()
        items2 = self.spridningHastighet()
        items3 = self.timeStamp()
        
        self.dialog = QDialog()
        self.dialog.setWindowTitle("Gissa brandspridningen")
        layout = QVBoxLayout(self.dialog)
        
        label1 = QLabel("Välj vilket vädersträck vinden kommer ifrån:")
        self.combo1 = QComboBox()
        self.combo1.addItems(items1)


        layout.addWidget(label1)
        layout.addWidget(self.combo1)
        
        label2 = QLabel("Välj vindstyrka:")
        self.combo2 = QComboBox()
        self.combo2.addItems(items2)
        layout.addWidget(label2)
        layout.addWidget(self.combo2)
        
        label3 = QLabel("Välj tid som ska beräknas:")
        self.combo3 = QComboBox()
        self.combo3.addItems(items3)
        layout.addWidget(label3)
        layout.addWidget(self.combo3)
        
        label4 = QLabel("<center><br><b>Beräkningen är bara en uppskattning<br> och måste kontrolleras! <br></b></center>")

        layout.addWidget(label4)

        
        button = QPushButton("Beräkna spridning")
        layout.addWidget(button)
        button.clicked.connect(self.on_button_clicked)
        self.createLayer = False

        self.dialog.exec_()

    # Denna metod anropas när användaren klickar på "Beräkna spridning"-knappen
    def on_button_clicked(self):
        self.createLayer = True
        item1 = self.combo1.currentText()
        item2 = self.combo2.currentText()
        item3 = self.combo3.currentText()
        self.dialog.accept()


    # Denna metod anropas när användaren klickar på kartan
    def canvasReleaseEvent(self, event):



        # Öppna dialogen för att välja vindriktning, vindhastighet och tid
        self.openProject()

        if self.createLayer is True:
            
            # Skapa ett nytt lager för att rita kilbufferten
            now = datetime.now()
            fireWedgeLayer = QgsVectorLayer('Polygon?crs=EPSG:3006', f'Beräknad kl {now.strftime("%H:%M")} spridning', 'memory')
            data_provider = fireWedgeLayer.dataProvider()
            data_provider.addAttributes([QgsField('text', QVariant.String),QgsField('spridning längd', QVariant.String), QgsField('frontFireTime', QVariant.String),QgsField('createTime',  QVariant.String),QgsField('startPoint',  QVariant.String)])
            fireWedgeLayer.updateFields()

            # Hämta koordinaterna för där användaren klickade
            punkt = p2 = self.toLayerCoordinates(fireWedgeLayer, event.pos())

            qgsPunkt = QgsPoint(punkt.x(), punkt.y())

            # Hämta de valda värdena från dialogen
            getDirection = self.combo1.currentText().split(' ')[1]
            combo1Direction = self.windDir(returnType='dir', dir=getDirection)
            combo2WindSpeed = self.spridningHastighet(returnType='speed', speed=self.combo2.currentText())
            combo3Time = int(self.combo3.currentText().split(' ')[0])
            fireFrontMeter = combo3Time*combo2WindSpeed

            # Skapa ett objekt för startpunkten
            startpunkt_objekt = QgsFeature()
            
            nowdelta = timedelta(hours=combo3Time)
            fireFrontTime = now + nowdelta
            

            # Skapa kilbufferten
            buff = QgsGeometry.createWedgeBuffer(qgsPunkt, combo1Direction, 90, fireFrontMeter, fireFrontMeter-(fireFrontMeter/10))
            startpunkt_objekt.setGeometry(buff)
            startpunkt_objekt.setAttributes([f'Vid vindhastigheten {self.combo2.currentText()} med riktning {self.combo1.currentText()} och efter {self.combo3.currentText()} timmar så beräknas branden spridits {fireFrontMeter} meter. Denna beräkning skall inte användas som en sanning',f'{fireFrontMeter} meter', fireFrontTime.strftime("%Y-%m-%d %H:%M"),now.strftime("%Y-%m-%d %H:%M"),qgsPunkt.asWkt()])
            fireWedgeLayer.dataProvider().addFeature(startpunkt_objekt)
            
            fireWedgeLayer.triggerRepaint()

            # Lägg till lagret i QGIS
            projectInst = QgsProject.instance()
            root = projectInst.layerTreeRoot()
            fireWedgeLayer.importNamedStyle(wedgeLayerStyle())
            projectInst.addMapLayer(fireWedgeLayer, False)
            root.insertLayer(0,fireWedgeLayer)
            self.iface.setActiveLayer(fireWedgeLayer)


            self.iface.mapCanvas().unsetMapTool(self)
        else:
            self.iface.mapCanvas().unsetMapTool(self)
