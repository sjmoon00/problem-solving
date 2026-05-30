x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

grid = [[0] * 2001 for _ in range(2001)]
offset = 1000
for i in range(x1[0] + offset, x2[0] + offset):
    for j in range(y1[0] + offset, y2[0] + offset):
        grid[i][j] = 1

for i in range(x1[1] + offset, x2[1] + offset):
    for j in range(y1[1] + offset, y2[1] + offset):
        grid[i][j] = 2

min_x, max_x = 9999, 0
min_y, max_y = 9999, 0
for i in range(2001):
    for j in range(2001):
        tile = grid[i][j]
        if tile == 1:
            min_x, max_x = min(min_x, i), max(max_x, i)
            min_y, max_y = min(min_y, j), max(max_y, j)

print((max_x - min_x + 1) * (max_y - min_y + 1))