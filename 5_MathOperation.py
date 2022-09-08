import math  # math - modules we can import and use

a = 10
b = 5
# By default, when the python executes  divided by , it will give the result in float
print(a / b)

a = 8.78
print(round(a))

# gives absolute value as 222
a = -222
print(abs(a))

# to find power
a = 2
print(pow(a, 3))
print(a ** 3)  # alternate method for pow()

a, b, c, d, e, f, g = 100, 234, 3443, 23982, 34, 21, 32
print(max(a, b, c, d, e, f, g))
print(min(a, b, c, d, e, f, g))

c = 4.56
print(math.ceil(c))
print(math.floor(c))
print(math.factorial(3))
print(math.gcd(4, 2, 6))
print(math.isclose(2, 5, abs_tol=3))

# gives remainder
print(4 % 2)

# Assignment

number = int(input("Please enter a no"))
print("log2(n) is : " + str(math.log2(number)))
print("Cos(n) is : " + str(math.cos(number)))
print("e(n) is : " + str(math.exp(number)))
