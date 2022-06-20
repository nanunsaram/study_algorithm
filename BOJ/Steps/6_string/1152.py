s = str(input()).strip()
space = s.count(' ')

# 항상 예외에 유의하여야 한다. 여기서는 공백만으로 이루어진 문자열이 주어지는 경우가 있다.
if len(s) == 0:
    print(0)
else:
    print(space+1)
    
# 간단한 풀이로는 파이썬의 split()을 이용하여
# print(len(input().split())) 같은 풀이도 가능하다.
