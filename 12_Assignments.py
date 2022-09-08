# import math
#
# num = int(input("Please enter no"))
#
# for i in range(0, num):
#     facto_num = math.factorial(i)
#     print(facto_num)

# total_todo_list = int(input("Enter total to do list to add"))
# lists = []
# for i in range(0, total_todo_list):
#     todo = input("Enter tasks")
#     lists.append(todo)
# print("Todo list completed")
# print(lists)


# def movNeg(arr):
#     total = len(arr)
#     fin = [None] * total
#     pos = 0
#     neg = total - 1
#     for i in range(total):
#         if arr[i] >= 0:
#             fin[pos] = arr[i]
#             pos += 1
#         else:
#             fin[neg] = arr[i]
#             neg -= 1
#     print(fin)
#     fin[pos:] = fin[total-1:pos-1:-1]
#     return fin


# Driver program
arr = [1, -1, -3, 0, -2, 7, 5, 11, 6,0,-6,0,0,0]
# print(movNeg(arr))


peeklen = len(arr)
peek = [None]*peeklen
ite = 0
for i in range(peeklen):
    if arr[i] == arr[0]:
        if arr[i] > arr[i+1]:
            peek[ite] = arr[0]
            ite += 1
    elif arr[i] == arr[peeklen-1]:
        if arr[i-1] > arr[i-2]:
            peek[ite] = arr[peeklen-1]
            ite += 1
    else:
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            peek[ite] = arr[i]
            ite += 1
print([x for x in peek if x is not None])
