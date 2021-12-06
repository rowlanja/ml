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
        x.append([int(x) for x in splt[1:25]])
        y.append(int(splt[0]))

x = np.array(x)
y = np.array(y)

mean_error = []
std_error = []
#c_range = [0.0001, 0.0005, 0.001, 0.005, 0.01]
c_range = [0.0000001, 0.0001, 0.0005, 0.001, 0.0015, 0.002]
#c_range = [10, 100, 500, 1000, 5000, 10000]

linear_m = True
if linear_m:
    model= LinearRegression()
     
    train_features,test_features,train_labels,test_labels = train_test_split(x,y,test_size=0.20,random_state=0)
    print(len(test_features))
    model.fit(train_features, train_labels)
    y_pred = model.predict(test_features)

    x_domain = []
    y_domain = []
    associated_fairness = []
    for features,pred_label,actual_label in zip(test_features,y_pred, test_labels):
        features = features[3:24]
        x_domain.append("D{}".format(np.where(features == 1)[0][0] + 1))
        y_domain.append(pred_label)
        associated_fairness.append((actual_label/pred_label) - 1)
    # -- PLOTTING --
    cm = plt.cm.get_cmap('cool')

    plt.scatter(x_domain, y_domain, c=associated_fairness,vmin=np.amin(associated_fairness), vmax=np.amax(associated_fairness), cmap =cm)
    plt.colorbar()
    plt.xlabel("Dublin Area")
    plt.ylabel("Price")      
    
   
else:
    for c in c_range:
        temp = []
        model = Lasso(alpha= 1 / (2 * c))
        #model = Ridge(alpha= 1 / (2 * c))
        kf = KFold(n_splits=5)
        for train, test in kf.split(x):
            model.fit(x[train], y[train])
            y_pred = model.predict(x[test])
            temp.append(mean_squared_error(y[test], y_pred))
        mean_error.append(np.array(temp).mean())
        std_error.append(np.array(temp).std())



#plt.errorbar(c_range, mean_error, yerr=std_error, ecolor="red")
#plt.xlabel("Lasso - C")
#plt.ylabel("Mean square error")
plt.show()