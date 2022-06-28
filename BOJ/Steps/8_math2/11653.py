# 기본적으로 오래 걸리는 방식이기는 하나,
# 소인수 분해에 더 이상 좋은 방법은 없는 듯하다

# BOJ에서 채점 우선순위가 2로 설정되어 있어서 더욱 느리게 채점된다

n = int(input())
i = 2

while i <= n:
    if n % i == 0:
        n = n // i
        print(i)
    if n % i == 0:
        continue
    else:
        i += 1
