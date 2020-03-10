import requests
from requests.auth import HTTPBasicAuth
import json
import time
import datetime
hourly_weather = [] #list of weather
import numpy as np

while(True):
    #hourly 7 days, params=[('q', 'requests+language:python')]
    responsetry = requests.get ('https://api.weather.com/v2/pws/observations/hourly/7day?stationId=KNMLASCR263&format=json&units=e&apiKey=33b111b523f94b80b111b523f9bb80b8', auth=HTTPBasicAuth('KNMLASCR263', 'N2miGFcR'))

    #forecast daily/5 days

    future_data = requests.get ('https://api.weather.com/v3/wx/forecast/daily/5day?geocode=32.28123,-106.753756&format=json&units=e&language=en-US&apiKey=33b111b523f94b80b111b523f9bb80b8')
    print(future_data)

    print(responsetry.status_code)

    print(responsetry.json())
    dict_ = responsetry.json()
    output = open('solarData' + str(datetime.date.today()) + '.csv', 'w')
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


    jprint(future_data.json())

    time.sleep(604800)