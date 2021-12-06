import matplotlib.pyplot as plt
import pandas as pd
  
  

import csv
 
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

    # fig, (ax1, ax2) = plt.subplots(2)
    # ax1.scatter(bedroomCount, prices)
    # ax1.set(xlabel='Number of Bedrooms', ylabel='Price in euros per month')      
    # ax2.scatter(bathroomCount, prices)
    # ax2.set(xlabel='Number of Bathrooms', ylabel='Price in euros per month')    

    plt.scatter(bedroomCount, prices)
    plt.grid()
    plt.xlabel('Number of Bedrooms')
    plt.ylabel('Price in euros per month')
    plt.show()
    plt.scatter(bathroomCount, prices)
    plt.grid()
    plt.xlabel('Number of Bathrooms')
    plt.ylabel('Price in euros per month')
    plt.show()
