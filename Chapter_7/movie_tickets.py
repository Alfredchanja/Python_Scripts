#Alfred Gachanja
#13-07-2023
#In this program I am practicing what I learned about the while and the user's input.

ages = "\nPlease tell me your age."
ages += "\nEnter 'quit' when you are done: "

active = True

while active:
    age = input(ages)

    if age == 'quit':
        break
    elif int(age) < 3:
        print("Your entrance fee is free.")
    elif int(age) < 12:
        print("Your ticket is $10.")
    elif int(age) > 12:
        print("Your ticket is $15.")