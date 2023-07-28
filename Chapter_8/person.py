#Alfred Gachanja
#19-07-2023
#In this program I learn how to return dictionaries from functions.

def build_person(first_name, last_name, middle_name='', age=''):
    """Return a dictionary of information about a person."""
    person = {
        'firstname': first_name,
        'lastname': last_name,
        'middlename': middle_name
        }
    if age:
        person['age'] = age
    return person

guy = build_person('alfred', 'mwangi', 'gachanja', age=21)
print(guy)

#Using functions with while loops
while True:
    print("\nPlease tell me your name:")
    print("Enter 'q' to quit at anytime\n")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    m_name = input("Middle name: ")
    if m_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    yr_age = input("How old are you: ")
    if yr_age == 'q':
        break
    yr_age = int(yr_age)

    persons_info = build_person(f_name, l_name, m_name, yr_age)
    print(persons_info)