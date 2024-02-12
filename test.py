"""
Data Preprocessing
Date : 12th Feb 2024
Author : S R Rayhan
"""

import numpy as np
import matplotlib as plt
import pandas as pd


dataset = pd.read_csv('Dataset.csv')
X = dataset.iloc[:,:-1]
Y = dataset.iloc[:,3]


#missing value handled by mean
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(X.iloc[:,1:3])
X.iloc[:,1:3] = imputer.transform(X.iloc[:,1:3])


#missing value handled by median
XX = dataset.iloc[:,:-1]
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='median')
imputer.fit(XX.iloc[:,1:3])
XX.iloc[:,1:3] = imputer.transform(XX.iloc[:,1:3])


#missing value handled by most frequent
XXX = dataset.iloc[:,:-1]
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
imputer.fit(XXX.iloc[:,1:3])
XXX.iloc[:,1:3] = imputer.transform(XXX.iloc[:,1:3])


#Using labelencoder for transferring string value to numarical value
from sklearn.preprocessing import LabelEncoder
labelEncoder_X = LabelEncoder()
X.iloc[:,0] = labelEncoder_X.fit_transform(X.iloc[:,0])

