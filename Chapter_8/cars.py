"""
Alfred Gachanja
28-07-2023
In this program I build a profile for a car.
with an arbitrary argument.
"""

def build_car(manufacture, model_name, **car_info):
    profile = {}
    profile['car manufacture'] = manufacture
    profile['car model'] = model_name
    for key, value in car_info.items():
        profile[key] = value
    return profile

car_profile = build_car('subaru', 'outback',
                        colour='black',
                        speed=205)

print(car_profile)