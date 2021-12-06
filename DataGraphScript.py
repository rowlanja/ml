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

    fig, (ax1, ax2, ax3) = plt.subplots(3)
    ax1.scatter(locations, prices)
    ax1.set(xlabel='Dublin Area Code', ylabel='Price in euros per month')    
    ax2.scatter(bedroomCount, prices)
    ax2.set(xlabel='Number of Bedrooms', ylabel='Price in euros per month')      
    ax3.scatter(bathroomCount, prices)
    ax3.set(xlabel='Number of Bathrooms', ylabel='Price in euros per month')    

    # plt.scatter(locations, prices)
    # plt.grid()
    # plt.xlabel('Dublin Area Code')
    # plt.ylabel('Price in euros per month')
    plt.show()
