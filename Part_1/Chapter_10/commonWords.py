"""
Alfred Gachanja
22-08-2023
In this program I practice how to read through a text file and find common words.
"""

filename = 'textFiles/alice.txt'

with open(filename) as fileObject:
    content = fileObject.read()
    print(content.lower().count('the'))