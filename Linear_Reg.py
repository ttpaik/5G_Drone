import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

#Reading the dataset
dataset = pd.read_csv("results.csv")


#Setting the value for X and Y
x = dataset[['DownloadSpeed', 'UploadSpeed']]
y = dataset['Latency']

#Splitting the dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 100)

#Fitting the Multiple Linear Regression model
mlr = LinearRegression()
mlr.fit(x_train, y_train)

#Intercept and Coefficient
print("Intercept: ", mlr.intercept_)
print("Coefficients:", mlr.coef_)
list(zip(x, mlr.coef_))


#Prediction of test set
y_pred_mlr= mlr.predict(x_test)
print("Prediction for test set: {}".format(y_pred_mlr))

#Actual value and the predicted value
mlr_diff = pd.DataFrame({'Actual value': y_test, 'Predicted value': y_pred_mlr})
mlr_diff.head()

#Model Evaluation
meanAbErr = metrics.mean_absolute_error(y_test, y_pred_mlr)
meanSqErr = metrics.mean_squared_error(y_test, y_pred_mlr)
rootMeanSqErr = np.sqrt(metrics.mean_squared_error(y_test, y_pred_mlr))
print('R squared: {:.2f}'.format(mlr.score(x,y)*100))
print('Mean Absolute Error:', meanAbErr)
print('Mean Square Error:', meanSqErr)
print('Root Mean Square Error:', rootMeanSqErr)


plt.plot(y_pred_mlr,y[0:20],'bo')
plt.ylabel('Actual Speed')
plt.xlabel('Predicted Speed')
plt.legend(['Network Performance'])
plt.title('Actual Speed vs Predicted Speed')
plt.grid()
plt.show()
