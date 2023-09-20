"""
Alfred Gachanja
19-09-2023
Creating a class for random walk.
"""

from random import choice

class RandomWalk():
    #A class that generates a random walk.

    def __init__(self, num_points=5000):
        #Initialize attributes for a walk
        self.num_points = num_points

        #All walks start at zero.
        self.x_values = [0]
        self.y_values = [0]

    def getSteps(self):
        # Determine the direction and distance of a step.

        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        step = direction * distance

        return step
           

    def fillWalk(self):
        # Calculate all points in a step.

        # Keep calculating until the desire length.
        while len(self.x_values) < self.num_points:
            
            # Choose the direction and distance to follow.
            x_step = self.getSteps()
            y_step = self.getSteps()

            # Rejec moves that are no made.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate next x and y values
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            # Add the values of the next x and y to the x and y value list.
            self.x_values.append(next_x)
            self.y_values.append(next_y)