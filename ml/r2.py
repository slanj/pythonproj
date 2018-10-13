import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np

df = pd.read_csv("FuelConsumption.csv")

# take a look at the dataset
# print(df.head())

# # summarize the data
# print(df.describe())

cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
# cdf.head(9)

viz = cdf[['CYLINDERS','ENGINESIZE','CO2EMISSIONS','FUELCONSUMPTION_COMB']]
# viz.hist()
# plt.show()

# plt.scatter(cdf.CYLINDERS, cdf.CO2EMISSIONS, color='blue')
# plt.xlabel("Cylinders")
# plt.ylabel("Emission")
# plt.show()

msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[~msk]

from sklearn import linear_model
regr = linear_model.LinearRegression()
train_x = np.asanyarray(train[['ENGINESIZE']])
train_y = np.asanyarray(train[['CO2EMISSIONS']])
regr.fit (train_x, train_y)
# The coefficients
print ('Coefficients simple: ', regr.coef_)
print ('Intercept simple: ',regr.intercept_)


train_x_mult = np.asanyarray(train[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']])
regr_mult = linear_model.LinearRegression()
regr_mult.fit(train_x_mult, train_y)
print ('Coefficients mutiple: ', regr_mult.coef_)


# plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
# plt.plot(train_x, regr.coef_[0][0]*train_x + regr.intercept_[0], '-r')
# plt.xlabel("Engine size")
# plt.ylabel("Emission")
# plt.show()


from sklearn.metrics import r2_score

test_x = np.asanyarray(test[['ENGINESIZE']])
test_y = np.asanyarray(test[['CO2EMISSIONS']])
test_y_ = regr.predict(test_x)

print("Mean absolute error for simple regression: %.2f" % np.mean(np.absolute(test_y_ - test_y)))
print("Residual sum of squares (MSE) for simple regression: %.2f" % np.mean((test_y_ - test_y) ** 2))
print("R2-score for simple regression: %.2f" % r2_score(test_y_ , test_y) )



test_y_hat= regr_mult.predict(test[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']])
test_x_mult = np.asanyarray(test[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']])
test_y_mult = np.asanyarray(test[['CO2EMISSIONS']])

print("Residual sum of squares for multiple regression: %.2f"
      % np.mean((test_y_hat - test_y_mult) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr_mult.score(test_x_mult, test_y_mult))