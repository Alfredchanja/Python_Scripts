"""
Alfred Gachanja
23-08-2023
In this program I am learn how to read a file using the json.load() function.
"""

import json

filename = 'jsonFiles/numbers.json'

with open(filename) as fileOject:
    numbers = json.load(fileOject)

print(numbers)