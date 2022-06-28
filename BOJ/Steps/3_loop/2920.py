scale = list(map(int, input().split()))
is_mixed = 0

for i in range(len(scale)-1):
    if scale[i+1] - scale[i] != 1 and scale[i+1] - scale[i] != -1:
        print("mixed")
        is_mixed = 1
        break

if is_mixed == 0:
    if scale[0] == 1:
        print("ascending")
    else:
        print("descending")
