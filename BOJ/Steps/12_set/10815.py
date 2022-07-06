import sys

n = int(input())
cards = set()
cards.update(list(map(int, sys.stdin.readline().split())))

m = int(input())
test_cards = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    if test_cards[i] in cards:
        test_cards[i] = 1
    else:
        test_cards[i] = 0
print(*test_cards)
