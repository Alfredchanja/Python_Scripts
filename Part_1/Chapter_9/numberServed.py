"""
Alfred Gachanja
02-08-2023
In this program I am going to create a class.
Then I will use the class to create an instance.
Afterwards I will use the attributes in the instance
 and a couple of methods in the class.
"""

class Restaurant():
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

restaurant = Restaurant('olive garden', 'america', 'italian-american', '1982')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(1000000)
restaurant.increase_number_served(1000)

restaurant_1 =  Restaurant('burger king', 'america', 'fast-food', '1953')
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
restaurant.set_number_served(2000000)
restaurant.increase_number_served(2000)

restaurant_2 = Restaurant('panera bread', 'france', 'bakery-cafe', '1987')
restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()
restaurant.set_number_served(3000000)
restaurant.increase_number_served(3000)

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, location, cuisine_type, start):
        super().__init__(restaurant_name,location, cuisine_type, start)
        self.flavours = ['chocolate', 'vanilla', 'strawberry']
    
    def display_flavour(self):
        for flavour in self.flavours:
            print(flavour)

restaurant_3 = IceCreamStand('creamy inn', 'africa', 'ice cream', 1987)
restaurant_3.describe_restaurant()
restaurant_3.open_restaurant()
restaurant_3.display_flavour()