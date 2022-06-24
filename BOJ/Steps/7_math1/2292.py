n = int(input())
layer_number = 1
max_in_layer = 1

while True:
    if n <= max_in_layer:
        break
    layer_number += 1
    max_in_layer += (layer_number-1)*6
print(layer_number)
