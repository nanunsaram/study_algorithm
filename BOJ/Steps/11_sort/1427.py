n = list(str(input()))
num_list = list(map(int, n))
num_list.sort(reverse=True)
print(''.join(list(map(str, num_list))))
