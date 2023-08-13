"""
Alfred Gachanja
13-08-2023
In this program I import from the restaurants modules.
Try it yourself exercise.
"""

from restaurants import Restaurants

restaurant = Restaurants('olive garden', 'america', 'italian-american', '1982')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(1000000)
restaurant.increase_number_served(1000)