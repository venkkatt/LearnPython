items = [(390, "shoe", 890), (346, "bat", 10000), (347, "phone", 890)]

# Permanent sorting
items.sort(reverse=True)
print(items)

# Temporary sorting
print(sorted(items))

# to sort with some key in tuple
items.sort(key=lambda item: item[1])
print(items)

# to sort in descending order
items.sort(key=lambda item: item[2], reverse=True)
print(items)

# Assignment
students = [("maths", "Anitha", 90), ("biology", "Anand", 80), ("biology", "Balaji", 50), ("maths", "Doo", 75)]

students.sort(key=lambda m: m[2])
print(students)

# Assignment
# Tuples are immutable and hence permanent sorting is not possible
# using sorted method for temporary sorting.
student1 = (("maths", "Anitha", 90), ("biology", "Anand", 80), ("biology", "Balaji", 50), ("maths", "Doo", 75))

sortedstud1 = sorted(student1, key=lambda c: c[2],reverse= False)
print(sortedstud1)
