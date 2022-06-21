dialpad = dict(zip(['A', 'B', 'C', 'D', 'E', 'F',
          'G', 'H', 'I', 'J', 'K', 'L',
          'M', 'N', 'O', 'P', 'Q', 'R', 'S',
          'T', 'U', 'V', 'W', 'X','Y', 'Z'],
         [2, 2, 2, 3, 3, 3,
          4, 4, 4, 5, 5, 5,
          6, 6, 6, 7, 7, 7, 7,
          8, 8, 8, 9, 9, 9, 9]))

word = input()
time = 0
for letter in word:
    time += dialpad[letter] + 1
print(time)
