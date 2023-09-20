"""
Alfred Gachanja
22-08-2023
In this program I am practicing how to read some text in a text file.
"""

filenames = ['textFiles/cat.txt', 'textFiles/dog.txt']

for file in filenames:
    try:
        with open(file) as fileObject:
            content = fileObject.read()
            print(f"{content}\n")
    except FileNotFoundError:
        pass