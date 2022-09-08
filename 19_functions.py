# since python is a interpreted language. it executes the statement
# in sequence and should not call a method before the
# compiler executes the function definition

def greet(fname="test", lname="test"):
    print("hello {0} and second {1}".format(fname, lname))


# we can define default value like below when one of parameter is passed
greet("venkat")
greet('', '')

# order not matter when we use the parameter in calling method
greet(lname="kumar", fname="venkat")


# sum of n natural no till 11
def sum_nat_no(n):
    sums = 0
    for i in range(0, n):
        sums += i
    return sums

print(sum_nat_no(3))
