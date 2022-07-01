while True:
    n = int(input())
    if n == 0:
        break
    else:
        total_list = [False]*2 + [True]*(2*n - 1) 
        for i in range(0, 2*n+1):
            if total_list[i] == False:
                continue
            else:
                for j in range(2*i, 2*n+1, i):
                    total_list[j] = False
        prime_number = [i for i in range(n+1, 2*n+1) if total_list[i] == True]
        print(len(prime_number))
