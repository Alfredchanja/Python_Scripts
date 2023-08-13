"""
Alfred Gachanja
1-08-2023
In this program I am learning about object oriented programming
 using classes.
"""

class Dog():
    #A simple attempt to model a dog.

    def __init__ (self, name, age):
        #Initializing the name and age attributes.
        self.name = name
        self.age = age

    def sit(self):
        #Simulate the dog sitting inresponse to a command.
        print("{} is now sitting." .format(self.name.title()))

    def roll_over(self):
        #Simulate the dog rolling over inresponse to command.
        print("{} is rolling over." .format(self.name.title()))

#This is called making an instance from a class.
my_dog = Dog('rock', 24)

#This is how we access the attributes of an instance.
print("My dog's name is {}." .format(my_dog.name.title()))
print("{}'s is {} years old." .format(my_dog.name.title(), str(my_dog.age)))

#Calling the methods in the class dog.
my_dog.sit()
my_dog.roll_over()
