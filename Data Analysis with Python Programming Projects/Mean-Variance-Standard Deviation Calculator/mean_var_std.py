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

  try:
    # Converting the list into a 3 x 3 numpy array.
    numbers = np.array(digits).reshape(3, 3)
    # print(numbers.shape)
    # print(numbers)

    # Calculate the mean of the newly formed array.
    m_axis1 = numbers.mean(axis=0) # Mean along axis1 - column.
    m_axis2 = numbers.mean(axis=1) # Mean along axis2 - row.
    m_flattened = numbers.mean()

    # print(m_axis1)
    # print(m_axis2)
    # print(m_flattened)

    # Calculate the variance.
    v_axis1 = numbers.var(axis=0) # Variance along axis1 - column.
    v_axis2 = numbers.var(axis=1) # Variance along axis2 - column.
    v_flattened = numbers.var()

    # print(numbers.var(axis=0))
    # print(numbers.var(axis=1))
    # print(numbers.var())

    # Calculate the standard deviation.
    std_axis1 = numbers.std(axis=0) # Standard deviation along axis1 - column.
    std_axis2 = numbers.std(axis=1) # Standard deviation along axis2 - row.
    std_flattened = numbers.std()

    # print(numbers.std(axis=0))
    # print(numbers.std(axis=1))
    # print(numbers.std())

    # Find the max value.
    max_axis1 = numbers.max(axis=0) # Max value along axis1 - column.
    max_axis2 = numbers.max(axis=1) # Max value along axis2 - column.
    max_flattened = numbers.max()

    # print(numbers.max(axis=0))
    # print(numbers.max(axis=1))
    # print(numbers.max())

    # Find the min value.
    min_axis1 = numbers.min(axis=0) # Min value along axis1 - column
    min_axis2 = numbers.min(axis=1) # Min value along axis2 - row
    min_flattened = numbers.min()

    # print(numbers.min(axis=0))
    # print(numbers.min(axis=1))
    # print(numbers.min())

    # Calculate the sum.
    sum_axis1 = numbers.sum(axis=0) # Sum along axis1 - column.
    sum_axis2 = numbers.sum(axis=1) # Sum along axis2 - row.
    sum_flattened = numbers.sum()

    # print(numbers.sum(axis=0))
    # print(numbers.sum(axis=1))
    # print(numbers.sum())

    # Calculate the cumulative sum.
    # cs_axis1 = numbers.cumsum(axis=0) # Cumulative sum along axis1 - column.
    # cs_axis2 = numbers.cumsum(axis=1) # Cumulative sum along axis2 - row
    # cs_flattend = numbers.cumsum()

    # print(numbers.cumsum(axis=0))
    # print(numbers.cumsum(axis=1))
    # print(numbers.cumsum())

    # Creating a dictionary that stores all the calculations
    calculations = {
      'mean': [list(m_axis1), list(m_axis2), m_flattened],
      'variance': [list(v_axis1), list(v_axis2), v_flattened],
      'standard deviation': [list(std_axis1), list(std_axis2), std_flattened],
      'max': [list(max_axis1), list(max_axis2), max_flattened],
      'min': [list(min_axis1), list(min_axis2), min_flattened],
      'sum': [list(sum_axis1), list(sum_axis2), sum_flattened],
      # 'cumulative sum': [list(cs_axis1), list(cs_axis2), list(cs_flattend)],
    }
    # print(calculations) 
    return calculations

  except ValueError:
      raise ValueError("List must contain nine numbers.")
  