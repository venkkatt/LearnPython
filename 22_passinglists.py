# reference the variables. values not copied to new variable.
# instead using the same address is referred to the variable.


def print_list_copy(lists):
    for i in range(len(lists)):
        lists[i] = lists[i].title() + '#'


names = ["test", "test1", "test2"]
print(names)  # ['test', 'test1', 'test2']
print_list_copy(names)
print(names)  # ['Test#', 'Test1#', 'Test2#']


# copy the list values to new address location
def print_list(lists):
    for i in range(len(lists)):
        lists[i] = lists[i].title() + '#'


names1 = ["test", "test1", "test2"]
print(names1)  # ['test', 'test1', 'test2']
print_list(names1[:])
print(names1)  # ['test', 'test1', 'test2']
