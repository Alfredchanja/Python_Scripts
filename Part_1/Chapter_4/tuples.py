#Alfred Gachanja
#04-07-2023
#This program is all about tuples. Tuples are lists that cannot change.
#In this program I learn to create and work with tuples.

#Working with individual elements of tuple.
dimensions = (200, 50)#Tuples are defines by using parenthesis and not square brackets.

print(dimensions[0])
print(dimensions[1])

#Looping through a tuple.
print("\nLooping.\n")
for dimension in dimensions:
    print(dimension)

#Wring over a tuple.
print("\nWriting over.\n")
print("Original dimensions:")
for dimension in dimensions:
    print("\t" + str(dimension))

dimensions = (400, 100)

print("\nModified dimensions:")
for dimension in dimensions:
    print("\t" + str(dimension))

#Practice
print("\nPractice\n")

buffet = ('vege-buggers', 'tofu', 'scarambled eggs', 'chapati', 'lentiles stew')

print("Food served in a buffet:")
for food in buffet:
    print("\t" + food.title())

buffet = ('vege-buggers', 'tofu', 'beans', 'rice', 'lentiles stew')

print("\nThe menu has been changed to:")
for food in buffet:
    print("\t" + food)