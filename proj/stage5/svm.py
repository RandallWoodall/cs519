# -*- coding: utf-8 -*-
"""
May 2020

SVM.

@author: Aya Elsayed
"""

import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd  
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error#RMSE
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error#MAE

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


#Applying the SVR_
SVR_ = SVR(kernel='sigmoid', degree=3, gamma='scale', coef0=0.0, tol=0.001,
 C=1.0, epsilon=0.1, shrinking=True, cache_size=200, verbose=False, max_iter=-1)
SVR_.fit(X_train, y_train)
y_train_pred = SVR_.predict(X_train)
y_test_pred = SVR_.predict(X_test)

r2 = r2_score(y_true=y_train, y_pred=y_train_pred)
print('r2 score for train data: ' + str(r2))
r2 = r2_score(y_true=y_test, y_pred=y_test_pred)
print('r2 score for test data: ' + str(r2))

RMSE = mean_squared_error(y_true=y_train, y_pred=y_train_pred)
print('RMSE score for train data: ' + str(RMSE))
RMSE = mean_squared_error(y_true=y_test, y_pred=y_test_pred)
print('RMSE score for test data: ' + str(RMSE))

MAE = mean_absolute_error(y_true=y_train, y_pred=y_train_pred)
print('MAE  score for train data: ' + str(MAE))
MAE = mean_absolute_error(y_true=y_test, y_pred=y_test_pred)
print('MAE  score for test data: ' + str(MAE))

