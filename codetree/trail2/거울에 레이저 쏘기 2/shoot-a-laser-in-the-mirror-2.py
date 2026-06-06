n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# 1~N: 아래, N+1~2N: 왼, 2N+1~3N: 위, 3N+1~4N: 오른
# 1~N: (-1, 0~N-1), N+1~2N: (0~N-1, N), 2N+1~3N: (N, 0~N-1), 3N+1~4N: (0~N-1, -1)

dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
curr_dir = 0
x, y = -1, -1
if (k - 1) // n == 0:
    curr_dir = 2
    x, y = -1, (k - 1) % n
elif (k - 1) // n == 1:
    curr_dir = 3
    x, y = (k - 1) % n, n
elif (k - 1) // n == 2:
    curr_dir = 0
    x, y = n, (n - 1) - (k - 1) % n
else:
    curr_dir = 1
    x, y = (n - 1) - (k - 1) % n, -1

# /: 위 -> 오른, 아래 -> 왼, 오른 -> 위, 왼 -> 아래
# \: 위 -> 왼, 아래 -> 오른, 오른 -> 아래, 왼 -> 위
answer = 0
while True:
    dx, dy = dxy[curr_dir][0], dxy[curr_dir][1]
    nx, ny = x + dx, y + dy
    if not(0 <= nx < n) or not(0 <= ny < n):
        print(answer)
        break
    x, y = nx, ny

    mirror = grid[nx][ny]
    if mirror == '/':
        if curr_dir == 0:
            curr_dir = 1
        elif curr_dir == 1:
            curr_dir = 0
        elif curr_dir == 2:
            curr_dir = 3
        else:
            curr_dir = 2
    else:
        if curr_dir == 0:
            curr_dir = 3
        elif curr_dir == 1:
            curr_dir = 2
        elif curr_dir == 2:
            curr_dir = 1
        else:
            curr_dir = 0
    answer += 1
