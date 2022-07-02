# 두번째 시도 
# 다른 사람들의 답안을 참고하여 다시 풀었다

def hanoi(n):
    if n == 1:
        return 1
    return hanoi(n-1) + 1 + hanoi(n-1)

# 시작 지점과 중간 지점, 목표 지점을 각각 a, b, c라는 변수로 입력받으면
# n개의 원반을 1에서 3으로 옮기는 방법이
# n-1개의 원반을 1에서 2로 옮긴 후, 
# 1개의 원반을 1에서 3으로 옮기고
# 다시 n-1개의 원반을 2에서 3으로 옮기는 과정으로 재귀적으로 표현된다

def hanoi_order(a, b, c, n):
    if n == 0:
      return
    hanoi_order(a, c, b, n-1)
    print(a, c)
    hanoi_order(b, a, c, n-1)
    
n = int(input())
print(hanoi(n))
hanoi_order(1, 2, 3, n)

# 아래는 첫번째 시도에서 작성한 알고리즘이다
# 바로 출력하는 대신 리스트를 만들고 이 값을 수정하는 방식이라 다소 복잡하다

# def hanoi(n):
#     if n == 1:
#         return 1
#     return hanoi(n-1) + 1 + hanoi(n-1)

# def hanoi_order(n):
#     if n == 1:
#         return ['1', '3']
#     previous_hanoi = hanoi_order(n-1)
#     hanoi_first = []
#     for i in previous_hanoi:
#         if i == '2':
#             hanoi_first.append('3')
#         elif i == '3':
#             hanoi_first.append('2')
#         else:
#             hanoi_first.append(i)
#     hanoi_second = []
#     for i in previous_hanoi:
#         if i == '1':
#             hanoi_second.append('2')
#         elif i == '2':
#             hanoi_second.append('1')
#         else:
#             hanoi_second.append(i)
#     return hanoi_first + ['1', '3'] + hanoi_second 
  
# n = int(input())
# print(hanoi(n))

# result = hanoi_order(n)
# for i in range(0,len(result),2):
#     print(result[i], result[i+1])
    
    
