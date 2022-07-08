import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A = set()
B = set()
A.update(list(input().split()))
B.update(list(input().split()))

# There are several ways to represent a symmetric difference
# As we only need to display the number of elements of a symmetric difference, it is not necessary to get the symmetric difference itself
# It suffices to get the numbers of elements of (A-B) and (B-A) respectively and add them
print(len(A-B)+len(B-A))
