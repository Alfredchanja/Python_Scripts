"""
Alfred Gachanja
21-09-2023
This program gives a simulation and visualization of three D6s Dice.
"""

from die import  Die as D6
import pygal

# Create a D6
die_1 = D6()
die_2 = D6()
die_3 = D6()

# Make some rolls and store them in a list
results = []
for roll_num in range(100000):
    result = die_1.rollDice() + die_2.rollDice() + die_3.rollDice()
    results.append(result)

# Analysing the results. Counting how many times we roll each number.
frequencies = []
max_results = die_1.numsides + die_2.numsides + die_3.numsides
for value in range(3, max_results+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualizing the data. Making a histogram.
hist = pygal.Bar()

hist.title = "The Results of Rolling a one D6 1000 times"
hist.x_labels = [str(num) for num in range(3, max_results + 1)]
hist._x_title = "Result"
hist._y_title = "Frequency of the results"

hist.add('D6', frequencies)
hist.render_to_file('3_D6s_visual.svg')
