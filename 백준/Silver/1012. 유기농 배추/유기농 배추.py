from collections import deque
T = int(input())
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for _ in range(T):
    M, N, K = map(int, input().split())
    ground = [[0] * N for _ in range(M)]
    for _ in range(K):
        x, y = map(int, input().split())
        ground[x][y] = 1
    
    def bfs(i, j):
        queue = deque([(i, j)])
        visited = [[False] * N for _ in range(M)]
        visited[i][j] = True
        while queue:
            x, y = queue.popleft()
            for d in dirs:
                nx, ny = x + d[0], y + d[1]
                if not(0 <= nx < M) or not(0 <= ny < N):
                    continue
                if visited[nx][ny]:
                    continue
                
                if ground[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    ground[nx][ny] = 0

    cnt = 0
    for i in range(M):
        for j in range(N):
            if ground[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)