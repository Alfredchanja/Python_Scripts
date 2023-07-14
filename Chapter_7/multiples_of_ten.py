#Alfred Gachanja
#12-03-2023
#This program check for the multiples of ten.

number = input("Lets find the multiples of ten: ")
number = int(number)

if number % 10 == 0:
    print("{} is a multiple of ten." .format(number))
else:
    print("{} is not a multiple of ten." .format(number))