#Alfred Gachanja
#12-07-2023
#In this progam I learn how to use the break statement to control my code execution.

prompt = "What cities would you like to visit?"
prompt += "\nEnter 'q' to stop the question. "

while True:
    city = input(prompt)

    if city == 'q':
        break
    else:
        print("\nYou would like to visit {}.\n" .format(city.title()))