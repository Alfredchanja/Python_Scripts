"""
Alfred Gachanja
16-08-2023
In this program I learn how to store user data in a textfile.
"""

filename = 'textFiles/guestBook.txt'

print("Type 'exit' to leave the cycle.")
while True:
    name = input("Name: ")
    if name != 'exit':
        print(f"Hello {name.title()}!")
        with open(filename, 'a') as fileObject:
            date = 81623
            fileObject.write(f"{name.title()} visited on {str(date)}\n")
    else:
        break