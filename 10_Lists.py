# Lists

# all the string operation is applicable to lists
cities = ['Madurai', 'Trichy', 'Chennai', 'Coimbatore']
val_num = [1, 2, 3, 4, 5, 6, 7, 8]
lists1 = ['city1', 3, 4, 5, 'my city']

# accessing the value by index
print(cities[0])
print(val_num[2])
print(cities[:3])

# -1 will reverse the lists
print(cities[:-3:-1])

# accessing the list by using step
print(cities[::2])

# prints full lists
print(lists1)

# Modify city
cities[2] = "Madras"
print(cities)

# Append
cities.append("Chennai")
print(cities)

# To find the particular string occurrence count
print("Count :" + str(cities.count("Chennai")))

# Length of the cities
print("Length of list " + str(len(cities)))
print(type(cities))

if "Chennai" in cities:
    print("Chennai exist")

cities.insert(3, "Tanjore")
print(cities)

# for deleting an item in the list
del cities[3]
print(cities)

# returns deleted value
deleted = cities.pop(3)
print("deleted " + deleted)
print(cities)

# remove by value
cities.remove("Madurai")
print(cities)

# cities.remove("Madurai")

cities.append("Madurai")
cities.append("Madurai")
print(cities)

# remove will remove first occurrence  in the list
cities.remove("Madurai")
print(cities)

# temporary sort. It will not affect the values stored in the variable.
print(sorted(cities))
print(sorted(val_num))

# Permanent sort
cities.sort()
print(cities)

# Reverse cities permanently
cities.reverse()
print(cities)

# when int and string mixed sort will not work
lists1 = ['city1', 3, 4, 5, 'my city']

print(lists1.pop(0))
print(lists1.pop(3))
lists1.sort()
print(lists1)

lists1 = [3, 3, 4, 5, 2,3]
c  = lists1.count(3)

for i in range(c):
    print(i)









