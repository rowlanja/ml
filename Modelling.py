import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split, KFold
from sklearn.preprocessing import PolynomialFeatures

data = open("Dataset.csv", "r")
next(data)

x = []
y = []

for line in data:
    if line != "\n":
        splt = line.strip().split(",")
        x.append([int(splt[1]), int(splt[2]), int(splt[3]), int(splt[4])])
        y.append(int(splt[0]))

x = np.array(x)
y = np.array(y)

mean_error = []
std_error = []
c_range = [0.01, 0.05, 0.1, 0.5, 1]

for c in c_range:
    temp = []
    #model = LinearRegression()
    model = Lasso(alpha= 1 / (2 * c))
    #model = Ridge(alpha= 1 / (2 * c))
    kf = KFold(n_splits=5)
    for train, test in kf.split(x):
        model.fit(x[train], y[train])
        y_pred = model.predict(x[test])
        temp.append(mean_squared_error(y[test], y_pred))
    mean_error.append(np.array(temp).mean())
    std_error.append(np.array(temp).std())

plt.errorbar(c_range, mean_error, yerr=std_error, ecolor="red")
plt.xlabel("Ridge - C")
plt.ylabel("Mean square error")
plt.show()