#Alfred Gachanja
#19-07-2023
#In this program I learn to use functions to get a return value.

def formatted_name(first_name, last_name, middle_name=''):
    """Returns a value of full name."""
    full_name = ("{} {} {}" .format(first_name, middle_name, last_name))
    return full_name.title()

names = formatted_name('alfred', 'mwangi','gachanja')
print(names)

names = formatted_name('alfred', 'gachanja')
print(names)