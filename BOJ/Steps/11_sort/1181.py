import sys

n = int(input())
words = []

for i in range(n):
    words.append(sys.stdin.readline().rstrip())

words = list(set(words))

words.sort()
words.sort(key = len)

for i in range(len(words)): print(words[i])
