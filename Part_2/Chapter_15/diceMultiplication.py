"""
Alfred Gachanja
21-09-2023
This program gives a simulation and visualization of the multiplication two D6 dice.
"""

from die import  Die as D6
import pygal

# Create two D6
die_1 = D6()
die_2 = D6()

# Make some rolls and store them in a list
results = []
for roll_num in range(1000):
    result = die_1.rollDice() * die_2.rollDice()
    results.append(result)

# Analysing the results. Counting how many times we roll each number.
frequencies = []
max_results = die_1.numsides
for value in range(1, max_results+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualizing the data. Making a histogram.
hist = pygal.Bar()

hist.title = "The Results of Rolling two D6 Dice 1000 times"
hist.x_labels = [str(x) for x in range(1, max_results+1)]
hist._x_title = "Result"
hist._y_title = "Frequency of the results"

hist.add('D6 + D6', frequencies)
hist.render_to_file('dicetimesdice_visual.svg')
