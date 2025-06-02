import heapq as hq
INF = float('inf')
N, M, X = map(int, input().split())
# G = [[0 if i == j else INF for j in range(N+1)] for i in range(N+1)]
G = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, cost = map(int, input().split())
    G[start].append((end, cost))

def dijkstra(G, start):
    distances = {node : INF for node in range(N+1)}
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

result = 0
dijkstra(G, X)
for i in range(1, N+1):
    go = dijkstra(G, i)
    back = dijkstra(G, X)
    result = max(result, go[X] + back[i])
print(result)