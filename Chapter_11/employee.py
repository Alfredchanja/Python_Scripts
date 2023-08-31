"""
Alfred Gachanja
31-08-2023
In this program I am writing a class module called Employee.
  This class module accepts acouple of information form the user
  and also raises the annual salary by default.
"""

class Employee():
    #Raise annual salary of employee by default or any named figure.

    def __init__(self, firstName, lastName, annualSalary, salaryRaise='5000'):
        self.firstName = firstName
        self.lastName = lastName
        self.annualSalary = annualSalary
        self.salaryRaise = salaryRaise

    def give_raise(self):
        givenRaise = int(self.annualSalary) + int(self.salaryRaise)
        print(givenRaise)