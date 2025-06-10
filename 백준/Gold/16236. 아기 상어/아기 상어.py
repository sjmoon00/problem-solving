from collections import deque
N = int(input())
space = []
size = 2
eat_cnt = 0
pos = (0, 0)
answer = 0
for i in range(N):
    row = list(map(int, input().split()))
    space.append(row)
    for j, x in enumerate(row):
        if x == 9:
            pos = (i, j)
space[pos[0]][pos[1]] = 0

def calc_dist(nx, ny):
    return abs(pos[0] - nx) + abs(pos[1] - ny)

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def bfs():
    queue = deque([(pos[0], pos[1], 0)])
    visited = [[False] * N for _ in range(N)]
    visited[pos[0]][pos[1]] = True
    dist = []

    while queue:
        x, y, path_len  = queue.popleft()
        for d in dirs:
            nx, ny = x + d[0], y + d[1]
            if not(0 <= nx < N) or not(0 <= ny < N):
                continue
            if visited[nx][ny]:
                continue

            fish = space[nx][ny]
            if fish == 0:
                queue.append((nx, ny, path_len + 1))
                visited[nx][ny] = True
            elif fish <= size:
                queue.append((nx, ny, path_len + 1))
                visited[nx][ny] = True
                if fish < size:
                    dist.append((path_len + 1, (nx, ny)))
    return dist

while True:
    distances = bfs()
    if not distances:
        break
    distances.sort(key=lambda x: (x[0], x[1][0], x[1][1]))

    dist, (x, y) = distances[0]
    answer += dist
    pos = (x, y)
    space[x][y] = 0
    eat_cnt += 1
    if eat_cnt == size:
        eat_cnt = 0
        size += 1

print(answer)