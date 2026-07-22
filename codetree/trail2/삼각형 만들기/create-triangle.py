from itertools import combinations
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

answer = 0
for p1, p2, p3 in combinations(points, 3):
    pts = [p1, p2, p3]

    for i in range(3):
        corner = pts[i]
        other1 = pts[(i + 1) % 3]
        other2 = pts[(i + 2) % 3]

        if corner[0] == other1[0] and corner[1] == other2[1]:
            height = abs(corner[1] - other1[1])
            width = abs(corner[0] - other2[0])
            answer = max(answer, height * width)
        elif corner[0] == other2[0] and corner[1] == other1[1]:
            height = abs(corner[1] - other2[1])
            width = abs(corner[0] - other1[0])
            answer = max(answer, width * height)

print(answer)