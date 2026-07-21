from itertools import combinations
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
INF = float('inf')

answer = 0
for p1, p2, p3 in combinations(points, 3):
    slope1 = (p1[1] - p2[1]) / (p1[0] - p2[0]) if p1[0] - p2[0] != 0 else INF
    slope2 = (p2[1] - p3[1]) / (p2[0] - p3[0]) if p2[0] - p3[0] != 0 else INF
    slope3 = (p1[1] - p3[1]) / (p1[0] - p3[0]) if p1[0] - p3[0] != 0 else INF

    if not{0, INF}.issubset([slope1, slope2, slope3]):
        continue
    
    if slope1 not in [0, INF]:
        horiz, verti = 0, 0
        if p2[0] == p3[0]:
            horiz = abs(p1[0] - p3[0])
            verti = abs(p3[1] - p2[1])
        elif p1[0] == p3[0]:
            horiz = abs(p3[0] - p2[0])
            verti = abs(p1[1] - p3[1])
        answer = max(answer, horiz * verti)
    elif slope2 not in [0, INF]:
        horiz, verti = 0, 0
        if p1[0] == p2[0]:
            horiz = abs(p1[0] - p3[0])
            verti = abs(p1[1] - p2[1])
        elif p1[0] == p3[0]:
            horiz = abs(p1[0] - p2[0])
            verti = abs(p1[1] - p3[1])
        answer = max(answer, horiz * verti)
    elif slope3 not in [0, INF]:
        horiz, verti = 0, 0
        if p1[0] == p2[0]:
            horiz = abs(p2[0] - p3[0])
            verti = abs(p1[1] - p2[1])
        elif p2[0] == p3[0]:
            horiz = abs(p1[0] - p2[0])
            verti = abs(p2[1] - p3[1])
        answer = max(answer, horiz * verti)

print(answer)