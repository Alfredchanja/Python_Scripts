#Alfred Gachanja
#12-07-2023
#In this program I learn how to use the 'continue' statement.
#The 'continue' statement returns the program to the beginning of the loop and ignores the rest of the code.

number = 0

while number < 10:
    number += 1
    if number % 2 == 0:
        continue
    else:
        print(number)