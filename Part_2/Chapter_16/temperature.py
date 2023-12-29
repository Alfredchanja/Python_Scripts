"""
Alfred Gachanja
27-09-2023
This program reads some of the data contained in sitka_weather_07-2014.csv file.
"""

import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Getting temperatures from the file.
filename = 'C:/Users/user/Documents/Programming/Python_Programming/Python_Scripts/Part_2/Chapter_16/sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    temps = []
    for row in reader:
        temps.append(row[1])

    #I used this to remove the symbology that was show when printing the list.
    date, temperatures = [], []
    for temp in temps:
        current_date = datetime.strptime(row[0], "%d")
        date.append(current_date)

        high = float(temp)
        temperatures.append(high)

    # print(temperatures)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(date, temperatures, c='red')

# Format plot
plt.title("Daily temperatures for Sitka, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()