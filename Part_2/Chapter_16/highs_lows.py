"""
Alfred Gachanja
26-09-2023
In this program we are examining the first line of the csv file,
  which contains a series of headers for the data.
"""

import csv

filename = 'C:/Users/user/Documents/Programming/Python_Programming/Python_Scripts/Part_2/Chapter_16/Jan2023_Nairobi_weather_data.csv'
with open(filename) as f:
    header_row = next(csv.reader(f))
    
    #Printing the headers and their positions.
    for index, column_header in enumerate(header_row):
        print(index, column_header)
