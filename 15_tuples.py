# values can be changed in list
# in tuples values can not be changed , Which means immutable

tup = (1, 2, 4)
print(tup)

# tup[1] = 9 # will throw tuple' object does not support item assignment

# can not change the individual item in the tuple like list.
# but we can change the entire tuple

tup = (4, 5, 6, 6)
print(tup)
print(tup.index(6))  # 2 position

print(tup.count(6))  # 2 occurrence

for i in tup:
    print(i, end=' ')

if 4 in tup:
    print('yes')  # yes

if 3 not in tup:
    print('Yes')  # yes

if tup:
    print("tup is not empty")  # tup is not empty

# above all the in built methods can be applied to lists as well.
# tuple also supports 2D
