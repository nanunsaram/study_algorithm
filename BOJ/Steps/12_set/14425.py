import sys

n, m = map(int, input().split())

word_set = set()
for i in range(n):
    word_set.add(sys.stdin.readline().rstrip())

how_many = 0
for i in range(m):
    word = sys.stdin.readline().rstrip()
    if word in word_set:
        how_many += 1
print(how_many)
