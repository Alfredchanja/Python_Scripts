#Alfred Gachanja
#25-06-2023
#This program contains some lists prints them to the terminal.
#In this program I learn how to use lists in python.

#Creating a list.
print("Printing a list.\n")
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#Accessing elements in a list.
print("\nAccessing and manipulating the elements in the list\n")
print(bicycles[0])
print(bicycles[1].title())
print(bicycles[-1])#This code accesses the last item of a list.

#Using the individual value from a list.
print("\nUsing the items of the list to print a message.")
message = "I own a " + bicycles[2].title() + " bicycle.\n"
print(message)

#Try it yourself
print("Practice.\n")

names = ['Bill', 'Binzare','Ian', 'Sandra', 'Davis']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

print("God loves you " + names[0] + ".")
print("God loves you " + names[1] + ".")
print("God loves you " + names[2] + ".")
print("God loves you " + names[3] + ".")
print("God loves you " + names[4] + ".")