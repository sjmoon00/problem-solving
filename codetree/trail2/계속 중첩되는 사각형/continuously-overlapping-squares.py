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
for num, (a1, b1, a2, b2) in enumerate(zip(x1, y1, x2, y2)):
    for i in range(a1 + offset, a2 + offset):
        for j in range(b1 + offset, b2 + offset):
            if num % 2 == 0: # 빨강
                grid[i][j] = 1
            else: # 파랑
                grid[i][j] = 2

answer = 0
for i in range(201):
    for j in range(201):
        if grid[i][j] == 2:
            answer += 1
print(answer)