## Machine Learning Online Class - Exercise 1: Linear Regression

#  Instructions
#  ------------
#
#  This file contains code that helps you get started on the
#  linear exercise. You will need to complete the following functions
#  in this exericse:
#
#     warmUpExercise.py
#     plotData.py
#     gradientDescent.m
#     computeCost.m
#     gradientDescentMulti.m
#     computeCostMulti.m
#     featureNormalize.m
#     normalEqn.m
#
#  For this exercise, you will not need to change any code in this file,
#  or any other files other than those mentioned above.
#
# x refers to the population size in 10,000s
# y refers to the profit in $10,000s
#

## Initialization

# import pandas as pd
import numpy as np

# clear  close all clc

## ==================== Part 1: Basic Function ====================
# Complete warmUpExercise.py
# Readings: https://docs.python.org/3/tutorial/modules.html

from warmUpExercise import warmUpExercise

print('Running warmUpExercise ... \n')
print('5x5 Identity Matrix: \n')

warmUpExercise()

input('Program paused. Press enter to continue.\n')

## ======================= Part 2: Plotting =======================
print('Plotting Data ...\n')

# Readings: https://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html 
#           https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.copy.html

DATA_PATH = "ex1data1.txt"
data = np.loadtxt(DATA_PATH, delimiter=',')

# Used np.copy here because the original data should be unchanged in case its needed later

X = np.copy(data[:, 0])
y = np.copy(data[:, 1])


m = len(y) # number of training examples

# Plot Data
# Note: You have to complete the code in plotData.py

from plotData import plotData
plotData(X, y)

input('Program paused. Press enter to continue.\n')

## =================== Part 3: Cost and Gradient descent ===================
