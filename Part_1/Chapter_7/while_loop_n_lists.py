#Alfred Gachanja
#14-03-2023
#In this program I learn how to work with while loops,
# and lists.

#Moving one item from one list to another.

#Start with a list of users that need to be verified.
#Then an empty list that holds confirmed users.
unconfirmed_users = ['john', 'david', 'alice', 'kelvin', 'antony']
confirmed_users = []

#Verify each user until there is no more unconfirmed users.
# Then move them into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: {}" .format(current_user.title()))
    confirmed_users.append(current_user)

#Display all the confirmed users.
print("\nThe following are the confirmed users.")
for confirmed_user in confirmed_users:
    print("\t{}" .format(confirmed_user.title()))
