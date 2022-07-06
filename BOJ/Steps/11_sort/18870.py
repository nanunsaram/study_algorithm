import sys

n = int(input())
coord = list(map(int, sys.stdin.readline().split()))

# get the unique values of the given coordinates and sort them in ascending order
coord_unique = sorted(list(set(coord)))
# As the list is now sorted, an element with index 'i' has 'i' smaller elements
# For example, the element with index 1(the second element of the list) has 1 smaller element
# Thus, we can match the element with its index number
coord_dict = dict(zip(coord_unique, range(len(coord_unique))))

# Using the given coordinates as keys, we can get the number of smaller elements as values
print(*[coord_dict[keys] for keys in coord])
