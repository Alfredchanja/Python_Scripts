"""
Alfred Gachanja
16-08-2023
In this program I learn how to handle errors with exceptions.
Handling the ZeroDivisionError exception
21-08-2023
In this program I learn how to use exception to prevent crashes.
"""

#try:
#    print(5/0)
#except ZeroDivisionError:
#    print("You cannot divide a number by zero!")

print("Give me two numbers and I will divide them.")
print("Enter 'q' to quit")

while True:
    firstNum = input("\nFirst number: ")
    if firstNum == 'q':
        break
    secondNum = input("Second number: ")
    if secondNum == 'q':
        break
    #wrapping the line that might produce the error in a try-except block.
    #The program also includes an else block.
    try:
        try:
            answer = int(firstNum)/int(secondNum)
        except ValueError:
            print("Please enter an integer.")
    except ZeroDivisionError:
        print("You cannot divide a number by Zero!")
    else:
        try:
            print(answer)
        #Here we pass the error silently.
        except NameError:
            pass
