n, m = map(int, input().split())
# 주어진 board 형태를 입력받는다(2D 배열)
board = []
for i in range(n):
    board.append(list(input()))

# "정답"이라 할 수 있는 8 x 8 보드를 2D 배열로 아래와 같이 만든다
# 좌상단 칸이 흑색인 경우만 만들어도 결과적으로는 충분하다
correct_b = []
for i in range(0, 8):
    correct_b.append(['B', 'W']*4)
    correct_b.append(['W', 'B']*4)

# 전체 보드에서 시작점의 위치를 결정한 뒤에,
# 그 시작점에서 출발하여 오른쪽으로 8개, 아래로 8개까지 있는 8 x 8 보드를 체크한다
total_wrong = 64
for i in range(0, n-7):
    for j in range(0, m-7):
        b_wrong = 0
        w_wrong = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
              # "정답" 보드와 다르면 고쳐야 하는 칸(즉 wrong칸)을 하나 증가시킨다
              # 만약 좌상단이 흑색인 보드와 다르다면, 좌상단이 백색인 보드와는 같을 수밖에 없으므로
              # 좌상단이 백색인 정답을 새롭게 비교할 필요 없이 아래와 같이 else로 처리해도 충분하다
                if board[k][l] != correct_b[k-i][l-j]:
                    b_wrong += 1
                else:
                    w_wrong += 1
          # 이 중 더 적게 틀린 경우를 고른다          
        if b_wrong <= w_wrong:
            wrong = b_wrong
        else:
            wrong = w_wrong
          # 특정 시작점의 값을 wrong으로 가지고 있는데,
          # 이를 total_wrong과 비교하여 더 작으면 total_wrong에 저장함으로써 최소값을 찾는다
        if wrong < total_wrong:
            total_wrong = wrong

print(total_wrong)
