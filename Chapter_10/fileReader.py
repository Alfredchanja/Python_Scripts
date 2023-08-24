"""
Alfred Gachanja
14-08-2023
In this program I am learning how to
read the entire the content of a txt.
"""

with open('piDigits.txt') as file_object:
    contents = file_object.read()
    print(contents)

print("\nReading a text file line by line.\n")

#Reading a file line by line.
with open('piDigits.txt') as fileObject:
    for line in fileObject:
        print(line.rstrip())

print("\nRelative file path\n")

#Reading files store in a different location using the relative file path.
with open('textFiles/alfredGachanja.txt') as userInfo:
    user = userInfo.read()
    print(user)

print("\nAbsolute file path\n")

#Reading files stored in a differet location using the absolute path.
#Remember to include the name of the file in the path.(fileName.txt)
filePath = 'C:/Users/user/Documents/Programming/Python Programming/\
Python_Scripts/Chapter_10/textFiles/alfredGachanja.txt'

with open(filePath) as Info:
    person = Info.read()
    print(person)