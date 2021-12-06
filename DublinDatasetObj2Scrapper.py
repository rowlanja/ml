#!/usr/bin/env python
# coding: utf-8

#PUT ALL REQUIREMENTS HERE
#if command fails try with pip instead of pip3
#pip3 install requests
#pip3 install bs4
#pip install selenium
#pip install csv
#run in the browser also what are you doing with the help of chrome driver


# import these two modules bs4 for selecting HTML tags easily
from bs4 import BeautifulSoup
from selenium import webdriver
import numpy as np

# requests module is easy to operate some people use urllib but I prefer this one because it is easy to use.
import requests
import csv
urls=[]
urls.append("https://www.rent.ie/houses-to-let/renting_dublin/dublin-1/")
urls.append("https://www.rent.ie/houses-to-let/renting_dublin/dublin-2/")
urls.append("https://www.rent.ie/houses-to-let/renting_dublin/dublin-3/")
urls.append("https://www.rent.ie/houses-to-let/renting_dublin/dublin-4/")
urls.append("https://www.rent.ie/houses-to-let/renting_dublin/dublin-5/")
urls.append("https://www.rent.ie/houses-to-let/renting_dublin/dublin-6/")
urls.append("https://www.rent.ie/houses-to-let/renting_dublin/dublin-7/")
urls.append("https://www.rent.ie/houses-to-let/renting_dublin/dublin-8/")
urls.append("https://www.rent.ie/houses-to-let/renting_dublin/dublin-9/")
urls.append("https://www.rent.ie/houses-to-let/renting_dublin/dublin-10/")
urls.append("https://www.rent.ie/houses-to-let/renting_dublin/dublin-11/")
urls.append("https://www.rent.ie/houses-to-let/renting_dublin/dublin-12/")
urls.append("https://www.rent.ie/houses-to-let/renting_dublin/dublin-13/")
urls.append("https://www.rent.ie/houses-to-let/renting_dublin/dublin-14/")
urls.append("https://www.rent.ie/houses-to-let/renting_dublin/dublin-15/")
urls.append("https://www.rent.ie/houses-to-let/renting_dublin/dublin-16/")
urls.append("https://www.rent.ie/houses-to-let/renting_dublin/dublin-17/")
urls.append("https://www.rent.ie/houses-to-let/renting_dublin/dublin-18/")
urls.append("https://www.rent.ie/houses-to-let/renting_dublin/dublin-20/")
urls.append("https://www.rent.ie/houses-to-let/renting_dublin/dublin-22/")
urls.append("https://www.rent.ie/houses-to-let/renting_dublin/dublin-24/")
areaCodes = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,22,24]

class Property:
    def __init__(self, price, bedroom_count, bathroom_count, furnished_state
        ,location1,location2,location3,location4,location5,location6,location7,
        location8,location9,location10,location11,location12,location13
        ,location14,location15,location16,location17,location18,location20,
        location22,location24
    ):
        # strip() removes new line characters
        self.price = price
        self.location1 = location1
        self.location2 = location2
        self.location3 = location3
        self.location4 = location4
        self.location5 = location5
        self.location6 = location6
        self.location7 = location7
        self.location8 = location8
        self.location9 = location9
        self.location10 = location10
        self.location11 = location11
        self.location12 = location12
        self.location13 = location13
        self.location14 = location14
        self.location15 = location15
        self.location16 = location16
        self.location17 = location17
        self.location18 = location18
        self.location20 = location20
        self.location22 = location22
        self.location24 = location24
        self.bedroom_count = bedroom_count
        self.bathroom_count = bathroom_count 
        self.furnished_state = furnished_state
    
    def __str__(self):
        price = ("price =" + self.price + "\n")
        location = ("location =" + self.location + "\n") 
        bedroom_count = ("bedroom_count =" + self.bedroom_count + "\n") 
        bathroom_count = ("bathroom_count =" + self.bathroom_count + "\n") 
        furnished_state = ("furnished_state =" + self.furnished_state + "\n")
        return (price+location+bedroom_count+bathroom_count+furnished_state)
    
    def toArr(self):
        return [self.price, self.bedroom_count, self.bathroom_count, self.furnished_state,
            self.location1,self.location2,self.location3,self.location4,self.location5,self.location6,self.location7,self.location8,
            self.location9,self.location10,self.location11,self.location12,self.location13,self.location14,self.location15,self.location16,self.location17,self.location18,self.location20,self.location22,self.location24]

def get_chrome_web_driver(options):
    return webdriver.Chrome("./chromedriver", chrome_options=options)


def get_web_driver_options():
    return webdriver.ChromeOptions()


def set_ignore_certificate_error(options):
    options.add_argument('--ignore-certificate-errors')


def set_browser_as_incognito(options):
    options.add_argument('--incognito')

def get_properties(url):
    ## scrap data from source
    source=requests.get(url) ## this requests dublin endpoint
    source_text=BeautifulSoup(source.text,'html')
    ### find html tags with classes
    properties=source_text.find_all("div",class_='search_result')
    return properties
def initialize_region(Property, regionInitialization):
    Property.initLocation(regionInitialization)     
    return Property
def create_property(html, county_index, regionInitialization):
    try:
        ## property_info contains property characteristics like bedroom count, bathroom count, furnished state
        property_info = html.find("div", class_='sresult_description').find('h3').text.strip()
        ## this removes the types of bedrooms the property has e.g '1 single, 2 double'
        property_info = ((property_info[:property_info.find("(")-1]) + (property_info[property_info.find(")")+1:])).split(',')
        ## normalised furnishings. unfurnished = 1, furnished = 0
        furnished = 1 if ("unfurnished" in (property_info[2])) else 0
        price = html.find("div", class_='sresult_description').find('h4').text.replace(" ", "").replace(",", "").strip()[1:]
        price = price[:price.find("(")]
        if "weekly" in price or "week" in price:
            price = int(price.strip("weekly"))
            price *= 4
        else : 
            price = int(price.strip("monthly"))
            new_property = Property(
                ## for price we need to remove whitespice with replace(), strip newline char with .strip() and remove euro sign with [1:]
                location1 =  regionInitialization[0],
                location2 =  regionInitialization[1],
                location3 =  regionInitialization[2],
                location4 =  regionInitialization[3],
                location5 =  regionInitialization[4],
                location6 =  regionInitialization[5],
                location7 =  regionInitialization[6],
                location8 =  regionInitialization[7],
                location9 =  regionInitialization[8],
                location10 = regionInitialization[9],
                location11 = regionInitialization[10],
                location12 = regionInitialization[11],
                location13 = regionInitialization[12],
                location14 = regionInitialization[13],
                location15 = regionInitialization[14],
                location16 = regionInitialization[15],
                location17 = regionInitialization[16],
                location18 = regionInitialization[17],
                location20 = regionInitialization[18],
                location22 = regionInitialization[19],
                location24 = regionInitialization[20], 
                price = str(price),
                bedroom_count = property_info[0][:1],
                bathroom_count = property_info[1][:2],
                furnished_state = str(furnished), 
            )
        return new_property
    except:
        return

def create_dataset():
    # stores properties as objects in dataset
    dataset = []
    # stores properties as arrays in dataset
    datasetArr = []
    regionInitialization = np.array([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    regionInitializationCheck = np.array([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    for index in range(len(urls)): 
        processedAllUrls = False
        pageIndex = 0 
        while(processedAllUrls == False):
            url = urls[index]+'page_'+str(pageIndex)+'/'
            countyProperties=get_properties(url)
            print('url : ', url, ' props : ',len(countyProperties))
            if(len(countyProperties) == 0): 
                processedAllUrls = True
                break
            for entry in countyProperties:
                newProperty = create_property(entry, areaCodes[index], regionInitialization) 
                ## checking for empty object. Empty object may be returned when property doesnt conform to standard 
                if newProperty != None:
                    dataset.append(newProperty)
                    datasetArr.append(newProperty.toArr())
            pageIndex += 1
        regionInitialization = np.roll(regionInitialization, 1)
        if((regionInitialization == regionInitializationCheck).all()): break
    return dataset,datasetArr

def print_dataset(dataset):
    # for property_obj in dataset:
    #     print(property_obj)
    print("Dataset contains : ", len(dataset), " properties") 

def update_csv(dataset_arr):
    fields = ['price', 'bedroom_count', 'bathroom_count', 'furnished',
                'Dublin_1',
                'Dublin_2',
                'Dublin_3',
                'Dublin_4',
                'Dublin_5',
                'Dublin_6',
                'Dublin_7',
                'Dublin_8',
                'Dublin_9',
                'Dublin_10',
                'Dublin_11',
                'Dublin_12',
                'Dublin_13',
                'Dublin_14',
                'Dublin_15',
                'Dublin_16',
                'Dublin_17',
                'Dublin_18',
                'Dublin_20',
                'Dublin_22',
                'Dublin_24'
    ] 

    with open('dublinDatasetObj2.csv', 'w', encoding='utf-8') as f:
        # using csv.writer method from CSV package
        write = csv.writer(f)
        write.writerow(fields)
        write.writerows(dataset_arr)

dataset,dataset_arr = create_dataset()
print_dataset(dataset)
update_csv(dataset_arr)

    