import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
G = []
for _ in range(N):
    row = list(map(int, input().strip()))
    G.append(row)

def bfs():
    queue = deque([(0, 0, 1, 0)])
    visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = True
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        x, y, distance, broken = queue.popleft()
        if x == N-1 and y == M-1:
            return distance

        for d in dirs:
            nx, ny = x + d[0], y + d[1]
            if not(0 <= nx < N) or not(0 <= ny < M):
                continue
            
            if G[nx][ny] == 0 and not visited[nx][ny][broken]:
                visited[nx][ny][broken] = True
                queue.append((nx, ny, distance + 1, broken))
            elif G[nx][ny] == 1 and broken == 0 and not visited[nx][ny][1]:
                visited[nx][ny][1] = True
                queue.append((nx, ny, distance + 1, 1))
    return -1
print(bfs())