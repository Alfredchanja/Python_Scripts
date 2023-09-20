#Alfred Gachanja
#12-07-2023
#In this program I learn how to use the module function to print an odd or even number.
#All the information is still coming from the user.

number = "Do you know that I can tell you whether a number is odd or even?"
number += "\nTry me give me any number: "

num = input(number)
num = int(num)

if num % 2 == 0:
    print("{} is an even number." .format(num))
else:
    print("{} is an odd number." .format(num))
