from collections import defaultdict
import heapq as hq
import sys

input = sys.stdin.readline
N, E = map(int, input().split())
G = defaultdict(list)
for _ in range(E):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))
v1, v2 = map(int, input().split())

INF = 1e9
def dijkstra(start):
    distances = {x:INF for x in range(N+1)}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_node = hq.heappop(pq)
        if current_distance > distances[current_node]:
            continue

        for neighbor, cost in G[current_node]:
            distance = current_distance + cost

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                hq.heappush(pq, (distance, neighbor))
    return distances

start_dist, v1_dist, v2_dist = dijkstra(1), dijkstra(v1), dijkstra(v2)
start_v1 = start_dist[v1]
v1_v2 = v1_dist[v2]
v2_end = v2_dist[N]

start_v2 = start_dist[v2]
v2_v1 = v2_dist[v1]
v1_end = v1_dist[N]

s_v1_v2_e = start_v1 + v1_v2 + v2_end
s_v2_v1_e = start_v2 + v2_v1 + v1_end

answer = min(s_v1_v2_e, s_v2_v1_e)
if answer < INF:
    print(answer)
else:
    print(-1)