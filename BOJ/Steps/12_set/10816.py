import sys

N = int(input())

# Make a list for counting the appearance of each number in hands
# Given hands are greater than or equal to -10,000,000 and less than or equal to 10,000,000
hands = list(map(int, sys.stdin.readline().split()))
hands_cnt = [0]*(2*(10**7)+1)
for i in range(N):
    hands_cnt[hands[i] + 10**7] += 1

M = int(input())
query = list(map(int, sys.stdin.readline().split()))

# For each queried number, print the element from the list for counting
for i in range(M):
    print(hands_cnt[query[i]+10**7], end=' ')
print()
