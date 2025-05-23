# from qgis.core import QgsExpression, QgsProject     ## For use in Qgis
# from qgis.utils import qgsfunction                  ## For use in Qgis
# from pathlib import Path
from datetime import datetime
from urllib.request import urlopen
import json
from pprint import pprint


class dialogSmhi:
       


    def lonLat(longitude, latitude):
        '''
        Input:longitude, latitude in WGS84 String or number.
        Output:List with rounded cooridinates.
        '''

        longitude = str(round(float(longitude),3))
        latitude = str(round(float(latitude),3))

        return [longitude, latitude]

    def getDirectionShortname(degrees):
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

    def getSmhiValidTimes():
        '''
        Gets valid times for forcasts
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



    def getSmhiWeather(longitude, latitude, validTime):
        '''
        Input: longitude, latitude (Cordinates in wgs84, EPSG:4326).
        Output: Response from Smhi API, Meteorological Forecasts
        '''
        lonLatList= dialogSmhi.lonLat(longitude, latitude)
        
        urlApi = f'api/category/pmp3g/version/2/geotype/point/lon/{lonLatList[0]}/lat/{lonLatList[1]}/data.json'
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

            for x in forcast['timeSeries']:
               if x['validTime'] == validTime:
                    y = datetime.strptime(x['validTime'],'%Y-%m-%dT%H:%M:%SZ')
                    wheaterDict['validTime'] = y.strftime('%Y-%m-%d %H:%M')

                    for para in x['parameters']:
                        # print(para)
                        if para['name'] == 'wd':
                            wheaterDict[para['name']] = str(round(para['values'][0]))
                            wheaterDict['vindriktning'] = dialogSmhi.getDirectionShortname(para['values'][0])
                        elif para['name'] == 'ws':
                            wheaterDict[para['name']] = str(round(para['values'][0]))
                            vind = str(round(para['values'][0]))
                        elif para['name'] == 'gust':
                            wheaterDict[para['name']] = str(round(para['values'][0]))
                            by = str(round(para['values'][0]))

            wheaterDict['vindtext'] = f'{vind}({by})'
                   


  
        
            
        finally:
            if response is not None:
                
                response.close()
                return wheaterDict
            





    def get_nearest_time(time_list):
        l = []
        for x in time_list:
            l.append(datetime.strptime(x, '%Y-%m-%dT%H:%M:%SZ'))

        current_time = datetime.now()
        nearest_time = min(l, key=lambda t: abs(t - current_time))
        return nearest_time.strftime('%Y-%m-%d %H:%M')
    
    def timeToSmhiTime(timeString):
        x = datetime.strptime(timeString, '%Y-%m-%d %H:%M')
        return x.strftime('%Y-%m-%dT%H:%M:%SZ')
    


            




