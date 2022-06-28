import math
import sys

m, n = map(int, sys.stdin.readline().split())

# 에라토스테네스의 체를 이용하기 위해 IsPrime이라는 list를 만들고
# 일단은 전부 소수라고 두고 True로 초기화한다
# 이 n개의 요소들은 자연수 1에서 n에 각각 대응된다
IsPrime = [True]*n

# i = 2부터 n의 제곱근까지, i의 배수를 소수에서 제외시켜 나간다
# n의 제곱근이 나온 이유는? 
# 약수가 갖는 대칭성 때문에 가능하다(!)
for i in range(2, int(math.sqrt(n))+1):
# i가 소수일 때
    if IsPrime[i] == True:
# i보다 큰 i의 배수들은 전부 소수가 아니므로, IsPrime값을 False로 변경
        for j in range(2*i, n, i):
            IsPrime[j] = False
# 위와 같이 바로 IsPrime[i] == True를 써도 되는 이유는?
# i가 2부터 시작해서 배수를 제외하면서 점점 커진 것이기 때문에,
# 어떤 IsPrime[i]가 True라는 것은 그보다 작은 i값들의 배수가 아니었다(즉 소수이다)는 의미이므로 그러하다

# 위 연산을 만약에 i보다 크고 n보다 작거나 같은 수를 직접 나누어 보면서
# 나머지가 0인지 확인한다면 시간초과가 된다
# 즉, 'i의 배수'의 개념을 'i로 나눈 나머지 == 0'로 하려면 모든 수를 직접 다 체크해야 하지만,
# 'i보다 크면서 i만큼씩 커지는 수'로 보면 그런 연산이 불필요하다(!)

# 우리가 원하는 m에서 n까지의 자연수에 대해서만 아래와 같이 출력할 수 있다
print(*[i for i in range(m-1, n) if IsPrime[i] == True], sep='\n')



# 이 코드는 https://this-programmer.tistory.com/409 를 참고하여 작성되었습니다. 감사합니다.
