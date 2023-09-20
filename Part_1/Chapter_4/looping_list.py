#Alfred Gachanja
#28-06-2023
#This program loops through a list to avoid repeating my codes
#In this program I learn how to loop through a list.

#The for loop.
guest_list = ['bill', 'binzare', 'ian', 'sandra', 'nyabuti', 'esther', 'chantelleh', 'davis', 'eric']
guest_list.sort()
print("THE GUEST LIST.\n")
for guest in guest_list:
    print(guest.title())
#printing a message with a for loop.
print("\nTHE INVITATION.\n")
for guest in guest_list:
    print(guest.title() + " is invited to Alfred's dinner party.")

print("\nI cannot wait to see you guys there!")