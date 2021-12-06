import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.model_selection import train_test_split, KFold
from sklearn.preprocessing import PolynomialFeatures

data = open("DublinDatasetObj2.csv", "r")
next(data)

x = []
y = []

for line in data:
    if line != "\n":
        splt = line.strip().split(",")
        x.append([int(splt[1]), int(splt[2]), int(splt[3]), int(splt[4]), int(splt[5]), int(splt[6]), int(splt[7]), int(splt[8]), 
        int(splt[9]), int(splt[10]), int(splt[11]), int(splt[12]), int(splt[13]), int(splt[14]), int(splt[15]), int(splt[16]), 
        int(splt[17]), int(splt[18]), int(splt[19]), int(splt[20]), int(splt[21]), int(splt[22]), int(splt[23]), int(splt[24])])
        y.append(int(splt[0]))

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=0)

modelLinear = LinearRegression()
modelLinear.fit(x_train, y_train)

modelLasso = Lasso(alpha= 1 /(2 * 0.001))
modelLasso.fit(x_train, y_train)

modelRidge = Ridge(alpha= 1 /(2 * 0.0001))
modelRidge.fit(x_train, y_train)

modelBaseline = DummyRegressor(strategy="mean")
modelBaseline.fit(x_train, y_train)

y_pred = modelLinear.predict(x_train)
#print("Linear Regresion MSE = ", mean_squared_error(y_test, y_pred, squared=False))
print("Linear Regresion MAE = ", mean_absolute_error(y_train, y_pred))
#print("Linear Regresion R2 = ", r2_score(y_train, y_pred))

y_pred = modelLasso.predict(x_train)
#print("Lasso MSE = ", mean_squared_error(y_test, y_pred, squared=False))
print("Lasso MAE = ", mean_absolute_error(y_train, y_pred))
#print("Lasso R2 = ", r2_score(y_train, y_pred))

y_pred = modelRidge.predict(x_train)
#print("Ridge MSE = ", mean_squared_error(y_test, y_pred, squared=False))
print("Ridge MAE = ", mean_absolute_error(y_train, y_pred))
#print("Ridge R2 = ", r2_score(y_train, y_pred))

y_pred = modelBaseline.predict(x_train)
#print("Baseline MSE = ", mean_squared_error(y_test, y_pred, squared=False))
print("Baseline MAE = ", mean_absolute_error(y_train, y_pred))
#print("Baseline R2 = ", r2_score(y_train, y_pred))