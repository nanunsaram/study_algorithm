# Built-in sort() function does a good job

import sys

n = int(input())
coord = []

for i in range(n):
    coord.append(list(map(int, sys.stdin.readline().split())))

# This works even without the key given by lambda function
# But it is more precise to set the key
# sort() and sorted() of Python both have 'key' parameter, which takes a function to be used as the key to sort
# Here, we used lambda function which takes keys given in a tuple.
coord.sort(key = lambda x: (x[0], x[1]))

for i in range(n):
    print(*coord[i])


# Bubble Sort is not efficient enough

# import sys

# n = int(input())
# coord = []

# for i in range(n):
#     coord.extend(map(int, sys.stdin.readline().split()))

# for i in range(2*n-2, -1, -2):
#     for j in range(0, i, 2):
#         if coord[j] > coord[j+2]:
#             coord[j], coord[j+2] = coord[j+2], coord[j]
#             coord[j+1], coord[j+3] = coord[j+3], coord[j+1]

# for i in range(2*n-2, -1, -2):
#     for j in range(1, i, 2):
#         if coord[j] > coord[j+2] and coord[j-1] == coord[j+1]:
#             coord[j-1], coord[j+1] = coord[j+1], coord[j-1]
#             coord[j], coord[j+2] = coord[j+2], coord[j]

# for i in range(0, 2*n-1, 2):
#     print(coord[i], coord[i+1])
