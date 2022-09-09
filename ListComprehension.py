sq_list = list(map(lambda c: c * c, range(1, 11)))
print(sq_list)

"""
List Comprehension
list [expression for item in iterable]
"""

sql_list = [x * x for x in range(1, 11)]
print(sql_list)

temp = [23, 30, 38, 22, 31, 47, 19]
temp_gre_30 = [t for t in temp if t > 30]
print(temp_gre_30)

# if else in list comprehension
temp_gre_30_else = [t if t > 30 else 0 for t in temp]
print(temp_gre_30_else)