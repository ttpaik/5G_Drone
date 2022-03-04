import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import scipy

dataset = pd.read_csv("res.csv")

# x = dataset[['Altitude']]
# y = dataset['Download Speed']

df = dataset.groupby(['Altitude']).mean()

x = df[['Alt']]
y = df['Download Speed']


#normalization
x = scipy.stats.zscore(x)
y = scipy.stats.zscore(y)

#Splitting the dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 100)

#Fitting and Regression Model
mlr = LinearRegression()
mlr.fit(x_train, y_train)

#Intercept and Coefficient
print("Intercept: ", mlr.intercept_)
print("Coefficients:", mlr.coef_)
list(zip(x, mlr.coef_))

#Prediction
y_pred_mlr= mlr.predict(x_test)
print("Prediction for test set: {}".format(y_pred_mlr))

#Actual and Predicted Value
mlr_diff = pd.DataFrame({'Actual value': y_test, 'Predicted value': y_pred_mlr})
mlr_diff.head()

#Error Rates
meanAbErr = metrics.mean_absolute_error(y_test, y_pred_mlr)
meanSqErr = metrics.mean_squared_error(y_test, y_pred_mlr)
rootMeanSqErr = np.sqrt(metrics.mean_squared_error(y_test, y_pred_mlr))

print('Mean Absolute Error:', meanAbErr)
print('Mean Square Error:', meanSqErr)
print('Root Mean Square Error:', rootMeanSqErr)
print('Accuracy: ', mlr.score(x_test,y_test)*100)

plt.plot(x,y,'bo')
plt.ylabel('Downloaad Speed(Mbps)')
plt.xlabel('Altitude(ft)')
plt.legend(['Network Performance'])
plt.grid()
plt.show()
#
#
# plt.plot(y_pred_mlr,y[0:30],'bo')
# plt.ylabel('Actual Speed')
# plt.xlabel('Predicted Speed')
# plt.legend(['Network Performance'])
# plt.title('Actual Speed vs Predicted Speed')
# plt.grid()
# plt.show()
