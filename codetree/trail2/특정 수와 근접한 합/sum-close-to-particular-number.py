from itertools import combinations
N, S = map(int, input().split())
arr = list(map(int, input().split()))

answer = 1e9
for comb in combinations(arr, N-2):
    T = sum(comb)
    answer = min(answer, abs(T - S))

print(answer)