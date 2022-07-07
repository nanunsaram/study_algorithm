import sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
    sentence = list(map(list, input().split()))
    for i in range(len(sentence)):
        sentence[i].reverse()
        print(''.join(sentence[i]), end=' ')
    print()
