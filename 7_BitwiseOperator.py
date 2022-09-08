'''
a  b a&b a|b a^b
0 0  0   0    0
0 1  0   1    1
1 0  0   1    1
1 1  1   1    0
'''

'''
1 byte = 8 bit
4 byte = 32 bits.
Since there is no defined data type in python and depends on the values
stored in the object size of the variable varies

010101010 --> each value is bit
'''
# And operator
print(3 & 4)
'''
3--> 0011
4--> 0100
-----------
     0000
'''

# Or Operator
print(3 | 4)
'''
3--> 0011
4--> 0100
-----------
     0111 --> 7
'''

# Exor Operator
print(3 ^ 4)

# Not Operator
print(~3)
'''
3--> 0000 0011 -->Not --> 1111 1100 --> Result -4
'''

print(~4)

# Most significant bit
# Least significatn bit
'''
<< --> Left shift operator 
12 --> 0000 1100 each value moves to previous place from left side
0001 1000 --> This is the result of left shift operator
12<<1 --> 24 
12<< 2--> 48

When left shift happens the values will be doubled
'''
print(234 << 1)

'''
>> --> Right shift operator 
12 --> 0000 1100 each value moves to previous place from right side
0000 0110 --> This is the result of Right shift operator
12>>1 --> 6 
12>> 2--> 3

When Right shift happens then the value will be reduced to half
'''
print(7 >> 1)
