#Alfred Gachanja
#14-07-2023
#In this program I learn how to work with while loop
# and dictionaries.

#Filling a Dictionary with user's input.

#Let us first start by creating an empty dictionary.
responses = {}

#Set a flag to indicate that the polling is active.
polling_active = True

while polling_active:
    #Prompt the user for a name and a response.
    name = input("\nWhat is your name? ")
    response = input("What city would you like to visit? ")

    #Store the responses in a dictionary.
    responses [name] = response

    #Find our if they would like to take the poll.
    repeat = input("would you like to let someone else take the poll?(yes/no) ")
    if repeat == 'no':
        polling_active = False
    
#The polling is complete now show the results.
print("\n--- Poll Results ----")
for name, response in responses.items():
        print("{} would like go to {} city." .format(name.title(), response.title()))