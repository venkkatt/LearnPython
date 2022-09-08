# outer loop for no of rows
# inner loop for no of columns
for j in range(1, 4):
    for i in range(1, 6):
        print(i, end='')
    print('')

s = "geeks"

# Pass statement
for i in s:
    if i == 'k':
        print('Pass executed')
        pass
    print(i)

print()

# Continue statement
for i in s:
    if i == 'k':
        print('Continue executed')
        continue
    print(i)

'''
g
e
e
Pass executed
k
s

g
e
e
Continue executed
s
'''

# instead of CONTINUE we can also use PASS.
# continue will not execute further statements, and it will move to the loop statement for next iteration
# pass will execute the further statements in the loop


str_ip = "34,5,2,8,9"
lists = []
single_str = ''
is_comma = False
for i in str_ip:
    if i == ',':
        is_comma = True
        continue
    if is_comma:
        lists.append(int(single_str))
        single_str = ''
    single_str += i
print(lists)
