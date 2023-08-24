"""
Alfred Gachanja
23-08-2023
In this program I learn how to store and use user generated data
 using Json.
24-08-2023
In combined the code in this file and the greetUser.py.
 Then I refactored my code. 
 Refactoring is the processes of breaking up a code into a series of functions.
"""

import json

#Load user name if stored in a json file.
# Other prompt for the useer name and store it.

def get_stored_username():
    # This function greets the user by name.
    fileName = 'jsonFiles/names.json'

    try:
        with open(fileName) as fileObject:
            username = json.load(fileObject)
    except FileNotFoundError:
         return None
    else:
         return username

def get_new_username():
        username = input("What is your name? ")
        fileName = 'jsonFiles/names.json'
        with open(fileName, 'w') as fileObject:
            json.dump(username, fileObject)
        return username
def greetUser():
    username = get_stored_username()
    confirmUserName = input(f"Is {username} your name?(y\\n) ")
    #This confirm the name of the user.
    if confirmUserName == 'y':
         print(f"Welcome back {username.title()}!")
    elif confirmUserName == 'n':
        username = get_new_username()
        print(f"I will remember you name when you come back {username.title()}!")

greetUser()