import sys
import heapq as hq
from collections import defaultdict
input = sys.stdin.readline
INF = 1e9
N = int(input())
M = int(input())
# G = [[0 if i == j else INF for j in range(N+1)] for i in range(N+1)]
G = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, input().split())
    # G[a][b] = c
    G[a].append((b, c))
S, E = map(int, input().split())

def dijkstra_with_path(start):
    q = []
    hq.heappush(q, (0, start))
    distances = [INF] * (N+1)
    prev_node = [0] * (N+1)
    distances[start] = 0

    while q:
        dist, node = hq.heappop(q)
        if distances[node] < dist:
            continue

        for adj_node, cost in G[node]:
            n_dist = dist + cost
            if n_dist < distances[adj_node]:
                distances[adj_node] = n_dist
                hq.heappush(q, (n_dist, adj_node))
                prev_node[adj_node] = node

    return(distances, prev_node)

distances, path = dijkstra_with_path(S)
paths = [E]
now = E
while now != S:
    now = path[now]
    paths.append(now)
paths.reverse()

print(distances[E])
print(len(paths))
print(*paths)