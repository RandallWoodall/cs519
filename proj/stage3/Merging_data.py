import glob
import os
import pandas as pd
list_files = os.listdir("weather_data")
print(list_files)
data = open('Data' + '.csv', 'w')
H_flag = 1 #flag for puttingg header one time
for py in list_files:
    date = (py[-8:])
    files = glob.glob('*'+ str(date))
    print(files)
    col_Names=["time", "solarRadiation", "uvHigh", "winddirAvg", "humidityHigh", "humidityLow", "humidityAvg", "qcStatus", "tempHigh", "tempLow","tempAvg", "windspeedHigh", "windgustLow", "windspeedAvg", "dewptHigh", "dewptLow", "dewptAvg", "windchillHigh", "windchillAvg", "heatindexHigh"
    ,"heatindexLow", "heatindexAvg", "pressureMax", "pressureMin", "pressureTrend","precipRate","precipTotal"]
    weather = pd.read_csv(files[0],names= dict.fromkeys(col_Names , 1))
    weather_temp = (weather.iloc[:,0]).str.split(expand=True) 
    weather = pd.concat([weather_temp.iloc[:,1],weather.iloc[:,1:] ],axis=1,names= col_Names)
    weather.columns = col_Names
    power = pd.read_csv(files[1],header=None,names=["time","power"])
    result = pd.merge(weather, power, on='time', how='inner')
    if H_flag == 1:
        result.to_csv("Data.csv",index=False, mode='a')
    else:
        result.to_csv("Data.csv",index=False, mode='a',header=None)
    H_flag = 0
    #print(files)

#time_p =  (power.iloc[:,0:2])
#time_W = (weather.iloc[:,0]).str.split(expand=True)
#print(time_W[1][-8:-3])
#print(time_W[1])
data.close()

