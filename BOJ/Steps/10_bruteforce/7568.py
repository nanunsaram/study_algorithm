n = int(input())

body_size = []

for _ in range(n):
    body_size.append(list(map(int, input().split())))

grade_list = []
for i in range(len(body_size)):
    grade = 1
    for j in [k for k in range(len(body_size)) if k != i]:
        if (body_size[j][0] > body_size[i][0] and body_size[j][1] > body_size[i][1]):
            grade += 1
    grade_list.append(grade)

print(*grade_list, sep = ' ')
