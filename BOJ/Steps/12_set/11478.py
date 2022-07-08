import sys
input = sys.stdin.readline

S = input().strip()
substrings = set()

for i in range(len(S)):
    for j in range(len(S)-i):
        substrings.add(S[i:i+j+1])

print(len(substrings))
