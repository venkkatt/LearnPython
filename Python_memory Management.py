a = 10
b = 11
c = 10
print(id(a) == id(c))  # true #address of this will be same
print(id(a) == id(c))  # false #address different

# next when value changed
print(id(a) == id(b))  # true # this will be same

# reference count based garbage collector
"""
value of variables stored in heap
address of the value stored in the stack
when a=10 is pointing to the address of variables in heap
When compiler finds another variable with same a=10 it will point to the same variable.
when the variable is not in use reference count based garbage collector will clear the space.

"""
