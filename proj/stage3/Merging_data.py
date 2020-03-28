import glob
import os
import pandas as pd
list_files = os.listdir("weather_data")
print(list_files)
data = open('Data' + '.csv', 'w')
for py in list_files:
    date = (py[-8:])
    files = glob.glob('*'+ str(date))
    print(files)
    col_Names=["time", "1", "2", "3", "4", "5", "6", "7", "8", "9","10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"
    ,"22", "23", "24", "25", "26"]
    weather = pd.read_csv(files[0],names= dict.fromkeys(col_Names , 1))
    weather_temp = (weather.iloc[:,0]).str.split(expand=True) 
    weather = pd.concat([weather_temp.iloc[:,1],weather.iloc[:,1:] ],axis=1,names= col_Names)
    weather.columns = col_Names
    power = pd.read_csv(files[1],header=None,names=["time","power"])
    result = pd.merge(weather, power, on='time', how='inner')
    result.to_csv("Data.csv",index=False, mode='a')
    #print(files)

#time_p =  (power.iloc[:,0:2])
#time_W = (weather.iloc[:,0]).str.split(expand=True)
#print(time_W[1][-8:-3])
#print(time_W[1])
data.close()

