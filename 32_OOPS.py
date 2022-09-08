from user import User, Student, Faculty, TempFaculty, StudentFaculty
from AbstractClass import Car, Bike, Vehicle

# user1 = User("Venkatesh", "test123")
# user2 = User("DOO", "test123")
# user3 = User("Test", "test123")
#
# user1.loging()
# user1.register()
#
# print(user1.user_name)
# print(user2.user_name)
# print(User.users)
#
# user1.users = 10  # we should avoid doing like this.
# print(user1.users)
# print(User.users)

# stud1 = Student()
# stud1.greet_student()
# stud1.loging()
#
# fac1 = Faculty()
# fac1.greet_faculty()
# fac1.register()
#
# tempfac1 = TempFaculty()
# tempfac1.greet_faculty()
# tempfac1.greet_tempFaculty()
#
# #
# studfac = StudentFaculty()
# studfac.greet_faculty()
# studfac.greet_student()

# stud = Student()
# stud.greet()

# fac = Faculty()
# fac.greet()

# Override will check if this class has greeted method , if not available
# then it will move to check the nearest greet method and print that.
# in below case greet method in tempFaculty is commented , but it fetched
# the nearest greet method in Faculty and will print "Hi Faculty"
# tempfac = TempFaculty()
# tempfac.greet()

# user = User()
# user.greet()

# user1 = User()
# user1.loging()
# user1.greet()

#  Instead of calling two separate method we can use method chaining.
#  Method Chaining
#  In loging in method we have return the  self to do the
#  Method chaining.
# user1.loging().greet()


# stud1 = Student("Ravi", "2345", "CS", 78000)
# stud1.greet()


# sf1 = StudentFaculty("doo", "abcd", "cs", 9000)
# sf1.greet()
'''
Hi Faculty
Hi Student doo
Hello Student Faculty
'''

car1 = Car().start()  # You are riding a Car...

# veh = Vehicle().start()  # Can't instantiate abstract class Vehicle with abstract method start

bike = Bike().start()  # Can't instantiate abstract class Bike with abstract method start
