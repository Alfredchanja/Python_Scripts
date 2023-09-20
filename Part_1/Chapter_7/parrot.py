#Alfred Gachanja
#12-07-2023
#This is a more interactive program than all the rest.
#It ask the user for some information using the input() function and uses the information provided.

prompt = "Tell me anything and I will repeat it to you:"
prompt += "\nEnter 'quit' if you want me to stop. "

#This is called a flag and it is used where a lot of conditions for the program should be defined.
active = True

while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)