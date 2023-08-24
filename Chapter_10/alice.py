"""
Alfred Gachanja
21-08-2023
In this program I am learning how to handle the FileNotFoundError exceptions.
"""

filename = 'textFiles/alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print(f"Sorry the file {filename} does not exist.")
else:
    #Count the number of word in file.
    word = contents.split()
    numWord = len(word)
    print(f"The file {filename} has about {str(numWord)} number of words.")
