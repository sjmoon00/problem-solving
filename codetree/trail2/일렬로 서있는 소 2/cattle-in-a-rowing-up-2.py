from itertools import combinations
N = int(input())
A = list(map(int, input().split()))

combi = combinations(A, 3)
answer = 0
for a, b, c in combi:
    if a <= b <= c:
        answer += 1

print(answer)