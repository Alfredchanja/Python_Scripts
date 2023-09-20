"""
Alfred Gachanja
16-08-2023
In this program I practice on using while loops to obtain
user data and store the data in a file.
"""

filename = 'textFiles/responses.txt'

print("Type 'exit' to leave cycle.")
while True:
    name = input("Name: ")  
    if name != 'exit':
        programming = input("Why do you love progamming?\n")
        with open(filename, 'a') as fileObjects:
            fileObjects.write(f"This is why {name.title()} loves programming;\n\t'{programming}.'\n")
    else:
        break
    