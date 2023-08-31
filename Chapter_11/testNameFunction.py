import unittest
from nameFunction import get_formatted_name

class NameTestCase(unittest.TestCase):
    #Test for nameFunction.py
    def test_first_last_name(self):
        formattedName = get_formatted_name('janis','joplin')
        self.assertEqual(formattedName, 'Janis Joplin')

    def test_first_last_middle_name(self):
        formattedName = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formattedName, 'Wolfgang Amadeus Mozart')

unittest.main()