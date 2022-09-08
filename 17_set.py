# set
# --> unique elements
# --> order is not saved. it will give in different order.

color = {'red', 'green', 'white', 'red'}
# it will give unique element and un ordered
print(color)  # {'red', 'white', 'green'}

# set to --> list
color_list = list(color)
print(color_list)  # ['red', 'green', 'white']

# tuple --> list
color = ('test', 'test2', 'test3')
print(list(color))  # ['test', 'test2', 'test3']

#  list to --> set
lists = [1, 2, 3, 4, 5, 6, 1, 2, 3]
print(set(lists))  # {1, 2, 3, 4, 5, 6}
# helpful when removing the duplicates and keep unique records

user = {'name': 'Ram', 'age': '23', 'gender': 'male'}
print(list(user.items()))  # ['name', 'age', 'gender'] print keys
print(set(user))  # {'name', 'age', 'gender'} print keys
print(tuple(user)) # ('name', 'age', 'gender') keys
