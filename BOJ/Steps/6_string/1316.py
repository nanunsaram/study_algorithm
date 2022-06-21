def group_checker(word):
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            continue
        elif word[i] in word[i+1:]:
            return False
    return True

N = int(input())
count = 0
for _ in range(N):
    if group_checker(input()) == True:
        count += 1
print(count)

# 원래는 아래와 같이 다소 복잡하게 구현했었다가, 다른 사람의 풀이를 보고 다시 구현했다

# def group_checker(word):
#     word_set = set(word)
#     for letter in word_set:
#         letter_index = [i for i in range(len(word)) if word[i] == letter]
#         index_difference = [letter_index[i+1] - letter_index[i] for i in range(len(letter_index)-1)]
#         for i in range(len(index_difference)):
#             if index_difference[i] == 1:
#                 continue
#             else:
#                 return False
#     return True

# N = int(input())
# count = 0
# for _ in range(N):
#     if group_checker(input()) == True:
#         count += 1
# print(count)
