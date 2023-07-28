"""
Alfred Gachanja
28-07-2023
In this program I use tuple to form an arbitraty number of arguments.
"""

def make_sandwich(*sandwiches):
    print(sandwiches)
    print("Here are the sandwiched in our menu:")
    for sandwich in sandwiches:
        print("- {}" .format(sandwich.title()))

make_sandwich('egg sandwich', 'seafood sandwich', 
              'roast beef sandwich', 'grilled cheese sandwich',
              'ham sandwich',)