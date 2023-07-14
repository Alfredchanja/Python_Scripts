#Alfred Gachanja
#12-07-2023
#In this program I am practicing what I learned about the input() and the int() function.

people = input("You want a table for how many people? ")
people = int(people)

if people > 8:
    print("You will have to wait for a table.")
else:
    print("Right this way, we have a table for you.")