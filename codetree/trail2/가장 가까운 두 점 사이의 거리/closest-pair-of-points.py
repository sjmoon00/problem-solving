from itertools import combinations
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

answer = float('inf')
for p1, p2 in combinations(points, 2):
    answer = min(answer, (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

print(answer)