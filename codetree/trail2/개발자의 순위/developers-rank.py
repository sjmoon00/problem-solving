from collections import defaultdict
k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

ranks = defaultdict(set)
for i in range(k):
    for j in range(n):
        first = arr[i][j]
        for m in range(j + 1, n):
            last = arr[i][m]
            ranks[i].add((first, last))

candidates = ranks[0]
for i in range(k):
    candidates = candidates & ranks[i]

print(len(candidates))