"""
Alfred Gachaja
25-07-2023
In this program I learn how to modify lists in functions.
"""

def print_models(unprinted_designs, completed_models):
    #First you simulated the printing of each models
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print("Current printing model: {}" .format(current_design))
        #Then you move the already printed design to the another list.
        #The complete_models list
        completed_models.append(current_design)

def show_printed_model(completed_models):
    print("\nThe are the models that are already printed:\n")
    for completed_model in completed_models:
        print("\t{}" .format(completed_model))

unprinted_designs = ['phone case', 'decohedron', 'building']
completed_models = []

#The slice notation[:] makes a copy of the above list and sends it to the function.
print_models(unprinted_designs[:], completed_models)
show_printed_model(completed_models)
