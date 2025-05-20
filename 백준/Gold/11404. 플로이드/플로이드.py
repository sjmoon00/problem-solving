import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
INF = float('inf')
G = [[INF] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    if c < G[a][b]:
        G[a][b] = c
for i in range(1, N+1):
    G[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            G[i][j] = min(G[i][j], G[i][k] + G[k][j])

for i in range(1, N+1):
    for j in range(1, N+1):
        if G[i][j] == INF:
            print(0, end=' ')
            continue
        print(G[i][j], end=' ')
    print()