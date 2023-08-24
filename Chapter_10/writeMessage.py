"""
Alfred Gachanja
16-08-2023
In this program I learn how to information tao an empty file.
"""

filename = 'textFiles/programming.txt'

with open(filename,'w') as fileObject:
    fileObject.write("I love programming.\n")
    fileObject.write("I love creating games.\n")

with open(filename, 'a') as fileObject:
    fileObject.write("I also love findingmeaning in large datasets.\n")
    fileObject.write("I love creating apps that run in a browser.\n")