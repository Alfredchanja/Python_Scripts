"""
Alfred Gachanja
16-08-2023
In this program I practice writing in a file using code.
"""

filename = 'textfiles/guest.txt'

name = input("Name: ")

with open(filename, 'w') as fileObject:
    fileObject.write(name)