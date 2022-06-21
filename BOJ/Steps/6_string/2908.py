a, b = input().split()

# 뒤에서부터 한 자리씩 비교해 나가는 방법을 쓴다면 아래와 같은 for문을 사용할 수 있다
for i in range(2, -1, -1):
    if a[i] > b[i]:
        print(a[::-1])
        break
    elif b[i] > a[i]:
        print(b[::-1])
        break
    else:
        continue

# 그러나 슬라이싱을 이용해 문자열을 뒤집어서 아래와 같이 간단하게 비교할 수도 있다        
        
# a, b = input().split()
# a = a[::-1]
# b = b[::-1]
# if a > b:
#     print(a)
# else:
#     print(b)
