import matplotlib.pyplot as plt
import pandas as pd
  
  
data = pd.read_csv("Dataset.csv")
  
plt.scatter(data['location'], data['price'])
plt.title("Scatter Plot")
plt.ylabel('Price')
plt.xlabel('Location')
  
plt.show()