# Loop Repeats a set of code

letter = ' '

# while not letter.isalpha():
#     letter = input("Enter only Alphabet")
#
# print("Alphabet is " + letter)

i = 0
while i >= 100:
    print(i)
    i += 1

# range( start place, stop place , step --> This is by default 1)
# We can also use else in for loop
for i in range(1, 100, 2):
    print(i)
else:
    print("Over")

# prints list range from 1 to 10
print(list(range(1, 11)))

print(list(range(11, -11, -1)))

# looping list with for
listss = [2, 3, 4, 5, 7, 85, 132]

for i in list:
    print(i)
