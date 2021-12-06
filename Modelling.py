import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.metrics import mean_squared_error
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

x = np.array(x)
y = np.array(y)

mean_error = []
std_error = []
#c_range = [0.0001, 0.0005, 0.001, 0.005, 0.01]
c_range = [0.0000001, 0.0001, 0.0005, 0.001, 0.0015, 0.002]
#c_range = [10, 100, 500, 1000, 5000, 10000]

for c in c_range:
    temp = []
    #model = LinearRegression()
    #model = Lasso(alpha= 1 / (2 * c))
    model = Ridge(alpha= 1 / (2 * c))
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