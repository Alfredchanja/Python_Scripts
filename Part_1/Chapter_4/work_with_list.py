#Alfred Gachanja
#30-06-2023
#This prints a group of elements contained in a list
#In this program I am learning how to work with groups of elements in a list.

#Slicing a list.
print("Slicing a list.")
players = ['frank', 'mageto', 'samson', 'desmas', 'rayhellen', 'allan', 'collins', 'amos',]

print(players[1:3])#Prints all the items from index 1 to 2.
print(players[3:])#Prints all the items from index 3 to the end.
print(players[:3])#Prints all the items from index 0 to 2.
print(players[-3:])#Prints all the items 3 positions from the start of the list.
print(players[:-3])#Prints all the items 3 positions from the end of the list.

#Looping through a slice.
print("\nLooping through a slices list.\n")
print("Here are the major participants in this year's PCM weekend:")
for player in players[:-2]:
    print("\t" + player.title())

#Copying a list.
print("\nCopying a list.\n")
main_pms = players[:]
main_pms.append("alfred")#This is to prove that we have two seperate lists.
main_pms.sort()

print(players)
print(main_pms)
