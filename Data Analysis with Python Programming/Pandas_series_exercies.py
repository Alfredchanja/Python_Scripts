'''
Alfred Gachanja
19-12-2023
Exercise for Pandas Series
'''

import numpy as np
import pandas as pd

# Series Creation
age = pd.Series({
	'Alfred': 22,
	'Sandra': 21,
	'Bill': 21,
	'Ian': 21,
	'Binzare': 21,
}, name = 'People\'s ages')
print(age)
print('\n')

# Given the X python list conver it to a Y pandas Series
X = ['A', 'S', 'B', 'I', 'B']
print(X, type(X))
print('\n')

Y = pd.Series(X)
print(Y, type(Y))
print('\n')

# Given the X pandas Series, name it 'My letters'
X = pd.Series(['A', 'S', 'B', 'I', 'B'], name = 'My letters')

print(X)
print('\n')

# Give the X pandas Series, show its values
print(f'Values of X:\n\t {X.values}\n')

# Assign index names to the given X pandas Series
index_names = ['Alfred', 'Sandra', 'Bill','Ian', 'Binzare']
X.index = index_names
print(X)
print('\n')

# Given the X pandas Series, show its first element.
print(X['Alfred'])
print(X.iloc[0])

# Given the X pandas Series, show its last element.
print(X.iloc[-1])
print(X['Binzare'])

# Given the X pandas Series, show all middle elements.
print(X.iloc[1:-1])

# Given the X pandas Series, show the elements in reverse position.
print(X.iloc[::-1])
print('\n')

# Given the X pandas Series, show the first and last elements.
print(X.iloc[[0, -1]])
print('\n')

# Convert the given pandas Series to a float.
age = pd.Series({
	'Alfred': 22,
	'Sandra': 21,
	'Bill': 21,
	'Ian': 21,
	'Binzare': 21,
}, name = 'People\'s ages')


age = pd.Series(age, dtype=np.float64)
print(age)
print('\n')

# Order (sort) the given pandas Series
X = X.sort_values()
print(X)
print('\n')

# Given the X pandas Series, set the fifth element equals to 10
X.iloc[-1] = 10
print(X)

# Given the X pandas Series, change all the middle elements to 0.
X.iloc[1:-1] = 0
print(X)

# Given the X pandas Series, add 5 to every element.
X['Alfred'] = 5
X = X + 5
print(X)
print('\n')

# Given the X pandas Series, make a mask showing negative elements.
Z = pd.Series([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])
print(Z < 0)
print('\n')
mask = Z <= 0
print(mask)
print('\n')

# Given the X pandas Series, get the negative elements.
print(Z[Z < 0])
print(Z[mask])

# Given the X pandas Series, get numbers higher than 5.
print(Z > 5)
print(Z[Z > 5])
print('\n')

# Given the pandas Series, get the numbers higher than the elements mean
print(Z[Z > Z.mean()])

# Given the pandas Series, get the numbers equal to 2 or 10.
print(Z[(Z == 2) | (Z == 10)])

# Given the X pandas Series, Return True if none of its elements is Zero
print(Z.all())

# Given the X pandas Series, Return True if any of its elements is zero.
print(Z.any())

# Given the X pandas Series, show the sum, mean value, max value and min Value of its elements.
print(Z.sum())
print(Z.mean())
print(Z.max())
print(Z.min())