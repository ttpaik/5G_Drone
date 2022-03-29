import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.neighbors import KNeighborsRegressor
import scipy

dataset = pd.read_csv("res.csv")

# x = dataset[['Altitude']]
# y = dataset['Download Speed']

df = dataset.groupby(['Altitude']).mean()

x = df[['Alt', 'Lon', 'Lat']]
y = df[['Download Speed', 'Upload Speed']]

# # plot data, check for linearity
# plt.subplot(1,3,1) # plot 1: Alt vs Download/Upload Speed
# plt.scatter(df['Alt'], df['Download Speed'], color='red')
# plt.scatter(df['Alt'], df['Upload Speed'], color='blue')
# plt.title('1: Network Speed vs Alt', fontsize=14)
# plt.xlabel('Alt', fontsize=14)
# plt.ylabel('Network Speed', fontsize=14)
# plt.grid(True)

# plt.subplot(1,3,2) # plot 2: Lon vs Download/Upload Speed
# plt.scatter(df['Lon'], df['Download Speed'], color='red')
# plt.scatter(df['Lon'], df['Upload Speed'], color='blue')
# plt.title('2: Network Speed vs Lon', fontsize=14)
# plt.xlabel('Lon', fontsize=14)
# plt.ylabel('Network Speed', fontsize=14)
# plt.grid(True)

# plt.subplot(1,3,3) # plot 3: Lat vs Download/Upload Speed
# plt.scatter(df['Lat'], df['Download Speed'], color='red')
# plt.scatter(df['Lat'], df['Upload Speed'], color='blue')
# plt.title('3: Network Speed vs Lat', fontsize=14)
# plt.xlabel('Lat', fontsize=14)
# plt.ylabel('Network Speed', fontsize=14)
# plt.grid(True)
# plt.show()

#normalization
# x = scipy.stats.zscore(x)
# y = scipy.stats.zscore(y)

#Splitting the dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 100)

#Fitting and Regression Model
mlr = KNeighborsRegressor(n_neighbors = 4, p=2)
mlr.fit(x_train, y_train)
print(mlr.get_params())

#Intercept and Coefficient
# print("Intercept: ", mlr.intercept_)
# print("Coefficients:", mlr.coef_)
# list(zip(x, mlr.coef_))

#Prediction
y_pred_mlr= mlr.predict(x_test)
print("Prediction for test set: {}".format(y_pred_mlr))

#Actual and Predicted Value
# mlr_diff = pd.DataFrame({'Actual value': y_test, 'Predicted value': y_pred_mlr})
# mlr_diff.head()

#Error Rates
meanAbErr = metrics.mean_absolute_error(y_test, y_pred_mlr)
meanSqErr = metrics.mean_squared_error(y_test, y_pred_mlr)
rootMeanSqErr = np.sqrt(metrics.mean_squared_error(y_test, y_pred_mlr))
r2Score = metrics.r2_score(y_test, y_pred_mlr) * 100

print('Mean Absolute Error:', meanAbErr)
print('Mean Square Error:', meanSqErr)
print('Root Mean Square Error:', rootMeanSqErr)
print('r2Score: ', r2Score)   

# plt.plot(df['Alt'],df['Download Speed'],'bo')
# plt.ylabel('Download Speed(Mbps)')
# plt.xlabel('Altitude(ft)')
# plt.legend(['Network Performance'])
# plt.grid()
# plt.show()


# plt.plot(y_pred_mlr,y[0:30],'bo')
# plt.ylabel('Actual Speed')
# plt.xlabel('Predicted Speed')
# plt.legend(['Network Performance'])
# plt.title('Actual Speed vs Predicted Speed')
# plt.grid()
# plt.show()
