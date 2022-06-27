N = int(input())
three_kilo_bag = 0
No_Answer = 0

while (N % 5) != 0:
    if N < 0:
        No_Answer = 1
        break
    else:
        N -= 3
        three_kilo_bag += 1
        
if No_Answer == 1:
    print(-1)
else:
    print((N // 5) + three_kilo_bag)
