import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = pd.read_csv('results.csv', usecols=['Date','ConnectionType' ,'Latitude','Longitude','DownloadSpeed','DownloadByte','UploadSpeed','UploadByte','Latency','Server','Inner IP','Outer IP','URL'])
A = data[['Latitude','Longitude','DownloadSpeed','UploadSpeed','Latency']]

# data = pd.read_csv('results12.csv', usecols=['Date','ConnectionType' ,'Altitude','Longitude','DownloadSpeed','DownloadByte','UploadSpeed','UploadByte','Latency','Server','Inner IP','Outer IP','URL'])
# A = data[['Altitude','Longitude','DownloadSpeed','UploadSpeed','Latency']]


matrix = np.array(A.values, 'float')
X = matrix[:,2]
y = matrix[:,4]

#normalization
X = X/(np.max(X))

plt.plot(X,y,'bo')
plt.ylabel('Latency')
plt.xlabel('Altitude')
plt.legend(['Network Performance'])
plt.title('Altitude vs Latency')
plt.grid()
plt.show()


m = np.size(y)
X = X.reshape([98,1])
x = np.hstack([np.ones_like(X),X])
theta = np.zeros([2,1])

def cost_function(x,y,theta):
    a = 1 / (2 * m)
    b = np.sum(((x @ theta) - y) ** 2)
    j = (a) * (b)
    return j


# print(cost_function(x,y, theta))


def gradient(x, y, theta):
    alpha = 0.00001
    iteration = 2000
    # gradient descend algorithm
    J_history = np.zeros([iteration, 1]);


    for iter in range(0, 2000):
        error = (x @ theta) - y
        temp0 = theta[0] - ((alpha / m) * np.sum(error * x[:, 0]))
        temp1 = theta[1] - ((alpha / m) * np.sum(error * x[:, 1]))
        theta = np.array([temp0, temp1]).reshape(2, 1)
        J_history[iter] = (1 / (2 * m)) * (np.sum(((x @ theta) - y) ** 2))  # compute J value for each iteration
    return theta, J_history

theta, J = gradient(x,y,theta)
# print(theta)

plt.plot(X,y,'bo')
plt.plot(X,x@theta,'-')
# plt.axis([0.75,1.25,0,40])
plt.axis([-1,1.25,0,55])
plt.ylabel('Latency')
plt.xlabel('Altitude')
plt.legend(['Altitude','LinearFit'])
plt.title('Altitude vs Network Performance')
plt.grid()
plt.show()

predict1 = [1,(164/np.max(matrix[:,0]))]


#visualising J (theta0 , theta1)
theta0_vals = np.linspace(-5,10,100).reshape(1,100)
theta1_vals = np.linspace(-5,10,100).reshape(1,100)
#initialise J value to matrix of 0
J_vals = np.zeros([np.size(theta0_vals),np.size(theta1_vals)])
#fill J_vals
for i in range(0,np.size(theta0_vals)):
    for j in range(0,np.size(theta1_vals)):
        t = np.array([theta0_vals[:,i],theta1_vals[:,j]])
        J_vals[i,j] = cost_function(x,y,t)
# Because of the way meshgrids work in the surf command, we need to
# transpose J_vals before calling surf, or else the axes will be flipped
J_vals = J_vals.T


#surface plot for covergence

fig = plt.figure(figsize=[12.0,8.0])
ax = fig.add_subplot(111,projection ='3d')
ax.plot_surface(theta0_vals,theta1_vals,J_vals)
ax.set_xlabel('theta0')
ax.set_ylabel('theta1')
ax.set_zlabel('J_vals')
plt.show()