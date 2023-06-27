#Alfred Gachanja
#26-06-2023
#This program organises a list in a particular order.
#In this porogram I learn the various way that python provides to organise a list.

#Using the sort() method.
guests = ['nyabuti', 'bill', 'ian', 'esther', 'binzare', 'sandra', 'sharon', 'davis', 'eric', 'chantelleh']
guests.sort()#This method permanently sorts a list in alphabetical order.
print("Permanently sorted in an alphabetical order:")
print(guests)
guests.sort(reverse=True)#This permanently sorts the list in a reverse alphabetical order.
print("\npermanently sorted in reverse alphabetical order:")
print(guests)

#Using the sorted() function.
guests = ['nyabuti', 'bill', 'ian', 'esther', 'binzare', 'sandra', 'sharon', 'davis', 'eric', 'chantelleh']
print("\nHere is the original list:")
print(guests)
print("\nHere is a sorted list:")
print(sorted(guests))#The sorted function temporarily sorts the list.
print(sorted(guests, reverse=True))#This sort the list in reverse order.
print("\nHere is the original list again:")
print(guests)

#Print the original list in reverse order.
print("\nOriginal order of a list:")
print(guests)
guests.reverse()#This method reversers the original order of a list.
print("\nReversed order of a list:")
print(guests)
print(len(guests))#This function gives us the length of a list.
