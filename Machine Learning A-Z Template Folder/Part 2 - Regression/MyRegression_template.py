#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 06:41:28 2019

@author: grigor
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 00:12:53 2019

@author: grigor
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# Splitting the dataset into the Training set and Test set
# from sklearn.linear_model import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Fitting the  Regression Mode to Dataset



# Predictin a new result with Polynomial Regression
y_pred = regressor.predict((np.array(6.5).reshape(1, -1)))



# Visualizing the Polynomial Regression results
plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color = "blue")
plt.title('Truth or Bluff ( Regression Model)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

# Visualizing the Polynomial Regression results (for higher resuolution and smoother curve)
X_grid = np.arrange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid),1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = "blue")
plt.title('Truth or Bluff ( Regression Model)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()