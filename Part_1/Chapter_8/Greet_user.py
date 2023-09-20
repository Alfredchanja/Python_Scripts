"""
Alfred Gachanja
25-07-2023
In this program I learn how to make lists efficient by using functions.
"""

def greet_user(names):
    """Prints a greeting to all the users in the list"""
    for name in names:
        print("Hello {}!" .format(name.title()))

usernames = ['alfred', 'david', 'james', 'john']
greet_user(usernames)