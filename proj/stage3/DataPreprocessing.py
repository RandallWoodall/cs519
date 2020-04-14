#!/usr/bin/env python
# coding: utf-8


import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer



dataset = pd.read_csv("Data.csv", na_values=['None', ' nan'])



dataset.head()


print('Before removing the nan', dataset.shape)

dataset = dataset[dataset['power'].notna()]

print('After removing the nan', dataset.shape)


print('the percentage of the zeros in precipRate column' , dataset['precipRate'].isin([0]).sum() / dataset['precipRate'].shape[0])
print('the percentage of the zeros in precipTotal column' , dataset['precipTotal'].isin([0]).sum() / dataset['precipTotal'].shape[0])



dataset.drop(['precipRate','precipTotal'], axis=1, inplace=True)

dataset.head()

missing_columns = [col for col in dataset.columns if dataset[col].isna().any()]


smp = SimpleImputer(missing_values=np.nan, strategy='mean')
dataset[missing_columns] = smp.fit_transform(dataset[missing_columns])
print('Total number of missing values ', dataset.isna().any().sum())
print('The final shape of the dataset ', dataset.shape)
dataset.head()
dataset.to_csv("cleanedData.csv", header = True, index = False)



