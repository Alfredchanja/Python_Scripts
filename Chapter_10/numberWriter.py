"""
Alfred Gachanja
23-08-2023
In this program I learn how to use the json module to store data.
The json.dump() is a function that is used by python to store data in a file.
It requires two arguments: the data to be stored and
 the file it can use to store the data.
"""

import json

numbers = [2, 4, 3, 5, 6, 7]

filename = 'jsonFiles/numbers.json'
with open(filename, 'w') as fileObject:
    json.dump(numbers, fileObject)