n, m = map(int, input().split())

grid = [[0] * m for _ in range(n)]
dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
alpha_num = 0
A = ord('A')

grid[0][0] = 'A'
alpha_num = 1
curr_dir = 0
x, y = 0, 0
for i in range(2, n * m + 1):
    dx, dy = dxy[curr_dir][0], dxy[curr_dir][1]
    nx, ny = x + dx, y + dy
    if not(0 <= nx < n) or not(0 <= ny < m) or grid[nx][ny]:
        curr_dir = (curr_dir + 1) % 4
        dx, dy = dxy[curr_dir][0], dxy[curr_dir][1]
        nx, ny = x + dx, y + dy
    x, y = nx, ny
    grid[x][y] = chr(A + alpha_num)
    alpha_num = (alpha_num + 1) % 26

for row in grid:
    print(*row)