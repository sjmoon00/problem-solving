n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

answer = 1e9
for x_line in range(2, 101, 2):
    for y_line in range(2, 101, 2):
        grid = [0] * 5
        for x, y in points:
            if x > x_line and y > y_line:
                grid[1] += 1
            elif x < x_line and y > y_line:
                grid[2] += 1
            elif x < x_line and y < y_line:
                grid[3] += 1
            elif x > x_line and y < y_line:
                grid[4] += 1
        M = max(grid)
        answer = min(answer, M)
print(answer)