"""
Alfred Gachanja
13-08-2023
In this program I learn how to work with the Python Standard Library.
"""

from random import randint

class Dice():
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_dice(self):
        if self.sides == 6:
            x = randint(1, 6)
            print(x)
        elif self.sides != 6:
            x = randint(1, self.sides)
            print(x)

sixSidedDice = Dice()
sixSidedDice.roll_dice()

tenSidedDice = Dice(10)
tenSidedDice.roll_dice()

twentySidedDice = Dice(20)
twentySidedDice.roll_dice()