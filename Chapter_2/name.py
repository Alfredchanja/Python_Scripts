#Alfred Gachanja
#20-06-2023
#This program prints a statement contained in a string.
#In this program I learned how to manipulate string variables.

#Changing case in strings using methods
#Changes the case of the first words of the string variable to uppercase.
print("Cases")
name = "alfred gachanja"
print("\n" + name.title())

#Changes the case of the string to uppercase and lowercase respectively.
name = "Alfred Gachanja"
print(name.upper())
print(name.lower())

#Combining or Concatenating strings
print("\nConcatenation")
first_name = "alfred"
second_name = "gachanja"
last_name = "mwangi"
full_name = first_name + " " + second_name + " " + last_name
message = "Hello, " + full_name.title() + "!"
print("\n" + full_name)
print(full_name.title())
print(full_name.upper())
print(full_name.lower())
print(message)

#Adding whitespace to strings with Tabs and Newlines
print("\nWhitespaces\n")
print("\tpython")
print("Languages:\npython\nC\nJavascript")
print("Languages:\n\tpython\n\tC\n\tJavascript")

#Stripping Whitespace
print("\nStripping whitespaces\n")

favourite_language = " python "
print(favourite_language)
print(favourite_language.rstrip())
print(favourite_language.lstrip())
print(favourite_language.strip())

#Try it yourself - this me practicing what I have learned.
print("\nPRACTICE\n")

famous_person = "carl jung"
print("Hello " + famous_person.title() + ", you are my favourite psychotherapist.\n")

print(famous_person.title())
print(famous_person.upper())
print(famous_person.lower())

print('\n{}once said, "Unless the unconscious is made conscious,\
 it will control the life and you will call it fate."\n' .format(famous_person.title()))

quote = ' once said "Unless the unconscious is made conscious,\
 it will control the life and you will call it fate."\n'

print(famous_person.title() + quote)