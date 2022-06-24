x = int(input())
layer = 1
number_of_fractions = 1

while True:
    if x <= number_of_fractions:
        break
    layer += 1
    number_of_fractions += layer
  
if layer % 2 == 0:
  print("{0}/{1}".format(layer-number_of_fractions+x,number_of_fractions-x+1))
else:
  print("{1}/{0}".format(layer-number_of_fractions+x,number_of_fractions-x+1))
