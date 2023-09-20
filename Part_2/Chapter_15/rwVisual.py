"""
Alfred Gachanja
19-09-2023
This program models the path of a polegrain in water.
"""

import matplotlib.pyplot as plt

from randomWalk import RandomWalk

while True:
    rw = RandomWalk(5000)
    rw.fillWalk()
    
    # Setting the size of the plotting window.
    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=2)
    
    # Emphasizing the first and the last points.
    plt.scatter(0, 0, c='green', edgecolors='none', s=75, zorder = 2)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
        s=75, zorder = 2)
    
    # Remove the current axes.
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break