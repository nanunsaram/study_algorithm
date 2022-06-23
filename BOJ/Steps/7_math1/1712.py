a, b, c = map(int, input().split())

if b >= c:
    print(-1)
else:
    breakeven = a // (c-b)
    print(breakeven+1)    
