import sys
import heapq as hq
from collections import defaultdict
input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())
INF = 1e9
G = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))

def dijkstra(start):
    distances = {x:INF for x in range(1, V+1)}
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

dist = dijkstra(K)
for x in dist.values():
    if x >= INF:
        print('INF')
    else:
        print(x)