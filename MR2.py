#Coefficient
#The coefficient is a factor that describes the relationship with an unknown variable.


import pandas
from sklearn import linear_model

df = pandas.read_csv("D:\\co2.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

print(regr.coef_)
