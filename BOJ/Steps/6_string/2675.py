def repeat(*args):
  """
  주어진 입력값을 요구된 출력값 형태로 반복하여 출력하는 함수
  """
    for i in range(len(args[1])):
        for j in range(args[0]):
            print(args[1][i], end='')
    print()
            
T = int(input())
for _ in range(T):
    number, word = input().split()
    repeat(int(number), word)
