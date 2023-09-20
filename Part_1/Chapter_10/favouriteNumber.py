"""
Alfred Gachanja
24-08-2023
In this program I am going to prompt a user for their favourite number.
"""

import json

favNum = input("What is your favourite number? ")

filename = 'jsonFiles/favouriteNumber.json'

with open(filename, 'w') as fileObject:
    json.dump(favNum, fileObject)
    print(f"I know your favourite number.")