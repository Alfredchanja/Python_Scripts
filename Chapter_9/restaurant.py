"""
Alfred Gachanja
02-08-2023
In this program I am going to create a class.
Then I will use the class to create an instance.
Afterwards I will use the attributes in the instance
 and a couple of methods in the class.
"""

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type, start):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.start = start

    def describe_restaurant(self):
        print("{} is a restaurant in America." .format(self.restaurant_name.title()))
        print("{} specializes in {} cuisine." .format(self.restaurant_name.title(), self.cuisine_type.title()))
    
    def open_restaurant(self):
        print("{} is opened." .format(self.restaurant_name.title()))

#Using methods in class.
restaurant = Restaurant('olive garden', 'italian-american', '1982')
restaurant.describe_restaurant()
restaurant.open_restaurant()

#Using attributes in instance.
print("The restaurant was opened in the year {}.\n" .format(str(restaurant.start.title())))

restaurant_1 =  Restaurant('burger king', 'fast-food', '1953')
restaurant_1.describe_restaurant()

print("The restaurant was opened in the year {}.\n" .format(str(restaurant_1.start.title())))

restaurant_2 = Restaurant('panera bread', 'bakery-cafe', '1987')
restaurant_2.describe_restaurant()

print("The restaurant was opened in the year {}." .format(str(restaurant_2.start.title())))