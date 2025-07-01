from collections import defaultdict
import heapq as hq
N = int(input())
M = int(input())
G = defaultdict(list)
INF = 1e9
for _ in range(M):
    start, end, cost = map(int, input().split())
    G[start].append((end, cost))
start, end = map(int, input().split())

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

dist = dijkstra(start)
print(dist[end])