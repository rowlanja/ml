import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
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
c_range = [0.001, 0.1, 1, 10]

for c in c_range:
    temp = []
    model = LogisticRegression(penalty="l2", C=c)
    kf = KFold(n_splits=5)
    for train, test in kf.split(x_poly):
        model.fit(x[train], y[train])
        y_pred = model.predict(x[test])
        temp.append(mean_squared_error(y[test], y_pred, squared=False))
    mean_error.append(np.array(temp).mean())
    std_error.append(np.array(temp).std())

plt.errorbar(c_range, mean_error, yerr=std_error, ecolor="red")
plt.xlabel("C")
plt.ylabel("Root mean square error")
#plt.xlim((0, 10.1))
#plt.xticks(np.arange(0, 10.01, 1))
plt.show()