import sys
input = sys.stdin.readline
N, K = map(int, input().split())
arr = []
arr.append((0, 0))
for _ in range(N):
    arr.append(tuple(map(int, input().split())))

dp = [[0] * (K+1) for _ in range(N+1)]
for i in range(1, N+1):
    weight, value = arr[i]
    for j in range(1, K+1):
        if weight <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
            
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])