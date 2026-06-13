n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

answer = 1e9
for i in range(1, n - 1):
    dist = 0
    for j in range(n - 1):
        if j == i:
            continue
        
        if j + 1 == i:
            n1, n2 = points[j], points[j + 2]
            dist += abs(n1[0] - n2[0]) + abs(n1[1] - n2[1])
        else:
            n1, n2 = points[j], points[j + 1]
            dist += abs(n1[0] - n2[0]) + abs(n1[1] - n2[1])
        
    answer = min(answer, dist)

print(answer)