"""
Alfred Gachanja
27-07-2023
In this program I am using a function to print a list of my friends.
"""

def show_friends(friends):
    print("This is a list of all my friends.")
    for friend in friends:
        print("\t{}" .format(friend.title()))

friends = ['bill', 'davis', 'eric', 'kelvin', 'sandra', 'binzare']
show_friends(friends)