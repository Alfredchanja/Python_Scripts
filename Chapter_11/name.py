"""
Alfred Gachanja
29-08-2023
In this program I am using the module nameFunction to write a neatly formatted name.
"""

from nameFunction import get_formatted_name

print("Enter 'q' to quit at anytime.")

while True:
    first = input("Please enter your first name: ")
    if first == 'q':
        break
    last = input("Please enter your last name: ")
    if last == 'q':
        break
    
    formattedName = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formattedName}.")