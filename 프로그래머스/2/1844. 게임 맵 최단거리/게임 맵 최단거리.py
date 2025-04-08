from collections import deque
def solution(maps):
    answer = -1
    N, M = len(maps), len(maps[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    queue = deque([(0, 0, 1)])
    while queue:
        x, y, cnt = queue.popleft()
        if x == N-1 and y == M-1:
            answer = cnt
            break
        for d in directions:
            nx, ny = x + d[0], y + d[1]
            if not(0 <= nx < N) or not(0 <= ny < M):
                continue
            if visited[nx][ny]:
                continue
            if maps[nx][ny] == 0:
                continue

            visited[nx][ny] = True
            queue.append((nx, ny, cnt + 1))
    
    return answer