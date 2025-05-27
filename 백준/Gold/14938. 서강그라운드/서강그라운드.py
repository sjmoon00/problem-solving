INF = float('inf')
n, m, r = map(int, input().split())
items = [0] + list(map(int,input().split()))
# G = [[INF] * (n+1) for _ in range(n+1)]
G = [[0 if i == j else INF for j in range(n+1)] for i in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    G[a][b] = l
    G[b][a] = l

def floyd(G):
    global n
    for k in range(n+1):
        for i in range(n+1):
            for j in range(n+1):
                G[i][j] = min(G[i][j], G[i][k] + G[k][j])
floyd(G)
answer = 0
for i in range(1, n+1):
    tmp = 0
    for j in range(1, n+1):
        d = G[i][j]
        if d <= m:
            tmp += items[j]
    answer = max(answer, tmp)

print(answer)