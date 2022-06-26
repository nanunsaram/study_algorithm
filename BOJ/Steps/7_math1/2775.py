T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    resident = list(range(1, n+1))
    for i in range(k):
      for j in range(1,n):
        resident[j] = resident[j] + resident[j-1]
    print(resident[n-1])   
    
    
# 아래와 같이 재귀함수를 쓰면 시간초과가 된다    
# def resident(k, n):
#     if k == 0:
#         return n
#     if n == 1:
#         return 1
#     return resident(k, n-1) + resident(k-1, n)

# T = int(input())
# for _ in range(T):
#     k = int(input())
#     n = int(input())
#     people = resident(k, n) 
#     print(people)    
