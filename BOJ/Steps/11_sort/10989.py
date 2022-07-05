# Counting Sort
import sys

n = int(input())
# We know that the numbers are less then or equal to 10000
# Why 10000 + 1? Because of zero-based numbering, it is convenient to put one more place of 0(although there will be no 0 given in this problem)
count_list = [0]*10001

for i in range(n):
    count_list[int(sys.stdin.readline())] += 1

for i in range(1, 10001):
    while count_list[i] != 0:
        print(i)
        count_list[i] -= 1  
