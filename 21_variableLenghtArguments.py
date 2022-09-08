# * - for passing any no of parameters.
def total(*testing):
    sums =0
    for i in testing:
        sums +=i
    return sums

# below passed values are converted into tuples
print(total(3,4,5,6,78,3))

# ** - when need to pass any no of parameter with variable name
def address(**testing):
    for key, val in testing.items():
        print(val)

# below passed values are converted into dictionary
print(address(f="f",l="l",t="t",e="e"))