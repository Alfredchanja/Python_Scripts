"""
Alfred Gachanja
29-08-2023
This program tests the city function.
"""
import unittest
from cityFunctions import City

class CitiesTestCase(unittest.TestCase):
    #Test the naming format of cities.
    def test_city_country_name(self):
        cityformat = City('nairobi', 'kenya')
        self.assertEqual(cityformat, 'Nairobi, Kenya')
    def test_city_country_population(self):
        cityformat = City('santiago', 'chile','500000')
        self.assertEqual(cityformat, 'Santiago, Chile - population 500000')
    
unittest.main()