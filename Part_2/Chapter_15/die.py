"""
Alfred Gachanja
21-09-2023
In this program I an learning how to use pygal for visualization.
 This is a class that simulates the rolling of a 6 sided dice.
"""

from random import randint
import pygal

class Die():
    # A class representing a single die.

    def __init__(self, numsides = 6):
        # Assumes a six sided die.
        self. numsides = numsides

    def rollDice(self):
        #return a random value form 1 to the number of sides of the dice.
        return randint(1, self.numsides)
    