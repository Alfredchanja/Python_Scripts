"""
Alfred Gachanja
15-08-2023
In this program I am practicing how to access files in python.
"""

filename = 'textFiles/learningPython.txt'

#Print the content once by reading the entire file.
#with open(filename) as fileContent:
#    content = fileContent.read()

#print(content)

#Print by looping over the file content.
#with open(filename) as fileContent:
#    for line in fileContent:
#        print(line.strip())

#Print by storing in a list and using the content outside the with block.
with open(filename) as fileContent:
    content = fileContent.readlines()
    #print(content)

#for line in content:
#    print(line.strip())

pyString = ""
for line in content:
    pyString += line
    
#print(pyString)
#pyString.replace('python', 'C')
#print(pyString)