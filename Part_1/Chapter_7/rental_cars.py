#Alfred Gachanja
#12-07-2023
#This is me practicing what I have been learning about the input function.

car = input("What kind of car would you like to rent? ")

if car == 'bmw':
    print("Lets seee if we can find you a {}." .format(car.upper()))
else:
    print("Lets see if we can find you a {}." .format(car.title()))