a, b = map(list, input().split())
a.reverse()
b.reverse()

if len(a) > len(b):
    a, b = b, a

a = a + ['0']*(len(b)-len(a))
sum = []
carry = 0

for i in range(len(b)):
    sum_digits = int(a[i]) + int(b[i]) + carry
    if sum_digits >= 10:
        sum.append(str(sum_digits % 10))
        carry = 1
        if i == len(a)-1:
            sum.append(str(1))
    else:
        sum.append(str(sum_digits))
        carry = 0

sum.reverse()
sum = ''.join(sum)
print(int(sum))
