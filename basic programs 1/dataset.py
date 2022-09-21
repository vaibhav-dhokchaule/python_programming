# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 21:31:17 2021

@author: HP
"""

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
import pandas as pd
from sklearn.impute import SimpleImputer
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
dataset = pd.read_csv ('Data.csv')
from sklearn.preprocessing import StandardScaler
x = dataset.iloc [:,:-1].values
y = dataset.iloc [:,-1].values  

imputer =SimpleImputer(missing_values=np.nan , strategy='mean')
imputer =imputer.fit (x[:, 1:])
x[:, 1 :] =imputer.transform (x[:, 1:])

labelencoder_X=LabelEncoder()
x[:,0]=labelencoder_X.fit_transform(x[:,0])
rg=ColumnTransformer([("Region",OneHotEncoder(),[0])],remainder='passthrough')
X=rg.fit_transform(x) 
labelencoder_Y=LabelEncoder()
Y=labelencoder_Y.fit_transform(y)  
X_train ,X_test ,Y_train ,Y_test = train_test_split(X,Y,test_size=0.2,random_state=0)
sc_X=StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)