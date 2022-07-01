T = int(input())

# 매번 소수인지를 체크하기보다는 에라토스테네스의 체를 이용해 미리 소수 리스트를 뽑아 놓는다
for _ in range(T):
    n = int(input())
    total_list = [False]*2 + [True]*(n-1)
    for i in range(0, n+1):
        if total_list[i] == False:
            continue
        else:
            for j in range(2*i, n+1, i):
                total_list[j] = False
# n//2 부터 시작해서 1씩 줄여가면서 더해서 n이 되는 소수의 쌍인지 체크한다                
    for i in range(n//2, 1, -1):
        if total_list[i] == True and total_list[n-i] == True:
            print(i, n-i, sep=' ')
            break
