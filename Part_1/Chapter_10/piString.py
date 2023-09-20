"""
Alfred Gachanja
14-08-2023
In this program I am learaning how to work with the contents
of a text file.
"""

filename = 'textFiles/piMillionDigits.txt'

with open(filename) as fileObject:
    lines = fileObject.readlines()

piString = ''
for line in lines:
    piString += line.strip()

print(piString[:52])
print(len(piString))

birthday = input("Enter your birthday in the form of mmddyy: ")
if birthday in piString:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")