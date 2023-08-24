"""
Alfred Gachanja
24-08-2023
In this program I print the users favourite number.
 This program is a combination of favouriteNumber.py.

"""

import json

filename = 'jsonFiles/favouriteNumber.json'

try:
    with open(filename) as fileObject:
        number = json.load(fileObject)
        print(f"Your favourite number is {number}.")
except FileNotFoundError:
    favNum = input("What is your favourite number? ")
    with open(filename, 'w') as fileObject:
        json.dump(favNum, fileObject)
        print(f"I know your favourite number.")