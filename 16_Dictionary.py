# Key value pair

user = {'name': 'Ram', 'age': '23', 'gender': 'male'}
# Fetching individual item
print(user['gender'])  # male

print(user)  # {'name': 'Ram', 'age': '23', 'gender': 'male'}

# Adding new value to the dictionary
user['city'] = 'Madurai'

print(user)  # {'name': 'Ram', 'age': '23', 'gender': 'male', 'city': 'Madurai'}

# Changing any of the key value pair
user['name'] = 'Rakshan'
print(user)  # {'name': 'Rakshan', 'age': '23', 'gender': 'male', 'city': 'Madurai'}

# deleting one of the key/value pair
del user['gender']
print(user)  # {'name': 'Rakshan', 'age': '23', 'city': 'Madurai'}

for venk, vals in user.items():
    print("key " + venk + " val " + str(vals))

# It will not give the item in order

for key in user.keys():
    print(key, end='-')

for val in user.values():
    print(val, end='-')
print('\n***********************\n')
print(user)
# to sort the dictionary items.
for key in sorted(user.keys()):
    print(key, end=' ')  # age city name

    print(user[key], end=' ')  # 23 Madurai Rakshan

# Key can not be duplicate in dictionary
job = {'venkat': 'TCS', "DOO": "DOO"}
job["venkat"] = "amaxon"

print('\n***********************\n')
# list of Dictionaries
users = []
users.append(user)
user = {'name': 'DOO', 'age': '2', 'gender': 'male'}
users.append(user)
print(users)
print(users[0])  # {'name': 'Rakshan', 'age': '23', 'city': 'Madurai'}
print(users[0]['name'])  # Rakshan

# we can do the all the things in dictionary same as like list

# we can add list of items in dictionary
user["favfood"] = ['dosa', 'biriyani', 'pongal']
print(user)  # {'name': 'DOO', 'age': '2', 'gender': 'male', 'favfood': ['dosa', 'biriyani', 'pongal']}
print(user['favfood'][0])  # dosa

# we can also add dictionary into dictionary
user["color"] = {'red': 'blued', 'pink': 'black', 'white': 'grey'}
print(
    user)  # {'name': 'DOO', 'age': '2', 'gender': 'male', 'favfood': ['dosa', 'biriyani', 'pongal'], 'color': {'red': 'blued', 'pink': 'black', 'white': 'grey'}}

people = {'name': 'ram', 'name': 'doo'}
print(people)
