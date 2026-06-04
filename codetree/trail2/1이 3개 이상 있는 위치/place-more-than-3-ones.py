n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
answer = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for dx, dy in dxy:
            nx, ny = i + dx, j + dy
            if not(0 <= nx < n) or not(0 <= ny < n):
                continue

            if grid[nx][ny]:
                cnt += 1
        if cnt >= 3:
            answer += 1

print(answer)