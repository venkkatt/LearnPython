name = 'hari'
like1 = 'apples'
like2 = 'bananas'
text = '{} likes {} and {}'.format(name, like2, like1)
print(text)  # hari likes bananas and apples
print('{1} likes {0} and {2}'.format(name, like2, like1))
# bananas likes hari and apples
# changed the output based on 0,1,2

text1 = '{name} likes {fruit1} and {fruit1}'
print(text1.format(name="venkatesh", fruit1='apple', fruit2='guva'))
print(text1.format(name="venkatesh", fruit1='orange', fruit2='grapes'))

# padding
print("***************{msg:10}**********".format(msg='venkat'))

# Left align
print("***************{msg:<10}**********".format(msg='venkat'))
# ***************venkat    **********

# Right align
print("***************{msg:>10}**********".format(msg='venkat'))
# ***************    venkat**********

# Center align
print("***************{msg:^10}**********".format(msg='venkat'))
# ***************  venkat  **********

# formatting numbers
pi = 3.1425
print("Value of pi is {}".format(pi))  # 3.1425
print("Value of pi is {:.2f}".format(pi))  # 3.14

val1 = 10000000000
print("value is {:,}".format(val1))  # 10,000,000,000

num1 = 101
print("binary format {:b}".format(num1))  # 1100101
print("ocatal format {:o}".format(num1))  # 145
print("hexa format {:x}".format(num1))  # 65
print("e format {:e}".format(num1))  # 1.010000e+02

'''
b - binary
o - octal
x - hexa
e - scientific notation
'''
