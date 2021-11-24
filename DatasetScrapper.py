#!/usr/bin/env python
# coding: utf-8

#PUT ALL REQUIREMENTS HERE
#if command fails try with pip instead of pip3
#pip3 install requests
#pip3 install bs4
#pip install selenium

#run in the browser also what are you doing with the help of chrome driver


# import these two modules bs4 for selecting HTML tags easily
from bs4 import BeautifulSoup
# requests module is easy to operate some people use urllib but I prefer this one because it is easy to use.
import requests
from selenium import webdriver

urls=[]
urls.append("https://www.rent.ie/houses-to-let/renting_dublin/")
urls.append("https://www.rent.ie/houses-to-let/renting_antrim/")
urls.append("https://www.rent.ie/houses-to-let/renting_armagh/")
urls.append("https://www.rent.ie/houses-to-let/renting_carlow/")
urls.append("https://www.rent.ie/houses-to-let/renting_cavan/")
urls.append("https://www.rent.ie/houses-to-let/renting_clare/")
urls.append("https://www.rent.ie/houses-to-let/renting_cork/")
urls.append("https://www.rent.ie/houses-to-let/renting_derry/")
urls.append("https://www.rent.ie/houses-to-let/renting_donegal/")
urls.append("https://www.rent.ie/houses-to-let/renting_down/")
urls.append("https://www.rent.ie/houses-to-let/renting_fermanagh/")
urls.append("https://www.rent.ie/houses-to-let/renting_galway/")
urls.append("https://www.rent.ie/houses-to-let/renting_kerry/")
urls.append("https://www.rent.ie/houses-to-let/renting_kildare/")
urls.append("https://www.rent.ie/houses-to-let/renting_kilkenny/")
urls.append("https://www.rent.ie/houses-to-let/renting_laois/")
urls.append("https://www.rent.ie/houses-to-let/renting_leitrim/")
urls.append("https://www.rent.ie/houses-to-let/renting_longford/")
urls.append("https://www.rent.ie/houses-to-let/renting_louth/")
urls.append("https://www.rent.ie/houses-to-let/renting_mayo/")
urls.append("https://www.rent.ie/houses-to-let/renting_meath/")
urls.append("https://www.rent.ie/houses-to-let/renting_monaghan/")
urls.append("https://www.rent.ie/houses-to-let/renting_offaly/")
urls.append("https://www.rent.ie/houses-to-let/renting_roscommon/")
urls.append("https://www.rent.ie/houses-to-let/renting_limerick/")
urls.append("https://www.rent.ie/houses-to-let/renting_longford/")
urls.append("https://www.rent.ie/houses-to-let/renting_louth/")

class Property:
    def __init__(self, price, location, bedroom_count, bathroom_count, furnished_state):
        self.price = price.strip()
        self.location = location.strip()
        self.bedroom_count = bedroom_count.strip()
        self.bathroom_count = bathroom_count.strip() 
        self.furnished_state = furnished_state.strip()
    
    def __str__(self):
        price = ("price =" + self.price + "\n")
        location = ("location =" + self.location + "\n") 
        bedroom_count = ("bedroom_count =" + self.bedroom_count + "\n") 
        bathroom_count = ("bathroom_count =" + self.bathroom_count + "\n") 
        furnished_state = ("furnished_state =" + self.furnished_state + "\n")
        return (price+location+bedroom_count+bathroom_count+furnished_state)

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

def create_property(html):
    try:
        property_info = html.find("div", class_='sresult_description').find('h3').text.split(',')
        new_property = Property(
            location = (html.find("a").text),
            price = (html.find("div", class_='sresult_description').find('h4').text),
            bedroom_count = property_info[0],
            bathroom_count = property_info[1],
            furnished_state = property_info[2], 
        )
        return new_property
    except:
        print("property didnt have enough features skipping")

def create_dataset():
    dataset = []
    for index in range(len(urls)): 
        properties=get_properties(urls[index])
        for entry in properties:
            ## property_info contains property characteristics like bedroom count, bathroom count, furnished state
            new_property = create_property(entry) 
            dataset.append(new_property)
    return dataset    

def print_dataset(dataset):
    for property_obj in dataset:
        print(property_obj)
    print("Dataset contains : ", len(dataset), " properties") 

dataset = create_dataset()
print_dataset(dataset)

    