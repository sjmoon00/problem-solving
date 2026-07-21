from itertools import combinations
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

answer = 1e9
for candid_points in combinations(points, n - 1):
    x_sort = sorted(candid_points, key=lambda x: x[0])
    y_sort = sorted(candid_points, key=lambda x: x[1])
    minX, maxX = x_sort[0][0], x_sort[-1][0]
    minY, maxY = y_sort[0][1], y_sort[-1][1]

    answer = min(answer, (maxX - minX) * (maxY - minY))

print(answer)