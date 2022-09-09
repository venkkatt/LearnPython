# Higher order functions
# takes function as parameter or return a function

def calmdown():
    print("calm down")


def happy():
    print("Jumping>>>")


def sad():
    print("Crying???")


def feeling(func):
    func()
    return calmdown

# Jumping>>> # this returns a function calm-down
# takes function as parameter. 
func = feeling(happy)
func()  # calm down
feeling(sad)  # Crying???

# print(happy)  # <function happy at 0x000001CD03CC3E20>
# # this is where the address of this function
#
# joy = happy
# print(joy) # <function happy at 0x000001E8E10E3E20>
# joy()  # Jumping>>>
#
# sorrow = sad
# sorrow()
