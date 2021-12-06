import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split, KFold
from sklearn.preprocessing import PolynomialFeatures

data = open("DublinDataset.csv", "r")
next(data)

x = []
y = []

for line in data:
    if line != "\n":
        splt = line.strip().split(",")
        x.append([int(splt[1]), int(splt[2]), int(splt[3]), int(splt[4])])
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
print("Linear Regresion MSE = ", mean_squared_error(y_train, y_pred, squared=False))

y_pred = modelLasso.predict(x_train)
print("Lasso MSE = ", mean_squared_error(y_train, y_pred, squared=False))

y_pred = modelRidge.predict(x_train)
print("Ridge MSE = ", mean_squared_error(y_train, y_pred, squared=False))

y_pred = modelBaseline.predict(x_train)
print("Baseline MSE = ", mean_squared_error(y_train, y_pred, squared=False))