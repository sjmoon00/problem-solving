from itertools import combinations
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

answer = 0
for x_num in range(4):
    y_num = 3 - x_num

    x_lines_combi = list(combinations(range(11), x_num))
    y_lines_combi = list(combinations(range(11), y_num))

    for x_lines in x_lines_combi:
        for y_lines in y_lines_combi:
            passed = [False] * n
            
            for i, (px, py) in enumerate(points):
                if px in x_lines or py in y_lines:
                    passed[i] = True
            if sum(passed) == n:
                answer = 1

print(answer)