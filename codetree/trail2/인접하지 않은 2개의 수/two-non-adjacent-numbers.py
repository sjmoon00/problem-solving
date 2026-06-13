from itertools import combinations
n = int(input())
numbers = list(map(int, input().split()))

answer = 0
for i, j in combinations(range(n), 2):
    if i + 1 == j: continue
    answer = max(answer, numbers[i] + numbers[j])

print(answer)