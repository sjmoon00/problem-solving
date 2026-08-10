from collections import Counter
n, m = map(int, input().split())
pairs = [tuple(sorted(map(int, input().split()))) for _ in range(m)]

C = Counter(pairs)
print(max(C.values()))