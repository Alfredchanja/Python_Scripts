"""
Alfred Gachanja
07-01-2024
This is a function that uses Numpy to calculate
 the mean, variance, standard deviation, max, min,
 and sum of the rows, columns, and elements in a
 3 by 3 matrix.
"""

import numpy as np

def calculate(digits):

    # Converting the list into a 3 x 3 numpy array.
    numbers = np.array(digits).reshape(3, 3)
    # print(numbers.shape)
    # print(numbers)

    # Calculate the mean of the newly formed array.
    numbers.mean(axis=0) # Mean along axis1 - column.
    numbers.mean(axis=1) # Mean along axis2 - row.
    numbers.mean()

    # print(numbers.mean(axis=0))
    # print(numbers.mean(axis=1))
    # print(numbers.mean())

    # Calculate the variance.
    numbers.var(axis=0) # Variance along axis1 - column.
    numbers.var(axis=1) # Variance along axis2 - column.
    numbers.var()

    print(numbers.var(axis=0))
    print(numbers.var(axis=1))
    # print(numbers.var())

    # Calculate the standard deviation.
    numbers.std(axis=0) # Standard deviation along axis1 - column.
    numbers.std(axis=1) # Standard deviation along axis2 - row.
    numbers.std()

    # print(numbers.std(axis=0))
    # print(numbers.std(axis=1))
    # print(numbers.std())

    # Find the max value.
    numbers.max(axis=0) # Max value along axis1 - column.
    numbers.max(axis=1) # Max value along axis2 - column.
    numbers.max()

    # print(numbers.max(axis=0))
    # print(numbers.max(axis=1))
    # print(numbers.max())

    # Find the min value.
    numbers.min(axis=0) # Min value along axis1 - column
    numbers.min(axis=1) # Min value along axis2 - row
    numbers.min()

    # print(numbers.min(axis=0))
    # print(numbers.min(axis=1))
    # print(numbers.min())

    # Calculate the sum.
    numbers.sum(axis=0) # Sum along axis1 - column.
    numbers.sum(axis=1) # Sum along axis2 - row.
    numbers.sum()

    # print(numbers.sum(axis=0))
    # print(numbers.sum(axis=1))
    # print(numbers.sum())

    # Calculate the cumulative sum.
    numbers.cumsum(axis=0) # Cumulative sum along axis1 - column.
    numbers.cumsum(axis=1) # Cumulative sum along axis2 - row
    numbers.cumsum()

    # print(numbers.cumsum(axis=0))
    # print(numbers.cumsum(axis=1))
    # print(numbers.cumsum())

values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
calculate(values)