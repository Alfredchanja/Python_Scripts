"""
Alfred Gachanja
28-07-2023
In this program I import functions from a module 
and give the module an alias.
"""
import pizza as p
#This line imports a specific function form the module 
# and give the function an alias.
from pizza import make_pizza as mp

p.make_pizza('medium', 'BBQ')
p.make_pizza('large', 'chicken', 'pineapple', 'cheese')

mp('medium', 'pepperoni')
mp('large', 'cheese', 'pepperoni', 'beef')