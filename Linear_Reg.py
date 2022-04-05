import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import KFold

dataset = pd.read_csv("res.csv")

# Cluster by altitude
df = dataset.groupby(['Altitude']).mean()

x = df[['Alt', 'Lon', 'Lat']]
y = df[['Download Speed', 'Upload Speed']]

# Split the dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 100)

# Test the parameters of intended model, KNeighborsRegression, using GridSearchCV
test_knn = KNeighborsRegressor()
param_grid = {'n_neighbors': np.arange(1, 6),
              'weights': ['uniform', 'distance']}
gscv = GridSearchCV(test_knn, param_grid, cv=KFold(n_splits=3,
                                              shuffle=True, random_state=0))
gscv.fit(x_train, y_train)
print("Best params", gscv.best_params_)

# Use "best parameters" that are found
params = gscv.best_params_
knn = KNeighborsRegressor(n_neighbors = params['n_neighbors'], weights = params['weights'])
# knn = KNeighborsRegressor(n_neighbors = 4)
knn.fit(x_train, y_train)

# Perform predictions and compare to actual values
y_pred_knn= knn.predict(x_test)
print("------------------")
for i in range(y_test.shape[0]):
    print("----- Prediction {}".format(i))
    print(" Predicted Download Speed: {0:.2f}, Actual Download Speed: {1:.2f}".format(y_pred_knn[i][0], y_test.iat[i,0]))
    print(" Predicted Upload Speed: {0:.2f}, Actual Upload Speed: {1:.2f}".format(y_pred_knn[i][1], y_test.iat[i,1]))
print("------------------")

# Evaluate with MAE, MSE, RMSE, R^2
meanAbErr = metrics.mean_absolute_error(y_test, y_pred_knn)
meanSqErr = metrics.mean_squared_error(y_test, y_pred_knn)
rootMeanSqErr = np.sqrt(metrics.mean_squared_error(y_test, y_pred_knn))
r2Score = metrics.r2_score(y_test, y_pred_knn) * 100

print('Mean Absolute Error:', meanAbErr)
print('Mean Square Error:', meanSqErr)
print('Root Mean Square Error:', rootMeanSqErr)
print('R Squared Score: ', r2Score)   
