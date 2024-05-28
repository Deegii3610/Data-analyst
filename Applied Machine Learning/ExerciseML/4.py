import numpy as np
import matplotlib.pyplot as plt

m = 50 
np.random.seed(42) #Used to plot the same points every run
Xtrain = np.linspace(0.0,1.0,num=m) 
ytrain = np.sign(Xtrain-0.5+np.random.normal(0,0.2,m)) 
Xtrain = Xtrain.reshape(-1, 1)

plt.scatter(Xtrain,ytrain)
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['Training points'])
plt.show()

#Test data
n_test = 10 
Xtest = np.linspace(0.0, 1.0, num=n_test) 
ytest = np.sign(Xtest - 0.5 + np.random.normal(0, 0.2, n_test)) 
Xtest = Xtest.reshape(-1, 1) 
