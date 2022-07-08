import sys
input = sys.stdin.readline

N, M = map(int, input().split())

never_heard = set()
never_seen = set()
for i in range(N):
    never_heard.add(input().strip())
for j in range(M):
    never_seen.add(input().strip())
dbj = never_heard.intersection(never_seen)

print(len(dbj))
print(*sorted(list(dbj)))
