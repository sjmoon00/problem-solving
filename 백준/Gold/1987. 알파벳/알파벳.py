R, C = map(int, input().split())
board = []
for _ in range(R):
    row = list(input())
    board.append(row)

visited_alpha = set([board[0][0]])
visited = [[False] * C for _ in range(R)]
visited[0][0] = True
answer = 1
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(x, y, path):
    global answer
    answer = max(answer, path)
    for d in dirs:
        nx, ny = x + d[0], y + d[1]
        if not(0 <= nx < R) or not(0 <= ny < C):
            continue
        if visited[nx][ny]:
            continue
        n_node = board[nx][ny]
        if n_node in visited_alpha:
            continue
        # visited[nx][ny] = True
        visited_alpha.add(n_node)
        dfs(nx, ny, path+1)
        # visited[nx][ny] = False
        visited_alpha.discard(n_node)

dfs(0, 0, 1)
print(answer)