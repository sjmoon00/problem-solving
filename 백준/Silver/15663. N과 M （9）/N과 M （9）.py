from itertools import permutations
N, M = map(int, input().split())
A = list(map(int, input().split()))
combi = set(permutations(A, M))
combi = list(combi)
combi.sort()
for c in combi:
    print(*c)