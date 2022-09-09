"""
lambda means anonymous function
we can pass any no of parameters.
we can pass this to Higher order function
It is not like regular function, and it can be used in places like
when the function creation is not necessary and which requires simpler
function
"""


def add(num):
    return num + 10


print(add(20))

adds = lambda x: x + 10
print(adds(40))

product = lambda a, b, c: a * b * c
print(product(45, 23, 23))

tall_enough = lambda h: h > 175
print(tall_enough(180))

strong_enough = lambda w: "yes" if w > 70 else "no"
print(strong_enough(100))

passing_list = lambda lis: [print(x) for x in lis]

passing_list([4,5,6,7,8])


