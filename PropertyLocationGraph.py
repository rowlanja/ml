import matplotlib.pyplot as plt
import pandas as pd
  
locations = [
    "dublin",
    "antrim",
    "armagh",
    "carlow",
    "cavan",
    "clare",
    "cork",
    "derry",
    "donegal",
    "down",
    "fermanagh",
    "galway",
    "kerry",
    "kildare",
    "kilkenny",
    "laois",
    "leitrim",
    "longford",
    "louth",
    "limerick",
    "mayo",
    "meath",
    "monaghan",
    "offaly",
    "roscommon",
    "sligo",
    "tipperary",
    "tyrone",
    "waterford",
    "wexford",
    "westmeath",
    "wicklow"
]

data = pd.read_csv("Dataset.csv")
  
plt.scatter(data['location'], data['price'])
plt.title("Scatter Plot")
plt.ylabel('Price')
plt.xlabel('Location')
  
plt.show()