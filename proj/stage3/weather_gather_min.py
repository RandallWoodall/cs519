import requests
from requests.auth import HTTPBasicAuth
import json
import time
import datetime
from datetime import datetime
#from datatime import now
hourly_weather = [] #list of weather
import numpy as np

while(True):
    #hourly 7 days, params=[('q', 'requests+language:python')]
    responsetry = requests.get ('https://api.weather.com/v2/pws/observations/hourly/7day?stationId=KNMLASCR263&format=json&units=e&apiKey=33b111b523f94b80b111b523f9bb80b8', auth=HTTPBasicAuth('KNMLASCR263', 'N2miGFcR'))
    #each min each day
    current_min = requests.get ('https://api.weather.com/v2/pws/observations/current?stationId=KNMLASCR263&format=json&units=e&apiKey=33b111b523f94b80b111b523f9bb80b8', auth=HTTPBasicAuth('KNMLASCR263', 'N2miGFcR'))

    #forecast daily/5 days

    future_data = requests.get ('https://api.weather.com/v3/wx/forecast/daily/5day?geocode=32.28123,-106.753756&format=json&units=e&language=en-US&apiKey=33b111b523f94b80b111b523f9bb80b8')
    #print(future_data)

    print(current_min.status_code)
    
    time_stamp=(str(datetime.now()))
    time_stamp = time_stamp.replace(" ", "--") 
    time_stamp = time_stamp.replace(":", "-") 
    print(current_min.json())
    dict_ = current_min.json()
    def jprint(obj):
    # create a formatted string of the Python JSON object
        text = json.dumps(obj, sort_keys=False, indent= 4)
        print(text)

    jprint(current_min.json())
    output = open('solarData' + time_stamp + '.csv', 'w')
    for hour in dict_['observations']:
        output.write(hour['obsTimeLocal'] + ',' + str(hour['solarRadiation']) + ',' + str(hour['uv']) + ',' + str(
            hour['winddir']) + ',' + str(hour['humidity']) + ',' + str(hour['qcStatus'])
              + ',' + str(hour['imperial']['temp']) + ',' + str(hour['imperial']['heatIndex']) + ',' + str(
            hour['imperial']['dewpt']) + ',' + str(hour['imperial']['windChill'])
              + ',' + str(hour['imperial']['windSpeed']) + ',' + str(hour['imperial']['windGust']) + ',' + str(
            hour['imperial']['pressure']) + ',' + str(hour['imperial']['precipRate']) + ',' + str(
            hour['imperial']['precipTotal']))
    output.close()


   

    time.sleep(60)
