'''
*****
****
***
**
*
'''
# n=6
# for row in range(0, n):
#     for col in range(0, n-1-row):
#         print("*", end='')
#     print('')
# n = 5
# for row in range(n):
#     print("*" * (n - row))

'''
*
**
***
****
*****
'''
# n=6
# for row in range(0, n):
#     for col in range(0, row):
#         print("*", end='')
#     print('')

# for row in range(0, 6):
#     print("*"*row)


'''
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
'''

# n = 6
# for row in range(0, n):
#     for empty in range(0, n - row):
#         print(end=' ')
#     for star in range(0, row):
#         print("*", end='')
#     print(" ")


# n1 = 5
# i = 0
# while i <= n1:
#     print(" " * (n1 - i) + "*" * i)
#     i += 1

'''
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
'''
n= 5
for i in range(0, n):
    print(" " * (n-i-3) + "*" * (i+1) + " " * (n-i-3))

