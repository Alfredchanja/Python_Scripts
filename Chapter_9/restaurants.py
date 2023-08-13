"""
Alfred Gachanja
13-08-2023
This is a model file that stores the general description of a restaurant.
"""

class Restaurants():
    def __init__(self, restaurant_name, location, cuisine_type, start):
        self.restaurant_name = restaurant_name
        self.location = location
        self.cuisine_type = cuisine_type
        self.start = start
        self.numberServed = 0

    def describe_restaurant(self):
        print("{} is a restaurant in {}." .format(self.restaurant_name.title(), self.location.title()))
        print("{} specializes in {} cuisine." .format(self.restaurant_name.title(), self.cuisine_type.title()))
        print("The restaurant was opened in the year {}." .format(str(self.start)))
    
    def open_restaurant(self):
        print("{} is opened." .format(self.restaurant_name.title()))
    
    def set_number_served(self, served):
        self.numberServed = served
        print("We have served over {} people today." .format(str(self.numberServed)))

    def increase_number_served(self, persons):
        self.numberServed += persons
        print("We have served {} people today.\n" .format(str(self.numberServed)))