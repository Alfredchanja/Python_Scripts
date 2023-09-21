"""
Alfred Gachanja
21-09-2023
This program gives a simulation and visualization of the die class we just created.
"""

from die import  Die as D6
import pygal

# Create a D6
die = D6()

# Make some rolls and store them in a list
results = []
for roll_num in range(1000):
    result = die.rollDice()
    results.append(result)

# Analysing the results. Counting how many times we roll each number.
frequencies = []
for value in range(1, die.numsides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualizing the data. Making a histogram.
hist = pygal.Bar()

hist.title = "The Results of Rolling a one D6 1000 times"
hist.x_labels = [str(num) for num in range(1, die.numsides + 1)]
hist._x_title = "Result"
hist._y_title = "Frequency of the results"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
