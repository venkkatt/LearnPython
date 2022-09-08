"""
Access specifiers are by convention and python will not restrict
like other language. All the below are by convention

private (__with_double_underscore)
--> This should access only within the class.
--> This is also called Dunder variables, methods
 ==> __variable
 ==> def __register(self):

Protected (_with_single_underscore)
--> This should be accessed within the class and also from the
    derived class
 ==> _variable
 ==> def _register(self):

 __variables__ --> Pythons internal variable.
"""


class User:
    users = 0

    def __init__(self, user_name, pwd):
        self.user_name = user_name  # instance variable
        self.pwd = pwd
        User.users += 1

    def register(self):
        print("Registered ")

    def loging(self):
        print("Logging in ")
        return self

    def greet(self):
        print("Hi User..")


# Inheritance
class Student(User):
    def __init__(self, username, pwd, course, fee):
        # Super function. Instead of initializing the user_name and pwd here,
        # without duplicating. we can pass this to the parent class to
        # initialize this user_name and pwd data.
        super().__init__(username, pwd)
        self.course = course
        self.fee = fee

    def greet_student(self):
        print("Hi Student")

    def greet(self):  # Override
        super().greet()
        print("Hi Student " + self.user_name)


class Faculty(User):
    def greet_faculty(self):
        print("Hi Faculty")

    def greet(self):
        print("Hi Faculty")


# Multi level inheritance
# User --> Faculty --> TempFaculty
# Inherited in multi level.
class TempFaculty(Faculty):
    def greet_tempFaculty(self):
        print("Hi Temp Faculty")

    # def greet(self):
    #     print("Hi Temp Faculty")


'''             |--------->Temp Faculty
    User--> Faculty----|
        |              |-->StudentFaculty
        |--> Student---|
        
Super() function is used to call parent class methods and initialize
the variables

In StudentFaculty class it is derived from both Faculty and Student Class
even if we use super() function in StudentFaculty class, it will not know
which parent class to call.

In python first 
1 --> it will call Student class greet() method if not
2 --> then it will call Faculty class greet() method if not available
3 --> then it will call User class greet() mtehod
'''


# Multiple Inheritance
# Try to avoid Multiple inheritance.
# StudentFaculty --> Student, Faculty
class StudentFaculty(Student, Faculty):
    def greet(self):
        super().greet()
        print("Hello Student Faculty")
