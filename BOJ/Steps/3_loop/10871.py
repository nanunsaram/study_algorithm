n, x = map(int, input().split())
sequence = list(map(int, input().split()))
print(*[sequence[i] for i in range(len(sequence)) if sequence[i] < x])
