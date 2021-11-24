## Predicting Prices of Rental Properties around Ireland

- Bair Buyrchiyev
- James Rowland
- Vsevolod Syrtsov
## 1. Motivation: 

Fair rental property prices are a big problem especially in Dublin’s city center. It can often be hard to estimate what classifies a reasonable rent price given the location, type of property etc. This is a result of there being no standard for the price of rent. Building a model based off of rental prices and their associated properties would be very useful. We could a) predict what a fair price would be for a property with certain characteristics i.e student accommodation in a certain area / 2 bedroom house in north of Cork, and b) detect whether a rental price is a fair price or if it is an unfair price and calculating how unfair the price is.

## 2. Dataset:  
In our project, we will scrap property and rental information from daft.ie, rent.ie and myhome.ie to create a dataset of properties available to rent across Ireland. This dataset will be limited to Irish properties because including multiple countries might result in an under fitted model. This dataset will contain attributes that characterize the property, the location and the price. 

## 3. Method
We plan on using a wide range of regression models. We will experiment and tune these models and will report our findings. Ridge regression would be a suitable regression technique to use, as ridge regression works well when there’s a high correlation between the independent variables (which in our case would be rental property information). Ridge regression can be biased when collinearity is very high, however we do not think this situation will arise. Ridge regression is also less susceptible to overfitting which is important for giving a useful rental price prediction. We will also see if Lasso regression gives a useful model. Lasso regression reduces non-impactful features to zero which helps with overfitting, which could be useful. We will experiment and see how useful this regression technique really is. We will also use confidence intervals to see, within what degree, a rental property is a good price. For example a rental property might be within the top 6% of all rental properties in that category, meaning it is a great price. Another rental property might only be within the top 25% meaning it is a good price but not excellent.
## 4. Intended experiments: 
We can try to scrap rental property review information from the web too. If it is available it will give us a dataset to test our model against. We can also manually create a dataset. It is important to have a definition for what is a fair rental price for each property classification. We can also partition the dataset into thirds. We can train our models with ⅓ of our dataset. We can then test our model against the remaining ⅔ of our dataset. For this to be effective we will need a big enough dataset
