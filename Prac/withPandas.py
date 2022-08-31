import pandas
from sklearn import linear_model

df = pandas.read_csv('cars.csv')
X = df[['Weight', 'Volume']]
Y = df['CO2']
reg = linear_model.LinearRegression()
reg.fit(X, Y)
print(reg.coef_, 1)
predCO2 = reg.predict([[2300, 1300]])
print(predCO2[0], 2)