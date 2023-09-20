"""
Alfred Gachanja
19-07-2023
In this program I practice what I learned about functions and return values.
"""

def city_country(city, country):
    locations = ('"{}, {}"' .format(city.title(), country.title()))
    return locations

place = city_country('nairobi', 'kenya')
print(place)

place = city_country('kampla', 'uganda')
print(place)