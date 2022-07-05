# 파이썬 삽입정렬 구현
n = int(input())

list_to_sort = []
for i in range(n):
    list_to_sort.append(int(input()))

for i in range(1, n):
  # i번째(i>=1)에 위치한 숫자를 pop()으로 뽑는다
  # pop()은 remove 기능까지 수행하기 때문에 유용하다
    key = list_to_sort.pop(i)
    for j in range(i-1, -1, -1):
      # i-1번째에서 0번째에 이르기까지 역순으로 위 key보다 작은 수가 나오는지 체크한다
      # 만약 작은 수가 나오면 key를 그 수 바로 오른쪽에 삽입한다
        if list_to_sort[j] < key:
            list_to_sort.insert(j+1, key)
            break
      # 만약 작은 수가 나오지 않았고 0번째에 이르렀다면
      # key가 제일 작은 수이므로 0번째에 삽입한다
        elif j == 0:
            list_to_sort.insert(0, key)

for i in list_to_sort: print(i)
