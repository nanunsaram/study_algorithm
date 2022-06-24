T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    if N % H == 0:
        floor = H
        vertical_line = (N // H)
    else:
        floor = N % H
        vertical_line = (N // H) + 1
    print(floor*100+vertical_line)
