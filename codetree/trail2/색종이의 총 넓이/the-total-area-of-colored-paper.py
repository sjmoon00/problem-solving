n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

grid = [[0] * 201 for _ in range(201)]
offset = 100
for a, b in zip(x, y):
    a, b = a + offset, b + offset
    for i in range(a, a + 8):
        for j in range(b, b + 8):
            grid[i][j] = 1

print(sum(sum(x) for x in grid))