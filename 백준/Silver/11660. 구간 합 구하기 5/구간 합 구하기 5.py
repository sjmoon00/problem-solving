import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = []
pre = [[0] * (N+1) for _ in range(N+1)]
for _ in range(N):
    row = list(map(int, input().split()))
    arr.append(row)
    
for i in range(1, N+1):
    for j in range(1, N+1):
        pre[i][j] += pre[i][j-1] + arr[i-1][j-1]
for i in range(1, N+1):
    for j in range(1, N+1):
        pre[i][j] += pre[i-1][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    total = 0
    
    s1, s2, s3, s4 = pre[x2][y2], pre[x2][y1-1], pre[x1-1][y2], pre[x1-1][y1-1]
    total = (s1 - s2 - s3 + s4)

    print(total)