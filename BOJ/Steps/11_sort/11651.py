import sys

n = int(input())
coord = []

for i in range(n):
    coord.append(list(map(int, sys.stdin.readline().split())))

coord.sort(key = lambda x: (x[1], x[0]))

for i in range(n): print(coord[i][0], coord[i][1])
