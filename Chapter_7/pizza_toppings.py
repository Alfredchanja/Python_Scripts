#Alfred Gachanja
#12-03-2023
#In this program I practice what I learned about the 'while' loop.

prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when the toppings are enough. "

active = True

while active:
    topping = input(prompt)

    if topping == 'quit':
        active = False
    else:
        print("We will add {} to your pizza." .format(topping))