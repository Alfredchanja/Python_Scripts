"""
Alfred Gachanja
29-08-2023
In this pragram I am going to practice what I learned about testing my code.
 The function in this code accepts two parameters.
"""

def City(city, country, population=''):
    cityname = city
    countryname = country
    populas = population
    if populas:
        location = cityname.title() + ', ' + countryname.title() + ' - population ' + populas
    else:
        location = cityname.title() + ', ' + countryname.title()

    return location