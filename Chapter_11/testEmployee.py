"""
Alfred Gachanja
31-08-2023
In this program I am testing the Employee class module.
"""

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.firstName = 'Alfred'
        self.lastName = 'Mwangi'
        self.annualSalary = 24000
        self.salaryRaise = 10000
        self.employeeRaise = Employee(self.firstName, self.lastName,
                                      self.annualSalary, self.salaryRaise)

    def test_give_default_raise(self):
        self.employeeRaise = Employee(self.firstName, self.lastName,
                                      self.annualSalary)
        self.employeeRaise.give_raise()

    def test_give_custom_raise(self):
        self.employeeRaise.give_raise()

unittest.main()