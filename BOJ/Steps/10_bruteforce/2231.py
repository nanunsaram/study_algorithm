n = int(input())
list_n = list(str(n))

# 직접 분해합을 구해보면서 찾으면 되지만, 과연 1부터 n-1까지를 다 확인해야 할까?
# 어떤 생성자의 모든 자리수가 9인 경우를 생각하면, 그 생성자의 자리수 * 9를 더했을 때 그 생성자로부터 나올 수 있는 가장 큰 분해합이 된다  
# 그렇다면 분해합의 관점에서 생각해보자. k자리의 수 n이 분해합으로 주어졌을 때,
# 제일 높은 자리를 제외한 모든 자리의 숫자가 9인 경우를 생각하면, 가능한 가장 큰 각 자리 숫자의 합은 (제일 높은 자리의 숫자 -1) + 9 * (k-1)가 된다
# 그래서 해당 경우의 생성자를 minimum으로 놓고 거기서부터 n-1까지만 분해합을 확인해 보면 충분하다
minimum = n - (int(list_n[0]) - 1 + 9 * (len(list_n)-1))
yes_answer = None

for i in range(minimum, n):
    numbers = list(str(i))
    decomposition_sum = i + sum(map(int, numbers))
    if decomposition_sum == n:
        yes_answer = 1
        print(i)
        break

if yes_answer == None:
    print(0)
