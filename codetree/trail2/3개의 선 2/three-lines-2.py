from itertools import combinations
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

min_x, max_x = min(x), max(x)
min_y, max_y = min(y), max(y)
answer = 0
for x_num in range(4):
    y_num = 3 - x_num

    x_lines_combi = combinations(range(min_x, max_x + 1), x_num)
    y_lines_combi = combinations(range(min_y, max_y + 1), y_num)
    passed = [False] * n
    if x_num == 0:
        for y_lines in y_lines_combi:
            for i, (px, py) in enumerate(points):
                if py in y_lines:
                    passed[i] = True
            if sum(passed) == n:
                answer = 1
        continue
    if y_num == 0:
        for x_lines in x_lines_combi:
            for i, (px, py) in enumerate(points):
                if px in x_lines:
                    passed[i] = True
            if sum(passed) == n:
                answer = 1
        continue
    
    for x_lines in x_lines_combi:
        for y_lines in y_lines_combi:
            for i, (px, py) in enumerate(points):
                if px in x_lines or py in y_lines:
                    passed[i] = True
            if sum(passed) == n:
                answer = 1

print(answer)