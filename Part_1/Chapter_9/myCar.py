"""
Alfred Gachanja
13-08-2023
Importing classes. In this program I use the car module I created.
"""

from car import Car

#Importing multiple classes
#from car import Car, ElectricCar

#Importing an entire class
import car


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

#Modifying an attribute's value directly.
#my_new_car.odometer_reading = 23

my_new_car.update_odometer(2000)
my_new_car.read_odometer()

my_new_car.increase_odometer(100)
my_new_car.read_odometer()

#When importing an entire module to access the class use the dot notation.
my_beetle = car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
