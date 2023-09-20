#Alfred Gachanja
#05-07-2023
#This program outputs different kinds of conditional statements.
#In this program I learn how to work with the different kinds of 'if statements'.

#Simple if statement.
age = 19

print("If statement.\n")

if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote?")

#If-else statement.
age = 17

print("\nIf-else statement.\n")

if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote?")
else:
    print("Sorry, you are not old enought to vote!")
    print("Please register as a voter as soon as you turn 18.")

#The if-elif-else chain.

age = 21

print("\nIf-elif-else statement.\n")

if age < 4:
    print("Entrance is free.")
elif age >= 4 and age < 18:
    print("Entrance fee is $5.")
else:
    print("Entrance fee is $10.")

#Using multiple elif blocks.
age = 70

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("Your entrance fee is $" + str(price) + "." )

#Omitting the else block.
age = 70

print("\nThis block of code omits the else block and insteaded uses the elif.\n")

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print("Your entrance fee is $" + str(price) + "." )

#Try it yourself.
print("\nPractice\n")

alien_colours = ['green', 'yellow', 'blue']

for alien_colour in alien_colours:
    if alien_colour == 'green':
        points = 5
    if alien_colour  == 'yellow':
        points = 10
    if alien_colour == 'blue':
        points = 15

    print("You have earned " + str(points) + "!")

#Using if statements with multiple list. Try it yourself.

print("\nPractice\n")

user_names = ['kelvin', 'dennis', 'admin', 'john', 'eric']
new_users = ['ERIC', 'antony', 'sheila', 'moreen', 'dennis']

user_names.sort()
new_users.sort()

for user_name in user_names:
    if user_name == 'admin':
        print("Hello {}, would you like to see a status report?" .format(user_name.title()))
    else:
        print("Hello {}, thank you for logging in again." .format(user_name.title()))

if user_names == []:
    print("We need to find some users!")

print("\n")

for new_user in new_users:
    if new_user == new_user.upper():
        print("{} please use lowercase letters scheme.\n" .format(new_user)) 
    elif new_user in user_names:
        print("The user {} already exists. Please find a new user name." .format(new_user.title()))      
    else:
        print("{} is your new username." .format(new_user.title()))
    
#Ordinal Numbers.
ordered_num = [1, 3, 5, 2, 8, 6, 4, 7, 9, 0]
ordered_num.sort()

print("\nPrinting Ordinal Numbers")
for number in ordered_num:
    if number == 1:
        print("{}st" .format(str(number)))
    elif number == 2:
        print("{}nd" .format(str(number)))
    elif number == 3:
        print("{}rd" .format(str(number)))
    elif number == 0:
        print(number)
    else:
        print("{}th" .format(str(number)))