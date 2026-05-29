n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

grid = [[0] * 201 for _ in range(201)]
offset = 100
for a1, b1, a2, b2 in zip(x1, y1, x2, y2):
    for i in range(a1 + offset, a2 + offset):
        for j in range(b1 + offset, b2 + offset):
            grid[i][j] = 1

print(sum(sum(x) for x in grid))