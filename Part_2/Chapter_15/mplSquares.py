"""
Alfred Gachanja
10-09-2023
Testing matplotlib
"""

import matplotlib.pyplot as plt

input_values =[1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

#Sets the chart title and lables the axis.
plt.title("Square Numbers", fontsize=14)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#Sets the size of thetick lables.
plt.tick_params(axis='both', labelsize = 14)

plt.show()