"""
Alfred Gachanja
14-09-2023
In this program I am going to plot a single point using the scatter function
"""

import matplotlib.pyplot as plt

x_values = list (range(1, 1001))
y_values = [x**2 for x in x_values]

#Removing outline from data points, defining custom color and using color maps.
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.plasma, edgecolors='none', s=40)

#Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)

#Set the range for each axis.
plt.axis([0, 1100, 0, 1100000])

#Saving your plot automatically. You can save as .png or .jpeg
plt.savefig('squares_plot.jpeg', bbox_inches='tight')