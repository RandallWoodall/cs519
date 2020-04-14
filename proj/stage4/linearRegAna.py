# -*- coding: utf-8 -*-
"""
April 2020

Feature extraction and linear regression analysis.

@author: EmrahSariboz
"""

import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd  
import seaborn as sns 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

plt.figure(figsize = (20,16))
sns.set()

dataset = pd.read_csv("cleanedData.csv")

dataset = dataset.iloc[:, 1:]

correlation_matrix = dataset.corr().round(2)

plt.figure(figsize = (20,16))
sns.heatmap(data=correlation_matrix, annot=True, linewidths=.5)
plt.show()

corr_target = abs(correlation_matrix['power'])


relevant_features = corr_target [corr_target >= 0.5]
relevant_features

'''

The features of linear regression should not have multi-co-lineraty. For example there is 
strong relation between solarRadiation and uvHigh. 
Thus, there is not need to include both. 
Once we check this relation for every attributes, we remain with following attributes
'''

relevant_features = ['solarRadiation', 'tempHigh']

X = pd.DataFrame(dataset[relevant_features])

Y = dataset.power


#The relationship of solarRadiation and tempHigh with a power
plt.figure(figsize=(16,8))

for i, col in enumerate(relevant_features):
    plt.subplot(1, len(relevant_features) , i+1)
    x = X[col]
    y = dataset.power
    plt.scatter(x, y, marker='.')
    plt.title(col)
    plt.xlabel(col)
    plt.ylabel('power')
    


#Train-test split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state=41)

#Applying the linear reg
lin_model = LinearRegression(normalize=True)
lin_model.fit(X_train, Y_train)


#model prediction
# model evaluation for training set
y_train_predict = lin_model.predict(X_train)


y_test_predict = lin_model.predict(X_test)

r2_train = r2_score(Y_train, y_train_predict)

r2_test = r2_score(Y_test, y_test_predict)

print('The r2 score on training ', r2_train)

print('The r2 score on testing ', r2_test)

