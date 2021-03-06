import requests
from requests.auth import HTTPBasicAuth
import json
import time
import datetime
hourly_weather = [] #list of weather
import numpy as np


#historical

day = np.array ([20200414,20200415,20200416,20200417,20200418,20200419,20200420,20200421,20200422,20200423,20200424
,20200425,20200426,20200427,20200428,20200429,20200430,20200501,20200502,20200503,20200504,20200505])

for i in range(day.size):

    old_data = requests.get ('https://api.weather.com/v2/pws/history/all?stationId=KNMLASCR263&format=json&units=e&date='+str(day[i])+'&apiKey=33b111b523f94b80b111b523f9bb80b8', auth=HTTPBasicAuth('KNMLASCR263', 'N2miGFcR'))
    #forecast daily/5 days

    print(old_data.status_code)

    print(old_data.json())
    dict_ = old_data.json()
    output = open('solarData' + str(day[i])+ '.csv', 'w')
    for hour in dict_['observations']:
        output.write(hour['obsTimeLocal'] + ',' + str(hour['solarRadiationHigh']) + ',' + str(hour['uvHigh']) + ',' + str(
            hour['winddirAvg']) + ',' + str(hour['humidityHigh']) + ',' + str(hour['humidityLow']) + ',' + str(
            hour['humidityAvg']) + ',' + str(hour['qcStatus'])
                + ',' + str(hour['imperial']['tempHigh']) + ',' + str(hour['imperial']['tempLow']) + ',' + str(
            hour['imperial']['tempAvg']) + ',' + str(hour['imperial']['windspeedHigh']) + ',' + str(
            hour['imperial']['windgustLow']) + ',' + str(hour['imperial']['windspeedAvg'])
                + ',' + str(hour['imperial']['dewptHigh']) + ',' + str(hour['imperial']['dewptLow']) + ',' + str(
            hour['imperial']['dewptAvg']) + ',' + str(hour['imperial']['windchillHigh']) + ',' + str(
            hour['imperial']['windchillAvg']) + ',' + str(hour['imperial']['heatindexHigh'])
                + ',' + str(hour['imperial']['heatindexLow']) + ',' + str(hour['imperial']['heatindexAvg']) + ',' + str(
            hour['imperial']['pressureMax']) + ',' + str(hour['imperial']['pressureMin']) + ',' + str(
            hour['imperial']['pressureTrend']) + ',' + str(hour['imperial']['precipRate'])
                + ',' + str(hour['imperial']['precipTotal']) + '\n')
    output.close()


    def jprint(obj):
        # create a formatted string of the Python JSON object
        text = json.dumps(obj, sort_keys=False, indent=4)
        print(text)


    #jprint(future_data.json())

  