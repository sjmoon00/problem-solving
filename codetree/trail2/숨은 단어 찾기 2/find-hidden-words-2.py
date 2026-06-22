N, M = map(int, input().split())
arr = [input() for _ in range(N)]

dxy = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
answer = 0
for i in range(N):
    for j in range(M):
        c1 = arr[i][j]
        if c1 != 'L':
            continue
        
        for dx, dy in dxy:
            nx, ny = i + dx, j + dy
            nnx, nny = nx + dx, ny + dy
            if not(0 <= nx < N) or not(0 <= ny < M) or not(0 <= nnx < N) or not(0 <= nny < M):
                continue
            c2, c3 = arr[nx][ny], arr[nnx][nny]
            if c1 + c2 + c3 == 'LEE':
                answer += 1

print(answer)