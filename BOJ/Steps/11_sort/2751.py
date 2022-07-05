# Heap Sort in Python
# Reference
# https://leedakyeong.tistory.com/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%ED%9E%99-%EC%A0%95%EB%A0%AC-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0-heap-sort-in-python

# BOJ에서 Python 3로 하면 시간초과가 되고, PyPy3 로 해야 통과가 된다
import sys

def heapify(li, idx, n):
    l = idx*2
    r = idx*2 + 1
    s_idx = idx
    if (l <= n) and (li[s_idx] > li[l]):
        s_idx = l
    if (r <= n) and (li[s_idx] > li[r]):
        s_idx = r
    if s_idx != idx:
        li[s_idx], li[idx] = li[idx], li[s_idx]
        return heapify(li, s_idx, n)

def heap_sort(n, v):
    v = [0] + v

    for i in range(n, 0, -1):
        heapify(v, i, n)

    for i in range(n, 0, -1):
        print(v[1])
        v[1], v[i] = v[i], v[1]
        heapify(v, 1, i-1)

n = int(input())

list_to_sort = []
for i in range(n):
    list_to_sort.append(int(sys.stdin.readline()))

heap_sort(n, list_to_sort)
