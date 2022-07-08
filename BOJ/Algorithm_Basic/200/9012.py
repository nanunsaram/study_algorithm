def VPS_checker(s):
    parenthese_cnt = 0
    for parenthese in s:
        if parenthese == "(":
            parenthese_cnt += 1
        else:
            parenthese_cnt -= 1
            if parenthese_cnt < 0:
                break
    if parenthese_cnt == 0:
        print("YES")
    else:
        print("NO")

N = int(input())
for i in range(N):
    VPS_checker(input())
            
