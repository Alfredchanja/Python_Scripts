"""
Alfred Gachanja
27-07-2023
In this program I learn how to pass an arbitraty number of arguments.
"""

def make_pizza(size, *toppings):
    """The * tells python to make an empty tuple."""
    print(toppings)
    print("Make a {} pizza with the following toppings:" 
          .format(size))
    for topping in toppings:
        print('- {}' .format(topping))
    print("\n")

#I removed the function calls from this file to make it a module.
#Then I created another file called make_pizza.
#There I made the function call and imported the module.