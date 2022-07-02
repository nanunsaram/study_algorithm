n, m = map(int, input().split())
given_cards = list((map(int, input().split())))
given_cards.sort(reverse = True)

threecards_sum = 0
for i in range(len(given_cards)):
    for j in range(i+1, len(given_cards)):
        for k in range(j+1, len(given_cards)):
            if given_cards[i] + given_cards[j] + given_cards[k] <= m and given_cards[i] + given_cards[j] + given_cards[k] > threecards_sum:
                threecards_sum = given_cards[i] + given_cards[j] + given_cards[k]

print(threecards_sum)          
