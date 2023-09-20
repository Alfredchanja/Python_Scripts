#Alfred Gachanja
#06-07-2023
#This program prints a bunch of python dictionaries.
#In this program I learn to work with dictionaries in python
# and their key-value pairs.

alien_0 = {'colour': 'green', 'points': 5}

print("The colour of the alien is: {}".format(alien_0['colour']))
print("The points earned from the alien are: {}" .format(alien_0['points']))
print("The length of the dictionary is {}.\n" .format(len(alien_0)))

#Adding new key-value pair to an existing dictionary.
alien_0['x-position'] = 0
alien_0['y-position'] = 25
alien_0['speed'] = 'slow'

print("The position of the alien is ({},{})" .format(alien_0['x-position'], alien_0['y-position']))
print("The length of the dictionary is {}." .format(len(alien_0)))

#Starting an empty dictionary.
alien_1 = {}

alien_1['colour'] = 'yellow'
alien_1['points'] = 10
alien_1['x-position'] = 25
alien_1['y-position'] = 0
alien_1['speed'] = 'medium'

print("\n" + str(alien_1))
print("\nThe colour of the alien is: {}" .format(alien_1['colour']))
print("The points earned form the alien are: {}" .format(alien_1['points']))
print("The position of the alien is ({})" .format(alien_1['x-position'], alien_1['y-position']))
#Modifying the values of a dictionary.
alien_0['points'] = 4
alien_1['points'] = 8

print("\nThe points for alien_0 is modified to: {}" .format(alien_0['points']))
print("The points for alien_1 is modified to: {}\n" .format(alien_1['points']))

#Changing the x-position of our aliens_0
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed'] == 'fast':
    x_increment = 3
else:
    x_increment = 4

alien_0['x-position'] = alien_0['x-position'] + x_increment
print("The new postion of alien_0 is: ({}, {})" .format(alien_0['x-position'], alien_0['y-position']))

#Changing the x_position of alien_1
if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
elif alien_1['speed'] == 'fast':
    x_increment = 3
else:
    x_increment = 4

alien_1['x-position'] = alien_1['x-position'] + x_increment
print("The new position of alien_1 is: ({}, {})" .format(alien_1['x-position'], alien_1['y-position']))

#Try it yourself
print("\nPractice\n ")

person = {
    'first_name': 'alfred',
    'second_name':'gachanja',
    'age': 21,
    'city': 'nairobi',
    }

print("My name is {} {}" .format(person['first_name'].title(), person['second_name'].title()))
print("I am {} years old." . format(person['age']))
print("I stay in {} city." .format(person['city'].title()))

person['fav_number'] = 12
print("My favourite number is {}." .format(person['fav_number']))
