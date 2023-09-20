"""
Alfred Gachanja
27-07-2023
In this program I am using a function to print a list of my friends.
Then I modify the list for my best friends.
"""

def show_friends(friends, bestie):
    print("This is a list of all my friends.")
    while friends:
        friend = friends.pop()

        print("\t{}" .format(friend.title()))
        bestie.append(friend)

def best_friends(bestie):
    for besty in bestie:
        print("My best friend is {}." .format(besty.title()))

friends = ['bill', 'davis', 'eric', 'kelvin', 'sandra', 'binzare']
bestie = []

show_friends(friends[:], bestie)
best_friends(bestie)

print(friends)