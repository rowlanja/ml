import matplotlib.pyplot as plt
import pandas as pd
  
  

import csv
 
# opening the CSV file
with open('dublinDataset.csv', mode ='r')as file:
   
    # reading the CSV file
    csvFile = csv.reader(file)
    prices = []
    locations = []
    # displaying the contents of the CSV file
    for lines in csvFile:
        if len(lines) > 0:
            if lines[0] == 'price':continue
            prices.append(int(lines[0]))
            locations.append(lines[1])
            print(lines[0], lines[1])
    plt.scatter(locations, prices)
    plt.grid()
    plt.xlabel('Dublin Area Code')
    plt.ylabel('Price in euros per month')
    plt.show()
