import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.dummy import DummyRegressor
from sklearn.model_selection import train_test_split

import csv

x = []
y = []
bedroomCountObj2 = []
bathroomCountObj2 = []

data = open("DublinDatasetObj2.csv", "r")
next(data)

for line in data:
    if line != "\n":
        # getting features for model
        splt = line.strip().split(",")
        bedroomCountObj2.append(int(splt[1]))
        bathroomCountObj2.append(int(splt[2]))
        x.append([int(splt[1]), int(splt[2]), int(splt[3]), int(splt[4]), int(splt[5]), int(splt[6]), int(splt[7]), int(splt[8]), 
        int(splt[9]), int(splt[10]), int(splt[11]), int(splt[12]), int(splt[13]), int(splt[14]), int(splt[15]), int(splt[16]), 
        int(splt[17]), int(splt[18]), int(splt[19]), int(splt[20]), int(splt[21]), int(splt[22]), int(splt[23]), int(splt[24])])
        y.append(int(splt[0]))

 
# opening the CSV file
with open('dublinDataset.csv', mode ='r')as file:
   
    # reading the CSV file
    csvFile = csv.reader(file)
    prices = []
    locations = []
    bedroomCount = []
    bathroomCount = []
    
    # displaying the contents of the CSV file
    for lines in csvFile:
        if len(lines) > 0:
            if lines[0] == 'price':continue
            prices.append(int(lines[0]))
            locations.append(lines[1])
            bedroomCount.append(lines[2])
            bathroomCount.append(lines[3])

    #x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=0)

    model = LinearRegression()
    model.fit(x, y)

    #model = Lasso(alpha= 1 /(2 * 0.001))
    #model.fit(x, y)

    #model = Ridge(alpha= 1 /(2 * 0.0001))
    #model.fit(x, y)

    #model = DummyRegressor(strategy="mean")
    #model.fit(x, y)

    y_pred = model.predict(x)

    print(len(bedroomCount))
    print(len(y_pred))

    plt.scatter(bedroomCount, prices, color="blue")
    plt.scatter(bedroomCountObj2, y_pred, color="red", s=15)
    plt.grid()
    plt.xlabel('Number of Bedrooms')
    plt.ylabel('Price in euros per month')
    plt.show()
    plt.scatter(bathroomCount, prices)
    plt.scatter(bedroomCountObj2, y_pred, color="red", s=15)
    plt.grid()
    plt.xlabel('Number of Bathrooms')
    plt.ylabel('Price in euros per month')
    plt.show()