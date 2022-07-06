import sys

n = int(input())
info = []

for i in range(n):
    info.append(list(sys.stdin.readline().split()) + [i])

# It is initially sorted by the input order
# So only need to sort by the age(it must be 'int' type; otherwise, '120' will appear earlier than '15')
info.sort(key = lambda x: int(x[0]))

for i in range(n): print(info[i][0], info[i][1])
