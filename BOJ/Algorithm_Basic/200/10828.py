import sys

def control(stack, command):
    command = command.split()
    if "push" == command[0]:
        stack.append(int(command[1]))
        return
    if "pop" == command[0]:
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
        return
    if "size" == command[0]:
        print(len(stack))
        return
    if "empty" == command[0]:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
        return
    if "top" == command[0]:
        if len(stack) != 0:
            print(stack[len(stack)-1])
        else:
            print(-1)

n = int(input())

stack = []
for i in range(n):
    control(stack, sys.stdin.readline())
