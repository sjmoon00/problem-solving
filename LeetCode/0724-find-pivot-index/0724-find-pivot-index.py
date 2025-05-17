class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # N = len(nums)
        # nums.append(0)
        # nums = [0] + nums
        # for i in range(1, N+1):
        #     left, right = sum(nums[:i]), sum(nums[i+1:])
        #     if left == right:
        #         return i-1
        # return -1
        left, right = 0, sum(nums[1:])
        N = len(nums)
        for i in range(1, N):
            if left == right:
                return i-1
            left += nums[i-1]
            right -= nums[i]
        if left == right:
            return N-1
        return -1