"""
Alfred Gachanja
29-08-2023
In this program I am learning how to test my code.
"""

def get_formatted_name(first, last, middle=''):
    #Generates a neatly formatted name.
    if middle:
        fullName = first + ' ' + middle + ' ' + last
    else:
        fullName = first + ' ' + last
    return fullName.title()