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
from sklearn.metrics import mean_squared_error#RMSE
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error#MAE
import sys

from my_pca import myPCA

if __name__ == '__main__':
    data_set = pd.read_csv('cleanedData.csv')
    y = data_set['power'].values
    X = data_set.loc[:, data_set.columns.difference(['power', 'time'])].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3, random_state=1)

    reducer = myPCA(n_components=int(sys.argv[1]))
    reducer.fit(X_train)
    reducer.transform(X_test)

    poly = PolynomialFeatures(int(sys.argv[1]))
    poly.fit_transform(X_train, y_train)
    poly.transform(X_test)

    model = LinearRegression()
    model.fit(X=X_train, y=y_train)

    prediction = model.predict(X=X_test)

    r2 = r2_score(y_true=y_test, y_pred=prediction)
    print('r2 score for train data: ' + str(r2))
    r2 = r2_score(y_true=y_train, y_pred=model.predict(X_train))
    print('r2 score for test data: ' + str(r2))

    RMSE = mean_squared_error(y_true=y_test, y_pred=prediction)
    print('RMSE score for train data: ' + str(r2))
    RMSE = mean_squared_error(y_true=y_train, y_pred=model.predict(X_train))
    print('RMSE score for test data: ' + str(r2))

    MAE = mean_absolute_error(y_true=y_test, y_pred=prediction)
    print('MAE  score for train data: ' + str(r2))
    MAE = mean_absolute_error(y_true=y_train, y_pred=model.predict(X_train))
    print('MAE  score for test data: ' + str(r2))
