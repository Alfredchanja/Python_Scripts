"""
Alfred Gachanja
24-08-2023
In this program I use the name of the user store in a file to print a greeting.
"""

import json

filename = 'jsonFiles/names.json'

with open(filename) as fileObject:
    username = json.load(fileObject)
    print(f"Welcome back {username.title()}!")