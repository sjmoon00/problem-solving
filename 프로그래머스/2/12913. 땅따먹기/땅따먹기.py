def solution(land):
    N = len(land)
    dp = [[0] * 4 for _ in range(N+1)]
    land = [[0] * 4] + land

    for i in range(1, N+1):
        for j in range(4):
            dp[i][j] = land[i][j] + max(dp[i-1][:j] + dp[i-1][j+1:])
    
    return max(dp[-1])