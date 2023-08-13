"""
Alfred Gachanja
02-08-2023
In this progam I practice what a I have learned so far about classes.
"""

class User():
    def __init__(self, first_name, last_name, second_name,
                 user_name, age, email_address):
        self.first_name  = first_name
        self.last_name = last_name
        self.second_name = second_name
        self.user_name = user_name
        self.age = age
        self.email_adress = email_address
        self.login_attempts = 0

    def describe_user(self):
        print("First name: {}" .format(self.first_name.title()))
        print("Second name: {}" .format(self.second_name.title()))
        print("Last name: {}" .format(self.last_name.title()))
        print("Age: {}" .format(str(self.age)))
        print("User name: {}" .format(self.user_name))
        print("email adress: {}" .format(self.email_adress))

    def greet_user(self):
        print("\nHello {}!" .format(self.user_name))

    def increment_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        if self.login_attempts > 3:
            self.login_attempts = 0
            print("We are resetting your login. Please try again in 30 secs.")
        else:
            print("You are logged in.")

user_0 = User('alfred', 'mwangi', 'gachanja', 'Alpppphhhyyy', '21', 'alfredgachanja8@gmail.com')
user_0.describe_user()
user_0.greet_user()

#Setting an instance to chack whether the increment_attempt method works.
#Line 48 prints the number of login attempts.
user_0.increment_attempts()
user_0.increment_attempts()
user_0.increment_attempts()
print(user_0.login_attempts)

#Setting an instance to check whether the reset_login_attempt  method works with its conditio
#The first condition and the socond work perfectly lines 52 and 54 confirms.
user_0.reset_login_attempts()

user_0.increment_attempts()
print(user_0.login_attempts)

user_0.reset_login_attempts()
print(user_0.login_attempts)#Confirms whether the login attempt has been reset.

class Priviledge():
    def __init__(self, priviledges= ['can add post', 'can delete post',
                        'can remove user', 'can add user']):
        self.priviledges = priviledges
       
    def show_priviledges(self):
        print("\nThe admin can do the following:")
        for priviledge in self.priviledges:
            print("\t{}" .format(priviledge))

class Admin(User):
    def __init__(self, first_name, last_name, second_name, user_name, age, email_address):
        super().__init__(first_name, last_name, second_name, user_name, age, email_address)
        self.superAdmin = Priviledge()

    
user_admin = Admin('alfred', 'mwangi', 'gachanja', 'Alpppphhhyyy', 21, 'alfredgachanja8@gmail.com')
user_admin.superAdmin.show_priviledges()