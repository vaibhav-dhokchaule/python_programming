# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 14:53:35 2022

@author: HP
"""

#importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Height_Weight.csv')
X = dataset.iloc[:, :-1].values #get a copy of dataset exclude last column
y = dataset.iloc[:, 1].values #get array of dataset in column 1st

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Visualizing the Training set results
viz_train = plt
viz_train.scatter(X_train, y_train, color='red')
viz_train.plot(X_train, regressor.predict(X_train), color='blue')
viz_train.title('Weight VS Height (Training set)')
viz_train.xlabel('Height Of Person')
viz_train.ylabel('Weight Of Person')
viz_train.show()

# Visualizing the Test set results 
viz_test = plt 
viz_test.scatter(X_test, y_test, color='red') 
viz_test.plot(X_train, regressor.predict(X_train), color='blue') 
viz_test.title('Weight VS Height (Test set)') 
viz_test.xlabel('Height of Person') 
viz_test.ylabel('Weight') 
viz_test.show() 

# Predicting the result of 65cm height of person weight
y_pred  = regressor.predict(np.array([65]).reshape(1, 1))
print(y_pred)
