# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Randall Woodall
# April 2020
# CS 519
# Implementation of polynomial regression to try on our dataset.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

if __name__ == '__main__':
    data_set = pd.read_csv('cleanedData.csv')
    y = data_set['power'].values
    X = data_set.loc[:, data_set.columns.difference(['power', 'time'])].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3, random_state=1)
    poly = PolynomialFeatures(26)
    #poly.fit_transform(X_train, y_train)
    #poly.transform(X_test)

    model = LinearRegression()
    model.fit(X=X_train, y=y_train)

    prediction = model.predict(X=X_test)
    f1 = f1_score(y_test, prediction, average='macro')
    acc = model.score(X_test, y_test)
    prec = precision_score(y_true=y_test, y_pred=prediction, average='macro')
    recall = recall_score(y_true=y_test, y_pred=prediction, average='macro')

