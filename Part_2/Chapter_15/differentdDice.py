"""
Alfred Gachanja
21-09-2023
This program gives a simulation and visualization of two different sided dice.
"""

from die import  Die as D6
import pygal

# Create two D6
die_1 = D6()
die_2 = D6(10)

# Make some rolls and store them in a list
results = []
for roll_num in range(50000):
    result = die_1.rollDice() + die_2.rollDice()
    results.append(result)

# Analysing the results. Counting how many times we roll each number.
frequencies = []
max_results = die_1.numsides + die_2.numsides
for value in range(2, max_results+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualizing the data. Making a histogram.
hist = pygal.Bar()

hist.title = "The Results of Rolling a D6 Dice and a D10 Dice 50000 times"
hist.x_labels = [str(x) for x in range(2, max_results+1)]
hist._x_title = "Result"
hist._y_title = "Frequency of the results"

hist.add('D6 + D10', frequencies)
hist.render_to_file('different_dice_visual.svg')
