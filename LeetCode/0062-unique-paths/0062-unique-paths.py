class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        G = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                G[i][j] = G[i][j-1] + G[i-1][j]
        return G[-1][-1]