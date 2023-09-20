#Alfred Gachanja
#11-07-2023
#In this program I learn how to nest dictionaries.
#Nesting is simply storing dictionaries in a list,
# storing a list of values in a dictionary or
# storing a dictionary inside another dictionary.

#A list of dictionaries.

print("A list of dictionaries.\n")

alien_0 = {'colour': 'green', 'points': 5}
alien_1 = {'colour': 'yellow', 'points': 10}
alien_2 = {'colour': 'blue', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
print("\n")
#You can use nesting to print number of copies of a particular item.
#Making 30 aliens.
aliens_0 = []
aliens_1 = []
aliens_2 = []

for alien_nm in range(30):
    nw_alien_0 = {'colour': 'green', 'points': 5, 'speed': 'slow' }
    nw_alien_1 = {'colour': 'yellow', 'points': 10, 'speed': 'medium'}
    nw_alien_2 = {'colour': 'blue', 'points': 15, 'speed': 'fast'}
    aliens_0.append(nw_alien_0)
    aliens_1.append(nw_alien_1)
    aliens_2.append(nw_alien_2)

print("...")
for alien_0 in aliens_0[-5:]:
    print(alien_0)
print("The total number of green aliens is : {}\n" .format(str(len(aliens_2))))

print("...")
for alien_1 in aliens_1[-5:]:
    print(alien_1)
print("The total number of yellow aliens is : {}\n" .format(str(len(aliens_2))))

print("...")
for alien_2 in aliens_2[-5:]:
    print(alien_2)

print("The total number of blue aliens is : {}\n" .format(str(len(aliens_2))))
#Modifying my aliens.
for alien_0 in aliens_0[-3:]:
    if alien_0['colour'] == 'green':
        alien_0['colour'] = 'yellow'
        alien_0['points'] = 10
        alien_0['speed'] = 'medium'

print("\n3 aliens modified.")
print("...")
for alien_0 in aliens_0[-5:]:
    print(alien_0)

for alien_1 in aliens_1[-3:]:
    if alien_1['colour'] == 'yellow':
        alien_1['colour'] = 'blue'
        alien_1['points'] = 15
        alien_1['speed'] = 'fast'

print("\n3 aliens modified.")
print("...")
for alien_1 in aliens_1[-5:]:
    print(alien_1)

for alien_2 in aliens_2[-3:]:
    if alien_2['colour'] == 'blue':
        alien_2['colour'] = 'red'
        alien_2['points'] = 20
        alien_2['speed'] = 'very fast'

print("\n3 aliens modified.")
print("...")
for alien_2 in aliens_2[-5:]:
    print(alien_2)

#A list in a dictionary.

print("\nA list in a dictionary.\n")

pizza = {
    'crust': 'thick',
    'toppings': ['extra cheese', 'bacon','pineapple'],
}
print("You ordered a {} pizza with the following toppings." .format(pizza['crust']))
for topping in pizza['toppings']:
    print("\t{}" .format(topping))

#Try it your self.

print("\nPractice\n")

user_0 = {
    'username': 'alfredchanja',
    'first_name': 'alfred',
    'second_name': 'gachanja',
    'location': 'nairobi',
    }

user_1 = {
    'username': 'light',
    'first_name': 'nuru',
    'second_name': 'juma',
    'location': 'kiambu',
}

user_2 = {
    'username': 'shanteru',
    'first_name': 'chantelle',
    'second_name':'white',
    'location': 'naivasha',
}

users = [user_0, user_1, user_2]

for user in users:
    print(user)
    print("Your username is {}." .format(user['username']))
    print("Your first name is {}." .format(user['first_name'].title()))
    print("Your second name is {}." .format(user['second_name'].title()))
    print("Your location is {}.\n" .format(user['location'].title()))

user_0['fav_meal'] = ['chapati', 'lentilice', 'cake']
user_1['fav_meal'] = ['chapati', 'beans', 'pizza']
user_2['fav_meal'] = ['rice', 'meat', 'ice cream']

for user in users:
    print("{}'s favourite meal is:" .format(user['first_name'].title()))
    for meal in user['fav_meal']:
        print("\t{} \3" .format(meal.title()))