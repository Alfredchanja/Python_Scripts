"""
Alfred Gachanja
19-09-2023
In this program I plot on a graph the cubes of a number.
"""

import matplotlib.pyplot as plt

x_values = list (range(1, 5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.plasma, edgecolors='none', s=40)

plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Number", fontsize=14)
plt.ylabel("Cube Values", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([0, 5100, 0, 130000000000])

plt.show()