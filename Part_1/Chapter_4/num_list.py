#Alfred Gachanja
#29-06-2023
#This prints numercal figures from a list.
#In this program I learn how to work with numbers in a list.

#Using the range function.
for value in range(1, 6):
    print(value)

#Using range function to make a list.
number = list(range(1, 6))

print(number)

#Printing even numbers using the range function.
even_num = list(range(2, 11, 2))

print("\nEven numbers:")
print(even_num)

#Printing odd numbers using the range function.
odd_num = list(range(1, 11, 2))

print("\nOdd numbers:")
print(odd_num)

#Square numbers using the range function.
squares = []

for value in range(1, 11):
    squares.append(value**2)

print("\nSquares")
print(squares)
print("The minimum square in the list is: " + str(min(squares)))
print("The maximum square in the list is: " + str(max(squares)))
print("The sum of the squares in the list is: " + str(sum(squares)))

#PRACTICE
print("\nPractice\n")

for value in range(1, 21):
    print(value)

num = list(range(1, 1000001))

print("\nThe minumum number in the list is: " + str(min(num)))
print("The maximum number in the list is:" + str(max(num)))
print("The sum from one to a million is:" + str(sum(num)) + "\n")

odd_num = list(range(1, 20, 2))

print("Odd numbers:")
for value in odd_num:
    print(value)

multiple_3 = list(range(3, 30, 3))

print("\nMultiples of three:")
for three in multiple_3:
    print(three)

cubes = []

for cube in range(1,10):
    cubes.append(cube**3)

print("\nThe third power")
print(cubes)

print("\nList Compression.")

cubes = [cube**3 for cube in range(1,10)]

print(cubes)
