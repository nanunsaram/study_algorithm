n = int(input())

numbers = list(map(int, input().split()))
for number in numbers:
    if number == 1:
        n -= 1
        continue
    for i in range(2, number):
        if number % i == 0:
            n -= 1
            break
print(n)        
