import sys
from collections import defaultdict
INF = 1e9
input = sys.stdin.readline
TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    G = defaultdict(lambda: INF)

    for _ in range(M):
        S, E, T = map(int, input().split())
        G[(S, E)] = min(G[(S, E)], T)
        G[(E, S)] = min(G[(E, S)], T)
    for _ in range(W):
        S, E, T = map(int, input().split())
        G[(S, E)] = min(G[(S, E)], -T)

    def df(start):
        distances = [INF] * (N+1)
        distances[start] = 0

        for i in range(N):
            for (a, b), c in G.items():
                if distances[b] > distances[a] + c:
                    distances[b] = distances[a] + c
                    if i == N-1:
                        return 'YES'
        return 'NO'

    print(df(1))