"""
Alfred Gachanja
21-08-2023
In this program I moved a bulk of the code for alice.py to form a function.
This function counts the number of words in a text file.
"""

def countWords (filename):
    #Counts the approximate number of words in a file.
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        #Count the number of word in file.
        word = contents.split()
        numWord = len(word)
        print(f"The file {filename} has about {str(numWord)} number of words.")

#filename = 'alice.txt'
#countWords(filename)

filenames = ['textFiles/alfredGachanja.txt', 'textFiles/alice.txt',
            'textFiles/learningPython.txt', 'textFiles/guestBook.txt']
for file in filenames:
    countWords(file)