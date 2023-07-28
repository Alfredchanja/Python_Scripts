#Alfred Gachanja
#19-07-2023
#In this program I learn how to pass arguments in functions.

#Positional Arguments
#In positional arguments the order of passing the arguments matters a lot.
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a {}." .format(animal_type))
    print("My {}'s name is {}." .format(animal_type.title(), pet_name.title()))

describe_pet('henry', 'hamster')
describe_pet('rock')
#Keyword Argument
#You associate the the name and the value directly when you call the function.
describe_pet(animal_type='cat', pet_name='puss')