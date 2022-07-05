import sys

n = int(input())
numbers = []

for i in range(n):
    numbers.append(int(sys.stdin.readline()))

# mean
mean = round(sum(numbers)/n)

# median
numbers.sort()
median = numbers[(n//2)]

# mode
count = [0]*8001

for i in range(n):
    if numbers[i] > 0:
        count[numbers[i] + 4000] += 1
    else:
        count[4000 + numbers[i]] += 1

max_count = max(count)
if count.count(max_count) == 1:
    mode = count.index(max_count) - 4000
else:
    mode_list = [i for i in range(8001) if count[i] == max_count]
    mode_list.sort()
    mode = mode_list[1] - 4000
  
# range
range_number = max(numbers) - min(numbers)

print(mean)
print(median)
print(mode)
print(range_number)
