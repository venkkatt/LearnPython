name = input("what is your name")
print("My name is " + name)

# Always inputs from user will be in string. We have to typecast
height = float(input("please enter your height"))

print("your height is " + str(height / 2.54) + " inches")

height_inches = "{:.2f}".format(height / 2.54)
print("inches " + height_inches)

# Assignment
name, email, phone_no = input("enter name"),\
                        input("enter email"),\
                        input("enter phone no")
print("***********************************************")
print("UserName : " + name)
print("Email : " + email)
print("Phone No : " + phone_no)
print("***********************************************")
