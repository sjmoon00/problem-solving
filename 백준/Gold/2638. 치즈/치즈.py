from collections import deque, defaultdict
N, M = map(int ,input().split())
G = []
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
cheeses = set()
air = set()
for i in range(N):
    row = list(map(int, input().split()))
    G.append(row)
    for j, x in enumerate(row):
        if x == 0:
            air.add((i, j))
        else:
            cheeses.add((i, j))

def bfs():
    global cheeses
    queue = deque([(0, 0)])
    visited = [[False] * M for _ in range(N)]
    visited_cheese = defaultdict(int)
    while queue:
        x, y = queue.popleft()
        for d in dirs:
            nx, ny = x + d[0], y + d[1]
            if not(0 <= nx < N) or not(0 <= ny < M):
                continue
            if visited[nx][ny]:
                continue
            if G[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny))
            elif G[nx][ny] == 1:
                visited_cheese[(nx, ny)] += 1
    for (x, y), cnt in visited_cheese.items():
        if cnt > 1:
            G[x][y] = 0
            cheeses.discard((x, y))
cnt = 0
while cheeses:
    bfs()
    cnt += 1
print(cnt)