"""
map function
map(function,iterable)
"""

student1 = [("maths", "Anitha", 90), ("biology", "Anand", 80), ("biology", "Balaji", 50), ("maths", "Doo", 75)]
inr_usd = lambda item: (item[0], item[1], "{:.2f}".format(item[2] / 78))
inr_usd2 = lambda item: (item[1], "{:.2f}".format(item[2] / 78))
usd_list = list(map(inr_usd, student1))
usd_list2 = list(map(inr_usd2, student1))
print(usd_list)
print(usd_list2)

val = [2, 3, 4, 5, 6, 74, 3]
val_sq = list(map(lambda x: x * x, val))
print(val_sq)


def sq(num):
    return num * num


val_sq1 = list(map(sq, val))
print(val_sq1)

stud = [("maths", "Anitha", 90), ("biology", "Anand", 80), ("biology", "Balaji", 50), ("maths", "Doo", 75)]
name_mark100 = lambda x: (x[1], (x[2] * 100) / 200)
fin_list = list(map(name_mark100, stud))
print(fin_list)

val = [72, 78, 99, 12, 56]
find_even = list(map(lambda x: "even" if x % 2 == 0 else "odd", val))
print(find_even)

temp = [102, 99, 89, 70, 103]
f_to_c = list(map(lambda f: (f - 32) * (5 / 9), temp))
print(f_to_c)

"""
Filter(function,iterable)
"""

items = [(390, "shoe", 890), (346, "bat", 700), (347, "phone", 300)]
less_than_500 = lambda item: item[2] < 500
filter_500 = list(filter(less_than_500, items))
print(filter_500)

filter_p = list(filter(lambda item: item[1][0] == 's', items))
print(filter_p)

btw_3k_4k = list(filter(lambda item: 500 < item[2] < 900, items))
print(btw_3k_4k)

g_stud = [("maths", "Anitha", 90), ("biology", "Anand", 80), ("biology", "Balaji", 50), ("maths", "Doo", 75)]
stu_A_start_mark_gre_80 = list(filter(lambda s: s[1][0] == 'A' and s[2] > 80, g_stud))
print(stu_A_start_mark_gre_80)

"""
reduce(function,iterable)
performs function on first two elements and repeats it until one value remains.
"""
from functools import reduce

val = [72, 78, 99, 12, 56]
fin_acc = reduce(lambda x, y: x + y, val)
print(fin_acc)
