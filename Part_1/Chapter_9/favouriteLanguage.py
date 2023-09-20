"""
Alfred Gachanja
13-08-2023
In this program I learn how to use the Python Standard Library.
"""

from collections import OrderedDict

favouriteLanguage = OrderedDict()

favouriteLanguage['jen'] = 'python'
favouriteLanguage['sarah'] = 'c'
favouriteLanguage['edward'] = 'ruby'
favouriteLanguage['phil'] = 'python'

for name, language in favouriteLanguage.items():
    print("{}'s favourite language is {}." .format(name.title(), language.title()))