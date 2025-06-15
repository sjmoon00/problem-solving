class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        answer = False
        wordSet = set(wordDict)
        N = len(s)
        dp = [False] * (N + 1)
        dp[0] = True

        for i in range(1, N+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        return dp[N]