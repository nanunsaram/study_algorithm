# https://wookcode.tistory.com/49 참고하였습니다.

# This problem is intended for stack
# It is also possible to solve by counting the parenthesis(left +1, right -1)

def VPS_checker(s):
    parenthese_stack = []
    for parenthese in s:
        if parenthese == "(":
            parenthese_stack.append(parenthese)
        else:
            if parenthese_stack:
                parenthese_stack.pop()
            else:
                print("NO")
                break
    else:
        if not parenthese_stack:
            print("YES")
        else:
            print("NO")

N = int(input())
for i in range(N):
    VPS_checker(input())
            
