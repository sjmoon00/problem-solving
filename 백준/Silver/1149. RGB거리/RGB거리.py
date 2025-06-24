import sys
input = sys.stdin.readline
N = int(input())
costs = []
for _ in range(N):
    row = list(map(int, input().split()))
    costs.append(row)

dp = [[0] * 3 for _ in range(N)]
dp[0] = costs[0]
for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

print(min(dp[-1]))