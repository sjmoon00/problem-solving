class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0] * N
        if N <= 2:
            if N == 1:
                return nums[0]
            elif N == 2:
                return max(nums[0], nums[1])
            else:
                return max(nums[1], nums[0] + nums[2])
            
        dp[0], dp[1], dp[2] = nums[0], max(nums[0], nums[1]), max(nums[1], nums[0] + nums[2])
        for i in range(3, N):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[-1]