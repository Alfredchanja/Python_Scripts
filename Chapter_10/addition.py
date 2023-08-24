"""
Alfred Gachanja
21-08-2023
In this program I am practicing how to work with the tyoe error.
"""

print("Give me two numbers and I will add them together.")
print("Enter 'q' to quit.\n")

while True:
    firstNum = input("First Number: ")
    if firstNum == 'q':
        break
    secondNum = input("Second Numer: ")
    if secondNum == 'q':
        break
    try:
        sum = int(firstNum) + int(secondNum)
    except ValueError:
        print("Please enter an integer.\n")
    else:
        print(f"{sum}\n")