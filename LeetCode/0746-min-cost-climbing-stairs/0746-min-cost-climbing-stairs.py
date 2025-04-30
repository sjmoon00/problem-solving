class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        N = len(cost)
        dp = [0] * (N + 2)
        for i in range(2, N + 2):
            if i == N + 1:
                dp[i] = dp[i-2] + cost[i-2]
                continue
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
            
        return min(dp[-1], dp[-2])