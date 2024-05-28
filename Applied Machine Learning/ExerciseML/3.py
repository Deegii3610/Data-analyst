import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
np.random.seed(42) #Used to plot the same points every run
m = 50 
Xtrain = np.linspace(0.0,1.0,num=m) 
ytrain = 10*Xtrain**2 + np.random.normal(0.0,1.0,m) 
Xtrain = Xtrain.reshape(-1, 1)

#Plot for Part a.
plt.scatter(Xtrain,ytrain)
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['Training points'])
plt.show()

#Write code to fit K-NN model here where K=3
model = KNeighborsRegressor(n_neighbors=3,weights='uniform').fit(Xtrain, ytrain)

#Test set for question Part c.
n_test = 10 
Xtest = np.linspace(0.0, 1.0, num=n_test) 
ytest = 10 * Xtest**2 + np.random.normal(0.0, 1.0, n_test) 
Xtest = Xtest.reshape(-1, 1)


# Linear regression model
linear_model = LinearRegression().fit(Xtrain, ytrain)

# Predict on the test set using both models
ypred_linear = linear_model.predict(Xtest)
ypred_knn = model.predict(Xtest)

# Calculate MSE for both models
mse_linear = mean_squared_error(ytest, ypred_linear)
mse_knn = mean_squared_error(ytest, ypred_knn)
print("MSE for Linear Regression Model:", mse_linear)
print("MSE for K-NN Model (K=3):", mse_knn)

#Write code to plot training data, test data, and model fit
plt.scatter(Xtrain, ytrain, color='red', marker='+', label='Traning Data')
plt.plot(Xtest, ypred_knn, color='green', label='Model Fit (K-NN, K=3)')
plt.plot(Xtest, ypred_linear, color='blue', label='Model Fit Linear regression model')
plt.xlabel('input x')
plt.ylabel('output y')
plt.legend()
plt.show()


