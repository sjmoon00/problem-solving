x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

grid = [[0] * 2001 for _ in range(2001)]
offset = 1000
cnt = 0
for a1, b1, a2, b2 in zip(x1, y1, x2, y2):
    if cnt > 1:
        for i in range(a1 + offset, a2 + offset):
            for j in range(b1 + offset, b2 + offset):
                grid[i][j] = 0
        break
    
    for i in range(a1 + offset, a2 + offset):
        for j in range(b1 + offset, b2 + offset):
            grid[i][j] = 1
    cnt += 1

print(sum(sum(x) for x in grid))