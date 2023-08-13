"""
Alfred Gachanja
06-08-2023
In this program I am learning how to work with instances and classes.
On the 13th of August I made this file a modules by removing all the instances.
I stored them in seperate files that use this module.
This module describes a car.
In this module I have added some classes from electricCar.py file.
"""

class Car():
    #A simple attempt to represent a car.

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        #Setting a default value for an attribute
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = ("{} {} {}" .format(str(self.year), self.make, self.model))
        return long_name.title()
    
    def read_odometer(self):
        print("This car has {} miles on it." .format(str(self.odometer_reading)))
    
    #Modifying an attributes value through a method.
    #Extending this method to do additional work.
    def update_odometer(self, mileage):
        #Setting the attribute odometer_reading to a given value.
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back the odometer.")

    #Increment an attribute through a method
    def increase_odometer(self, miles):
        if self.odometer_reading + miles >= self.odometer_reading:
            self.odometer_reading += miles
        else:
            print("You cannot roll back the odometer.")

#Instances as attributes
class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        #Print a statement describing the battery size.
        print("This car has a battery size of {}-kw." .format(str(self.battery_size)))

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = ("This car can go appoximately {} miles on full charge." .format(str(range)))
        print(message)
    
    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

#The child class.
class ElectricCar(Car):
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Initializa the attributes specific to the child class.
        """
        super().__init__(make, model, year)
        #Here we create an instance(Battery) and store it in an attribute.
        self.battery = Battery()