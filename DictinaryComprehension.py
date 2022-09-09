"""
Dictionary Comprehension

dictionary ={key : expression for (key.value) in iterable}
"""

cart = {'phone': '20000', 'bike': '50000', 'car': '25000', 'house': '75000'}

cart_rounded = {k: round(int(v)) for (k, v) in cart.items()}
print(cart_rounded)

# if condition in dictionary comprehension
# dictionary ={key : expression for (key.value) in iterable if condition}
cart2 = {k: v for k, v in cart.items() if int(v) > 30000}
print(cart2)

# if condition in dictionary comprehension
# dictionary ={key : expression if else condition for (key.value) in iterable}

cart3 = {k: int(v) - int(v) * .1 if int(v) > 30000 else v for k, v in cart.items()}
print(cart3)


# passing function for expression Dictionary Comprehension
def veh_discount(k, v):
    if k == 'bike' or k == 'car':
        v *= .5
    return v


cart4 = {k: veh_discount(k, int(v)) for k, v in cart.items()}
print(cart4)
