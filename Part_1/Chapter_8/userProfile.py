"""
Alfred Gachanja
28-07-2023
In this program I learn how to use arbitrary keyword arguments
"""

def build_profile(first, last, **userinfo):
    #Build a dictionary that contains everything you know about the user.
    profile = {}
    profile ['first_name'] = first
    profile ['last_name'] = last
    for key, value in userinfo.items():
        profile [key] = value
    return profile

user_profile = build_profile('alfred', 'mwangi',
                             location='nairobi',
                             occupation='student')

print(user_profile)