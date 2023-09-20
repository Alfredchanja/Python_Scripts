#Alfred Gachanja
#06-07-2023
#This program loops through a dictionary's key-values pairs,
# its keys, and values.
#In this program I learn how to loop through a dictionary.

#Looping through all key value pairs.
user_0 = {
    'username_0': 'alfredchanja',
    'first_name': 'alfred',
    'second_name': 'gachanja',
}

for key, value in user_0.items():
    if key == 'username_0':
        print("\nKey: " + key)
        print("value: " + value)
    else:
        print("\nKey: " + key)
        print("Value: " + value.title())

#Looping through the keys in a dictionary.
print("\n")

#You can write the below line of the code with or without the keys() method.
for key in user_0.keys():
    print("Key: " + key)

user_0['username_1'] = 'light_nuru'
user_0['first_1_nm'] = 'nuru'
user_0['second_1_nm'] = 'amudi'
user_0['username_2'] = 'shanteru'
user_0['first_2_nm'] = 'chantelleh'
user_0['second_2_nm'] = 'carrie'

usernames = ['username_1', 'username_2']

print("\n")

for username in user_0.keys():
    if username in usernames:
        print("Your username is {}." .format(username.title()))

#Looping through all the values in a dictionary.
usernms = ['alfredchanja', 'light_nuru', 'shanteru']

print("\n")

for name in user_0.values():
    if name in usernms:
        print("Your username is {}." .format(name))

#Try it yourself.
print("\nPractice\n")

rivers = {
    'nile': 'africa',
    'mississippi': 'north america',
    'amazon river': 'south america',
    }

for river, location in rivers.items():
    print("The {} runs through {}." .format(river.title(), location.title()))

print("\nThese are some of the rivers of the world:")
for river in rivers.keys():
    print("\t{}" .format(river.title()))

print("\nThese are their locations in the world:")
for location in rivers.values():
    print("\t{}" .format(location.title()))