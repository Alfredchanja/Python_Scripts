#Alfred Gachanja
#25-06-2023
#This program manipulates the items in a list.
#In this program I learn how to change, add, and remove the items in a list.

#Changing the elements of a list.
print("Change the elements of a list.")
motorcycle = ['honda', 'yamaha' , 'suzuki']
print(motorcycle)

motorcycle[0] = 'ducati'
print(motorcycle)

#Adding elements to a list.
print("\nAppending")#This adds the item at the end of the list.
motorcycle.append('honda')
print(motorcycle)
print("\nInserting")#This can add an element at any position in the list.
motorcycle.insert(1, 'bmw')
print(motorcycle)

#Removing elements from a list.
print("\nUsing the del statement.")#Remove the items from any know position.
del motorcycle[1]
print(motorcycle)

#This removes item of the list but allows you access to this item.
# You can also remoe an item of know position.
print("\nUsing the pop method.")
popped_bike = motorcycle.pop()
print(motorcycle)
print(popped_bike)

#This removes the element of the list by stating the values of this element.
print("\nUsing the remove method.")
motorcycle.remove('ducati')
print(motorcycle)

#Try it yourself
print("\nPractice.\n")

guest_List = ['bill', 'ian', 'binzare', 'sandra', 'davis', 'eric']
print(guest_List[0].title() + " is invited to Alfred's dinner party.")
print(guest_List[1].title() + " is invited to Alfred's dinner party.")
print(guest_List[2].title() + " is invited to Alfred's dinner party.")
print(guest_List[3].title() + " is invited to Alfred's dinner party.")
print(guest_List[4].title() + " is invited to Alfred's dinner party.")
print(guest_List[5].title() + " is invited to Alfred's dinner party.\n")

popped_guest = guest_List.pop(3)
print(popped_guest.title() + " sent an apology that she cannot make it for the dinner party.")

guest_List.insert(3, 'sharon')
print(guest_List[3].title()+ " will take her place at the dinner party\n")

#More space more guests.
guest_List.insert(0, 'nyabuti')
guest_List.insert(3, 'esther')
guest_List.append('chantelleh')

print(guest_List)
print(guest_List[0].title() + " is invited to Alfred's dinner party.")
print(guest_List[1].title() + " is invited to Alfred's dinner party.")
print(guest_List[2].title() + " is invited to Alfred's dinner party.")
print(guest_List[3].title() + " is invited to Alfred's dinner party.")
print(guest_List[4].title() + " is invited to Alfred's dinner party.")
print(guest_List[5].title() + " is invited to Alfred's dinner party.")
print(guest_List[6].title() + " is invited to Alfred's dinner party.")
print(guest_List[7].title() + " is invited to Alfred's dinner party.")
print(guest_List[8].title() + " is invited to Alfred's dinner party.")

#Saddest part of the program. Less space.
print("\nDue to the unavailability of space I can only invite two guests to dinner\n")

popped_guest0 = guest_List.pop(0)
popped_guest2 = guest_List.pop(1)
popped_guest3 = guest_List.pop(1)
popped_guest4 = guest_List.pop(1)
popped_guest5 = guest_List.pop(1)
popped_guest6 = guest_List.pop(1)
popped_guest7 = guest_List.pop(1)

print("Really sorry " + popped_guest0.title() + " I cannot invite you to the dinner party.")
print("Really sorry " + popped_guest2.title() + " I cannot invite you to the dinner party.")
print("Really sorry " + popped_guest3.title() + " I cannot invite you to the dinner party.")
print("Really sorry " + popped_guest4.title() + " I cannot invite you to the dinner party.")
print("Really sorry " + popped_guest5.title() + " I cannot invite you to the dinner party.")
print("Really sorry " + popped_guest6.title() + " I cannot invite you to the dinner party.")
print("Really sorry " + popped_guest7.title() + " I cannot invite you to the dinner party.\n")

#The only two invited.
print(guest_List[0].title() + " you are still invited to the dinner party.")
print(guest_List[1].title() + " you are still invited to the dinner party.\n")

#Empty list.
del guest_List[0]
del guest_List[0]
print(guest_List)