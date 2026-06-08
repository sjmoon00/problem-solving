N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

x, y = N // 2, N // 2
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
curr_dir = 0
answer = board[x][y]
for command in str:
    if command == 'L':
        curr_dir = (curr_dir + 3) % 4
    elif command == 'R':
        curr_dir = (curr_dir + 1) % 4
    else:
        dx, dy = dxy[curr_dir][0], dxy[curr_dir][1]
        nx, ny = x + dx, y + dy
        if not(0 <= nx < N) or not(0 <= ny < N):
            continue
        
        x, y = nx, ny
        answer += board[x][y]

print(answer)