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
from sklearn.metrics import r2_score
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
    print('r2 score: ' + str(r2))
    # f1 = f1_score(y_test, prediction, average='macro')
    # acc = model.score(X_test, y_test)
    # prec = precision_score(y_true=y_test, y_pred=prediction, average='macro')
    # recall = recall_score(y_true=y_test, y_pred=prediction, average='macro')


