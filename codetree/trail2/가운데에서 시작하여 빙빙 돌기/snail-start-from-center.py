n = int(input())
grid = [[0] * n for _ in range(n)]

dxy = [(0, 1), (-1, 0), (0, -1), (1, 0)]
x, y = n - 1, n - 1
grid[x][y] = n * n
curr_dir = 2
for i in range(n * n - 1, 0, -1):
    dx, dy = dxy[curr_dir][0], dxy[curr_dir][1]
    nx, ny = x + dx, y + dy
    if not(0 <= nx < n) or not(0 <= ny < n) or grid[nx][ny]:
        curr_dir = (curr_dir + 3) % 4
        dx, dy = dxy[curr_dir][0], dxy[curr_dir][1]
        nx, ny = x + dx, y + dy
    
    x, y = nx, ny
    grid[x][y] = i

for row in grid:
    print(*row)