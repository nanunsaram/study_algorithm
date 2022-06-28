m = int(input())
n = int(input())

number_list = list(range(m, n+1))

for i in range(m, n+1):
    if i == 1:
        number_list.remove(i)
        continue
    for j in range(2, i):
        if i % j == 0:
            number_list.remove(i)    
            break

if len(number_list) == 0:
    print(-1)
else:
    print(sum(number_list))
    print(min(number_list))
