# d(n) 함수 정의
def d(n):
    """
    d(n)을 계산하는 함수입니다.
    """
    numbers_string = list(str(n)) #각 자리 숫자를 문자열로 변환하여 list에 저장
    return n + sum(map(int, numbers_string)) #이 값을 다시 정수형으로 변환하여 합산

d_results = set() #d()의 결과값들이 담길 빈 세트 생성

for i in range(1, 10000):
    d_results.add(d(i)) #1부터 9999까지 수 i에 대해 d(i)를 계산하여 세트에 추가(중복되는 것은 추가되지 않음)

for i in range(1, 10000):
    if i not in d_results:
        print(i) #위 세트에 없을 경우 셀프넘버이므로 출력
