from qgis.core import QgsExpression, QgsProject     ## For use in Qgis
from qgis.utils import qgsfunction                  ## For use in Qgis
from pathlib import Path
from urllib.request import urlopen
import json

group_name = 'BrandGIS'                             ## For use in Qgis

def initBrandGisSmhiFunctions():                    ## For use in Qgis
    QgsExpression.registerFunction(getForcastHtml)
    QgsExpression.registerFunction(getForcastDict)

def unloadBrandGisSmhiFunctions():                  ## For use in Qgis
    QgsExpression.unregisterFunction('getForcastHtml')
    QgsExpression.unregisterFunction('getForcastDict')
    
def fileJsonNoContent():
        emptyDict = {'SmhiWeather':{},
                    'SmhiFireDaily':{},
                    'SmhiFireHourly':{}
                    }
        # emptyDict = {'SmhiWeather':{'latlon1':{'approvedtime1':{'timeseries1':{'para1':['x','1','2'],'para2':['y','1','2']},
        #                                                         'timeseries2':{'para1':['x','1','2'],'para2':['y','1','2']}}},
        #                             'latlon2':{'approvedtime1':{'timeseries1':{'para1':['x','1','2'],'para2':['y','1','2']},
        #                                                         'timeseries2':{'para1':['x','1','2'],'para2':['y','1','2']}},
        #                                        'approvedtime2':{'timeseries1':{'para1':['x','1','2'],'para2':['y','1','2']},
        #                                                         'timeseries2':{'para1':['x','1','2'],'para2':['y','1','2']}}}},
        #              'SmhiFireDaily':{'latlon1':{'approvedtime':{'timeseries1':{'para1':['x','1','2'],'para2':['y','1','2']}}}},
        #              'SmhiFireHourly':{'latlon1':{'approvedtime':{'timeseries1':{'para1':['x','1','2'],'para2':['y','1','2']}}}}
        #              }

        return emptyDict

def filePathJson():                                 ## For use in Qgis

    qgis = QgsProject.instance().absolutePath()
    filename = 'smhiForcasts'
    path = 'brandgis_1_resurser/gemensamma_resurser/smhi'
    fileType = 'json'

    filePath = f'{qgis}/{path}/{filename}.{fileType}'
    filePath = Path(filePath)
    print(filePath)

    return filePath

# def filePathJson():                               ##For use in Esri ArcGIS

#     filePath = Path(__file__).parent / "smhiForcasts.json"

#     print(filePath)

#     return filePath

def createJsonFile():
    from pathlib import Path
    import json

    filePath = filePathJson()
    fileContent = fileJsonNoContent()

    Path(filePath).parent.mkdir(parents=True, exist_ok=True)

    with open(filePath, 'w', encoding='utf-8') as f:
        f.write(json.dumps(fileContent, indent=4))

def readJsonFile():

    filePath = filePathJson()
    if Path(filePath).is_file() is False:

        createJsonFile()

    else:
        pass

    with open(filePath, 'r', encoding='utf-8') as f:
        dataOrig = json.load(f)

    return dataOrig

def writeJsonFile(fileContent):

    filePath = filePathJson()

    with open(filePath, 'w', encoding='utf-8') as f:
        f.write(json.dumps(fileContent, indent=4))

        print('Filen är uppdaterades med nya prognoser')

def lonLat(longitude, latitude):
    '''
    Input:longitude, latitude in WGS84 String or number.
    Output:List with rounded cooridinates.
    '''

    longitude = str(round(float(longitude),2))
    latitude = str(round(float(latitude),2))

    return [longitude, latitude]

def lonLatString(lonLatList):
    '''
    Creates a string from lonLat for are used to store data in Jsonfile and for reading Jsonfile.
    '''
    lonLatString = '_'.join(lonLatList)
    return lonLatString

def getSmhiWeather(lonLatList):
    '''
    Input: longitude, latitude (Cordinates in wgs84, EPSG:4326).
    Output: Response from Smhi API, Meteorological Forecasts
    '''
    
    urlApi = f'api/category/pmp3g/version/2/geotype/point/lon/{lonLatList[0]}/lat/{lonLatList[1]}/data.json'
    urlSmhi = 'https://opendata-download-metfcst.smhi.se/'

    response = None
    # print(f'{urlSmhi}{urlApi}')
    try:
        response = urlopen(f'{urlSmhi}{urlApi}')
    except Exception as ex:
        print(ex, ': Kan inte hämta prognos, getSmhiWeather()')
    else:
        body = response.read()
        forcast = json.loads(body)
      
        return  [forcast, lonLatList]
    finally:
        if response is not None:
            response.close()

def getSmhiFireDaily(lonLatList):
    '''
    Input: longitude, latitude (Cordinates in wgs84, EPSG:4326). Conditional name of POI.
    Output: response from Smhi API
 
    '''

    smhiPeriod = 'daily'
    urlApi = f'api/category/fwif1g/version/1/{smhiPeriod}/geotype/point/lon/{lonLatList[0]}/lat/{lonLatList[1]}/data.json'
    urlSmhi = 'https://opendata-download-metfcst.smhi.se/'
    
    response = None
    # print(f'{urlSmhi}{urlApi}')
    try:
        response = urlopen(f'{urlSmhi}{urlApi}')
    except Exception as ex:
        print(ex, ': Kan inte hämta prognos, getSmhiFireDaily()')
    else:
        body = response.read()
        forcast = json.loads(body)
      
        return  [forcast, lonLatList]
    finally:
        if response is not None:
            response.close()

def getSmhiFireHourly(lonLatList):
    '''
    Input: longitude, latitude (Cordinates in wgs84, EPSG:4326). Conditional name of POI.
    Output: response from Smhi API
 
    '''

    smhiPeriod = 'hourly'
    urlApi = f'api/category/fwif1g/version/1/{smhiPeriod}/geotype/point/lon/{lonLatList[0]}/lat/{lonLatList[1]}/data.json'
    urlSmhi = 'https://opendata-download-metfcst.smhi.se/'

    response = None
    # print(f'{urlSmhi}{urlApi}')
    try:
        response = urlopen(f'{urlSmhi}{urlApi}')
    except Exception as ex:
        print(ex, ': Kan inte hämta prognos, getSmhiFireHourly()')
    else:
        body = response.read()
        forcast = json.loads(body)
      
        return  [forcast, lonLatList]
    finally:
        if response is not None:
            response.close()

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
    if type(degrees) == str:
        return 'No data'
    
    else:

        if degrees <= 360 and degrees >= 0:

            directionsText = {'0.0':'N',
                            '22.5':'NNO',
                            '45.0':'NO',
                            '67.5':'ONO',
                            '90.0':'O',
                            '112.5':'OSO',
                            '135.0':'SO',
                            '157.5':'SSO',
                            '180.0':'S',
                            '202.5':'SSV',
                            '225.0':'SV',
                            '247.5':'VSV',
                            '270.0':'V',
                            '292.5':'VNV',
                            '315.0':'NV',
                            '337.5':'NNV',
                            '360.0':'N'
                            } 
            directionsDegrees = [float(x) for x in directionsText.keys()] ## Creates a list of Keys from dictonary
            closest =  min(directionsDegrees,key=lambda x:abs(x-degrees)) ## Get closest key
            
            return directionsText[str(closest)] ## Get short name from dict
        else:
            return 'No data'

def formatSmhiWheaterResponse(forcast):

    lonlatKey = lonLatString(forcast[1])
    lonlatResponse = forcast[0]['geometry']['coordinates'][0]
    approvedTimeKey = forcast[0]['approvedTime']

    
    
    lonlatDict = {}
    approvedTimeDict = {}
    timeSerieDict = {}
    for time in forcast[0]['timeSeries']:
        
        paramDict = {}
        wind = ''
        gust = ''
        for param in time['parameters']:


            if param['name'] == 't':
                paramDict['Temp'] = str(round(param['values'][0]))

            elif param['name'] == 'pmean':
                paramDict['Pmean'] = str(round(param['values'][0]))

            elif param['name'] == 'r':
                paramDict['RelativeHumidity'] = str(round(param['values'][0]))

            elif param['name'] == 'ws':
                wind = str(round(param['values'][0]))
                paramDict['WindSpeed'] = str(round(param['values'][0]))

            elif param['name'] == 'gust':
                paramDict['Gust'] = str(round(param['values'][0]))
                gust = str(round(param['values'][0]))

            elif param['name'] == 'wd':
                paramDict['WindDirection'] = getDirectionShortname(param['values'][0])         
            else:
                pass
            paramDict['Wind'] = f'{wind}({gust})'
            paramDict['CoordinatesString'] = f'{round(lonlatResponse[0],4)}, {round(lonlatResponse[1],4)}'

        timeSerieDict[time['validTime']] = paramDict
    approvedTimeDict[approvedTimeKey] = timeSerieDict
    lonlatDict[lonlatKey] = approvedTimeDict


    return lonlatDict

def formatSmhiFireDailyResponse(forcast):

    lonlatKey = lonLatString(forcast[1])
    lonlatResponse = forcast[0]['geometry']['coordinates'][0]
    approvedTimeKey = forcast[0]['approvedTime']

    
    
    lonlatDict = {}
    approvedTimeDict = {}
    timeSerieDict = {}
    for time in forcast[0]['timeSeries']:
        
        paramDict = {}
        wind = ''
        gust = ''
        for param in time['parameters']:


            if param['name'] == 'fwi':
                paramDict['Fwi'] = str(round(param['values'][0]))
            elif param['name'] == 'fwiindex':
                paramDict['Fwiindex'] = str(round(param['values'][0]))
            elif param['name'] == 'isi':
                paramDict['Isi'] = str(round(param['values'][0]))
            elif param['name'] == 'ffmc':
                paramDict['Ffmc'] = str(round(param['values'][0]))
            elif param['name'] == 'bui':
                paramDict['Bui'] = str(round(param['values'][0]))
            elif param['name'] == 'dmc':
                paramDict['Dmc'] = str(round(param['values'][0])) 
            elif param['name'] == 'dc':
                paramDict['Dc'] = str(round(param['values'][0]))        
            else:
                pass
            paramDict['CoordinatesString'] = f'{round(lonlatResponse[0],3)}, {round(lonlatResponse[1],3)}'


        timeSerieDict[time['validTime']] = paramDict
    approvedTimeDict[approvedTimeKey] = timeSerieDict
    lonlatDict[lonlatKey] = approvedTimeDict


    return lonlatDict

def formatSmhiFireHourlyResponse(forcast):

    lonlatKey = lonLatString(forcast[1])
    lonlatResponse = forcast[0]['geometry']['coordinates'][0]
    approvedTimeKey = forcast[0]['approvedTime']

    
    
    lonlatDict = {}
    approvedTimeDict = {}
    timeSerieDict = {}
    for time in forcast[0]['timeSeries']:
        
        paramDict = {}
        wind = ''
        gust = ''
        for param in time['parameters']:


            if param['name'] == 'fwi':
                paramDict['Fwi'] = str(round(param['values'][0]))
            elif param['name'] == 'fwiindex':
                paramDict['Fwiindex'] = str(round(param['values'][0]))
            elif param['name'] == 'isi':
                paramDict['Isi'] = str(round(param['values'][0]))
            elif param['name'] == 'ffmc':
                paramDict['Ffmc'] = str(round(param['values'][0]))
            elif param['name'] == 'bui':
                paramDict['Bui'] = str(round(param['values'][0]))
            elif param['name'] == 'dmc':
                paramDict['Dmc'] = str(round(param['values'][0])) 
            elif param['name'] == 'dc':
                paramDict['Dc'] = str(round(param['values'][0]))        
            else:
                pass
            paramDict['CoordinatesString'] = f'{round(lonlatResponse[0],3)}, {round(lonlatResponse[1],3)}'


        timeSerieDict[time['validTime']] = paramDict
    approvedTimeDict[approvedTimeKey] = timeSerieDict
    lonlatDict[lonlatKey] = approvedTimeDict


    return lonlatDict

def listQuerrytimes():
    '''
    Returns validtimes and 6,12,24,30,36,54,78 hours from today 08:00.
    Output: List
    '''
    from datetime import datetime, timedelta

    qTimeseries = []
    dateshift = [0,6,12,24,30,36,52,76]
    present = datetime.now()
    startValue = present.replace(hour=8,minute=0,second=0,microsecond=0)
    for shift in dateshift:
        x = startValue+timedelta(hours=shift)
        qTimeseries.append(x.strftime("%Y-%m-%dT%H:%M:%SZ"))

    return qTimeseries

def tabelDates(validtimeList):
    '''
    Input: List with timestamps from API response.
    Output: Creates a list with dates from valid times. It is for use in tabel. The first 6 positions in list with strings, format Year-Month-Day, position 6-8 format Month-Day
    '''
    from datetime import datetime


    dates = []
    for vTime in validtimeList:
        if vTime == '-':
            dates.append(vTime)
        else:
            if vTime in validtimeList[0:6]:
                
                x = datetime.strptime(vTime,'%Y-%m-%dT%H:%M:%SZ')
                dates.append(x.strftime('%Y-%m-%d'))

            elif vTime in validtimeList[6:8]:
                
                x = datetime.strptime(vTime,'%Y-%m-%dT%H:%M:%SZ')
                dates.append(x.strftime('%m-%d'))
        

    return dates

def tabelTimes(validtimeList):
    '''
    Input: List with timestamps from API response.
    Output: Creates a list with dates from valid times. It is for use in tabel. Format Hour:Minutes
    '''
    from datetime import datetime


    times = []

    for vTime in validtimeList:
        if vTime == '-':
            times.append(vTime)
        else:
            x = datetime.strptime(vTime,'%Y-%m-%dT%H:%M:%SZ')
            times.append(x.strftime('%H:%M'))

    return times

def loadToJsonFile(forcastType,fileContent,formattedForcast, posString):


    fCoord = list(formattedForcast.keys())
    fApprovedTime = list(formattedForcast[fCoord[0]].keys())

    if bool(set(fileContent[forcastType]).intersection(set(fCoord))) is False:
        fileContent[forcastType][fCoord[0]] = formattedForcast.get(fCoord[0])
        print(f'Koordinater finns inte i filen för platsen: {posString} i {forcastType}')
        writeJsonFile(fileContent)
    elif bool(set(fileContent[forcastType]).intersection(set(fCoord))) is True:
        print(f'Koordinater finns redan i filen för platsen: {posString} i {forcastType}')

        if bool(set(fileContent[forcastType][fCoord[0]]).intersection(set(fApprovedTime))) is False:
            fileContent[forcastType][fCoord[0]][fApprovedTime[0]] = formattedForcast[fCoord[0]].get(fApprovedTime[0])
            print(f'Approvedtime finns inte i filen för platsen: {posString} i {forcastType}')
            writeJsonFile(fileContent)

        elif bool(set(fileContent[forcastType][fCoord[0]]).intersection(set(fApprovedTime))) is True:
            print(f'Approvedtime finns redan i filen för platsen: {posString} i {forcastType}')            

def closestApprovedTime(approvedTimesList):
    '''
    Input: List with approvedtimes
    Output: String with closest time to present.
    '''
    from datetime import datetime

    datetime_list = []

    for dt in approvedTimesList:
        datetime_list.append(datetime.strptime(dt,'%Y-%m-%dT%H:%M:%SZ'))

    return datetime.strftime(max(datetime_list),'%Y-%m-%dT%H:%M:%SZ')

def runLoad(longitude, latitude):
    
    pos = lonLat(longitude, latitude)
    posString = lonLatString(pos)
    try:
        fileContent = readJsonFile()
        w = getSmhiWeather(pos)
        formattedForcastW = formatSmhiWheaterResponse(w)
        forcastType = 'SmhiWeather'
        loadToJsonFile(forcastType, fileContent, formattedForcastW, posString)
    except:
        print('Kunde inte hämta väder från API')
    try: 
        fileContent = readJsonFile()
        fd = getSmhiFireDaily(pos)
        formattedForcastfh = formatSmhiFireDailyResponse(fd)
        forcastType = 'SmhiFireDaily'
        loadToJsonFile(forcastType, fileContent, formattedForcastfh, posString)
    except:
        print('Kunde inte hämta bransrisk (daglig) från API')
    try:
        fileContent = readJsonFile()
        fh = getSmhiFireHourly(pos)
        formattedForcastfh = formatSmhiFireHourlyResponse(fh)
        forcastType = 'SmhiFireHourly'
        loadToJsonFile(forcastType, fileContent, formattedForcastfh, posString)
    except:
        print('Kunde inte hämta bransrisk (timme) från API')

def noData():
    qValidTimesLen = 8
    noData = '-'
    qDict = {
        'dates':[noData] * qValidTimesLen,      
        'datesTime':[noData] * qValidTimesLen,    
        'validTimes':[noData] * qValidTimesLen,
        'airTemp':[noData] * qValidTimesLen,
        'relativeHumidity':[noData] * qValidTimesLen,
        'gust':[noData] * qValidTimesLen,
        'winDirection':[noData] * qValidTimesLen,
        'windSpeed':[noData] * qValidTimesLen,
        'wind':[noData] * qValidTimesLen,
        'pmean':[noData] * qValidTimesLen,
        'fwi':[noData] * qValidTimesLen,
        'isi':[noData] * qValidTimesLen,
        'ffmc':[noData] * qValidTimesLen,
        'bui':[noData] * qValidTimesLen,
        'dmc':[noData] * qValidTimesLen,
        'dc':[noData] * qValidTimesLen,
        'meteorologicalApprovedTime':noData,
        'fireApprovedTimeDaily':noData,
        'fireApprovedTimeHourly':noData,
        'coordinatesResponse':[noData,noData]
        }
    return qDict

def runRead(longitude, latitude):

    pos = lonLat(longitude, latitude)
    posString = lonLatString(pos)
    fileContent = readJsonFile()

    #SmhiWeather
    w = list(fileContent['SmhiWeather'][posString].keys())
    latestApprovedTimeW = closestApprovedTime(w)
    cw = fileContent['SmhiWeather'][posString][latestApprovedTimeW]
    #SmhiFireHourly
    fh = list(fileContent['SmhiFireHourly'][posString].keys())
    latestApprovedTimeFh = closestApprovedTime(fh)
    cfh = fileContent['SmhiFireHourly'][posString][latestApprovedTimeFh]
    #SmhiFireDaily
    fd = list(fileContent['SmhiFireDaily'][posString].keys())
    latestApprovedTimeFd = closestApprovedTime(fd)
    cfd = fileContent['SmhiFireDaily'][posString][latestApprovedTimeFd]    
    

    qValidTimes = listQuerrytimes()
    qValidTimesLen = len(qValidTimes)
 

    noData = '-'
    qDict = {
        'dates':[noData] * qValidTimesLen,        # ['today yyyy-mm-dd','today yyyy-mm-dd','today yyyy-mm-dd', 'today+1day yyyy-mm-dd','today+1day yyyy-mm-dd','today+1day yyyy-mm-dd', 'today+2day mm-dd','today+3day mm-dd'],
        'datesTime':[noData] * qValidTimesLen,    # hh:mm
        'validTimes':[noData] * qValidTimesLen,
        'airTemp':[noData] * qValidTimesLen,
        'relativeHumidity':[noData] * qValidTimesLen,
        'gust':[noData] * qValidTimesLen,
        'winDirection':[noData] * qValidTimesLen,
        'windSpeed':[noData] * qValidTimesLen,
        'wind':[noData] * qValidTimesLen,
        'pmean':[noData] * qValidTimesLen,
        'fwi':[noData] * qValidTimesLen,
        'isi':[noData] * qValidTimesLen,
        'ffmc':[noData] * qValidTimesLen,
        'bui':[noData] * qValidTimesLen,
        'dmc':[noData] * qValidTimesLen,
        'dc':[noData] * qValidTimesLen,
        'meteorologicalApprovedTime':noData,
        'fireApprovedTimeDaily':noData,
        'fireApprovedTimeHourly':noData,
        'coordinatesResponse':[noData,noData]
        }
    
    qDict['validTimes'] = qValidTimes
    qDict['meteorologicalApprovedTime'] = latestApprovedTimeW
    qDict['fireApprovedTimeDaily'] = latestApprovedTimeFd
    qDict['fireApprovedTimeHourly'] = latestApprovedTimeFh
    qDict['dates'] = tabelDates(qDict['validTimes'])
    qDict['datesTime'] = tabelTimes(qDict['validTimes'])
    
    for y in qDict['validTimes']:
        ind = qDict['validTimes'].index(y)
        try:
            qDict['airTemp'][ind] = cw[y]['Temp']
            qDict['relativeHumidity'][ind] = cw[y]['RelativeHumidity']
            qDict['winDirection'][ind] = cw[y]['WindDirection']
            qDict['wind'][ind] = cw[y]['Wind']
            qDict['pmean'][ind] = cw[y]['Pmean']
            qDict['gust'][ind] = cw[y]['Gust']
            qDict['windSpeed'][ind] = cw[y]['WindSpeed']

            if ind <= 5:
                qDict['fwi'][ind] = cfh[y]['Fwi']
                qDict['isi'][ind] = cfh[y]['Isi']
                qDict['ffmc'][ind] = cfh[y]['Ffmc']
                qDict['bui'][ind] = cfh[y]['Bui']
                qDict['dmc'][ind] = cfh[y]['Dmc']
                qDict['fwi'][ind] = cfh[y]['Fwi']
                qDict['dc'][ind] = cfh[y]['Dc']

            elif ind >= 6:
                qDict['fwi'][ind] = cfd[y]['Fwi']
                qDict['isi'][ind] = cfd[y]['Isi']
                qDict['ffmc'][ind] = cfd[y]['Ffmc']
                qDict['bui'][ind] = cfd[y]['Bui']
                qDict['dmc'][ind] = cfd[y]['Dmc']
                qDict['fwi'][ind] = cfd[y]['Fwi']
                qDict['dc'][ind] = cfd[y]['Dc']

            qDict['coordinatesResponse'] = cw[y]['CoordinatesString'].split(', ')

        except:
            None

    return qDict

def htmltabeldata(rowlist):
    td = '''<td width="25 px">{0}</td>'''
    tdx = ''.join([td.format(a) for a in rowlist])
    return tdx 

def htmlTabel(forcastDict):

    startBody = '''<!DOCTYPE html>
    <html>
    <head>
    <style>
    table, td, th {
    border: 1px solid black;
    border-color: #cccccc;
    font-family: Arial, Helvetica, sans-serif;font-size:70%;
    }

    th, td {
    padding: 1px;
    text-align: center;
    border-color: #F4F6F6;
    }

    table {
    border-collapse: collapse;
    width: auto;
    
    }

    </style>
    </head>
    <body>'''

    endBody = '''</body>
    </html>'''


    html = '''
    <table>
    <tr>
        <th colspan="2"; style="border-top-style: hidden; border-left-style: hidden; border-right-style: hidden;"></th>
        <th colspan="3"; style="border-top-style: hidden; border-left-style: hidden; border-right-style: hidden;">{date1}</th>
        <th colspan="3"; style="border-top-style: hidden; border-left-style: hidden; border-right-style: hidden;">{date2}</th>
        <th style="border-top-style: hidden; border-left-style: hidden; border-right-style: hidden;">{date3}</th>
        <th style="border-top-style: hidden; border-left-style: hidden; border-right-style: hidden;">{date4}</th>
    </tr>
    <tr>
        <td style="text-align: right;font-weight:bold">Tid</td>
        <td></td>
        {time}
    </tr>
    <tr style = "background-color: #f7f7f7;">
        <td style="text-align: right;font-weight:bold">Luft temp.</td>
        <td>(°C)</td>
        {temp}
    </tr>
    <tr>
        <td style="text-align: right;font-weight:bold">Nederbörd</td>
        <td>(mm/h)</td>
        {pmean}
    </tr>
    <tr style = "background-color: #f7f7f7;">
        <td style="text-align: right;font-weight:bold">Relativ fukt.</td>
        <td>(%)</td>
        {relativeHumidity}
    </tr>  
    <tr>
        <td style="text-align: right;font-weight:bold">Vind(by)</td>
        <td>(m/s)</td>
        {wind}
    </tr>
    <tr style = "background-color: #f7f7f7;">
        <td style="text-align: right;font-weight:bold">Vindriktning</td>
        <td>(från)</td>
        {winDirection}
    </tr>
    <tr>
        <td style="text-align: right;font-weight:bold">FWI</td>
        <td></td>
        {fwi}
    </tr>  
    <tr style = "background-color: #f7f7f7;">
        <td style="text-align: right;text-decoration:underline;">ISI</td>
        <td></td>
        {isi}
    </tr>
    <tr>
        <td style="text-align: right;">FFMC</td>
        <td></td>
        {ffmc}
    </tr>   
    <tr style = "background-color: #f7f7f7;">
        <td style="text-align: right;text-decoration:underline;">BUI</td>
        <td></td>
        {bui}
    </tr>
    <tr>
        <td style="text-align: right;">DMC</td>
        <td></td>
        {dmc}
    </tr> 
    <tr style = "background-color: #F8F9F9;">
        <td style="text-align: right;">DC</td>
        <td></td>
        {dc}
    </tr>  
    <tr>
        <td colspan="8"; style="text-align: left; border-bottom-style: hidden; border-left-style: hidden; border-right-style: hidden; font-size:50%">Väderprognos utfärdades kl {MeteorologicalApprovedTime} av SMHI (Timprognos)</td>
        <td colspan="2"; style="text-align: left; border-bottom-style: hidden; border-left-style: hidden; border-right-style: hidden; font-size:50%">(WGS 84: </td>
    </tr>  
    <tr>
        <td colspan="8"; style="text-align: left; border-bottom-style: hidden; border-left-style: hidden; border-right-style: hidden; font-size:50%">Brandriskprognos utfärdades kl {FireApprovedTime} av SMHI (Dygnsprognos)
        <td colspan="2"; style="text-align: left; border-bottom-style: hidden; border-left-style: hidden; border-right-style: hidden; font-size:50%">{LonLat})</td>
    </td>
    </tr> 
    </table>
    '''

    tabel = html.format(date1 = forcastDict['dates'][2],
                    date2 = forcastDict['dates'][5],
                    date3 = forcastDict['dates'][6],
                    date4 = forcastDict['dates'][7],
                    MeteorologicalApprovedTime = forcastDict['meteorologicalApprovedTime'],
                    FireApprovedTime = forcastDict['fireApprovedTimeDaily'],
                    time = htmltabeldata(forcastDict['datesTime']),
                    temp = htmltabeldata(forcastDict['airTemp']),
                    pmean = htmltabeldata(forcastDict['pmean']),
                    relativeHumidity = htmltabeldata(forcastDict['relativeHumidity']),
                    wind = htmltabeldata(forcastDict['wind']),
                    winDirection = htmltabeldata(forcastDict['winDirection']),
                    fwi = htmltabeldata(forcastDict['fwi']),
                    isi = htmltabeldata(forcastDict['isi']),
                    ffmc = htmltabeldata(forcastDict['ffmc']),
                    bui = htmltabeldata(forcastDict['bui']),
                    dmc = htmltabeldata(forcastDict['dmc']),
                    dc = htmltabeldata(forcastDict['dc']),
                    LonLat = ', '.join([forcastDict['coordinatesResponse'][0][:6],forcastDict['coordinatesResponse'][1][:6]])
                    )

    htmldok = ''.join([startBody, tabel, endBody])

    return htmldok

@qgsfunction(args='auto', group=group_name)                                             ##For use in Qgis
def getForcastDict(longitude, latitude, feature, parent):
    """
    Html tabel with wheater and fireforcasts for the location.
    Input coordinates in Wgs84

    <h4>Syntax</h4>
    <p><b>getForcastDict</b>(<i>14.92, 57.67</i>)</p>

    <h4>Example usage</h4>
    <ul>
      <li><b> getForcastDict( $x ,$y)['airTemp'][1]</li>
      <li><b>map_akeys( getForcastDict( $x ,$y))</li>

      <li>&rarr; Returns a dictionary with current forcast</li>
    </ul>
    """
    try:
        runLoad(longitude, latitude) #Loading new data to Jsonfile from Smhi APIs.
    except:
        print('Kunde inte hämta någon ny prognos')
    try:
        data = runRead(longitude, latitude) #Retreving data from Jsonfile as Dict
    except:
        data = noData()

    return data
@qgsfunction(args='auto', group=group_name)                                             ##For use in Qgis
def getForcastHtml(longitude, latitude, feature, parent):
    """
    Html tabel with wheater and fireforcasts for the location.
    Input coordinates in Wgs84

    <h4>Syntax</h4>
    <p><b>getForcastHtml</b>(<i>14.92, 57.67</i>)</p>

    <h4>Example usage</h4>
    <ul>
      <li><b> getForcastHtml( x(transform( centroid(map_get( item_variables('Karta1'), 'map_extent')),map_get( item_variables('Karta1'), 'map_crs'),'EPSG:4326')), y(transform( centroid(map_get( item_variables('Karta1'), 'map_extent')),map_get( item_variables('Karta1'), 'map_crs'),'EPSG:4326')))</li>
      <li>&rarr; Htmltabel</li>
    </ul>
    """
    try:
        runLoad(longitude, latitude) #Loading new data to Jsonfile from Smhi APIs.
    except:
        print('Kunde inte hämta någon ny prognos')
    try:
        data = runRead(longitude, latitude) #Retreving data from Jsonfile as Dict
    except:
        data = noData()
    return htmlTabel(data)

# def getForcastDict(longitude, latitude):                                              ##For use in Esri ArcGIS
#     try:
#         runLoad(longitude, latitude) #Loading new data to Jsonfile from Smhi APIs.
#     except:
#         print('Kunde inte hämta någon ny prognos')
#     try:
#         data = runRead(longitude, latitude) #Retreving data from Jsonfile as Dict
#     except:
#         data = noData()

#     return data

# def getForcastHtml(longitude, latitude):                                                ##For use in Esri ArcGIS
#     try:
#         runLoad(longitude, latitude) #Loading new data to Jsonfile from Smhi APIs.
#     except:
#         print('Kunde inte hämta någon ny prognos')
#     try:
#         data = runRead(longitude, latitude) #Retreving data from Jsonfile as Dict
#     except:
#         data = noData()
#     return htmlTabel(data)