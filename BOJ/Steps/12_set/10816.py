import sys

N = int(input())
hands = list(map(int, sys.stdin.readline().split()))

hands_count = {}
for hand in hands:
    if hand in hands_count:
        hands_count[hand] += 1
    else:
        hands_count[hand] = 1

M = int(input())
query = list(map(int, sys.stdin.readline().split()))

# I did some 'unexpected' experiments while trying to solve this problem
# Timeout displays if I use
#     if each_query in hands:
# instead of
#     if each_query in hands_count:
# It is meaningless to check the original list if we already have (supposedly) more concise dictionary
# For huge amounts of data, it could be critical

for each_query in query:
    if each_query in hands_count:
        print(hands_count[each_query], end=' ')
    else:
        print(0, end=' ')
print()
