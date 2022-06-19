def hansoo(n):
    numbers = list(str(n)) # 주어진 수의 각 자리 수를 문자열로 바꾼 뒤 list형태로 저장
    if len(numbers) <= 2:
        return True # 한 자리 수, 두 자리 수는 모두 한수이므로 True 반환
    else: # 이외에는 입력 조건 상 세 자리 수나 네 자리 수가 주어질 수 있다
        distance_0 = int(numbers[0]) - int(numbers[1]) # 첫 두 개 숫자의 차이
        for i in range(1, len(numbers)-1):
            if (int(numbers[i]) - int(numbers[i+1])) != distance_0:
                return False # 이후 두 개의 숫자의 차이를 계산하여 distance_0과 다르면 바로 False를 반환
        return True

n = int(input())
count = 0
for i in range(1,n+1):
    if hansoo(i) == True:
        count += 1
print(count)
