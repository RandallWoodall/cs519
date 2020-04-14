# -*- coding: utf-8 -*-
"""
April 2020

Random forest.

@author: Aya Elsayed
"""

import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd  
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler


# Loading our data set
data = pd.read_csv("cleanedData.csv")
x = data .iloc[:, 1:(data.shape[1]-1)].values
y = data .iloc[:, -1].values


# Splitting data into 70% training and 30% test data:
X_train,X_test,y_train, y_test = train_test_split(x,y, test_size=0.3, random_state=1)
# Standardizing the features:
sc = StandardScaler()
sc.fit(X_train)
X_train = sc.transform(X_train)
X_test= sc.transform(X_test)


#Applying the Random Forest
forest = RandomForestRegressor(n_estimators = 100 , random_state = 1)
forest = forest.fit(X_train, y_train)
y_train_pred = forest.predict(X_train)
y_test_pred = forest.predict(X_test)

r2 = r2_score(y_true=y_train, y_pred=y_train_pred)
print('r2 score for train data: ' + str(r2))
r2 = r2_score(y_true=y_test, y_pred=y_test_pred)
print('r2 score for test data: ' + str(r2))

