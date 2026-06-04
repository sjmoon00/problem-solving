n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
curr_dir = 0
x, y = 0, -1
for i in range(1, n * m + 1):
    nx, ny = x + dxy[curr_dir][0], y + dxy[curr_dir][1]

    if not(0 <= nx < n) or not(0 <= ny < m) or arr[nx][ny]:
        curr_dir = (curr_dir + 1) % 4
        nx, ny = x + dxy[curr_dir][0], y + dxy[curr_dir][1]

    arr[nx][ny] = i
    x, y = nx, ny

for row in arr:
    print(*row)