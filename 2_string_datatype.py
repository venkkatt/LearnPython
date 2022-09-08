message = "hello son's"

name = '"Rakshan"'

print(message)
print(name)
string_concat = message + name
# inbuilt method , performs a specified task

# Upper , lower and title case
print(name.upper())
print(name.lower())
print(name.title())

# sting concatenation
print(message + " " + name)
print(string_concat)

# next line
print("hello \n test")

# create a tab space
print("hello \t test")

# to find the length of the string
print(len(message))

# find the index of the character first occurrence
# if not found it will return -1
print(message.find("e"))

# to find the no of occurrence of the letter.
print(message.count("l"))

# to replace a char with another character
print(message.replace('h', 'l'))

# to check if the all the character is alphabet, it contains space.
print(message.isalpha())

# to check if this is digit or not
print(message.isdigit())

# to print multiple times
print(message * 10)
