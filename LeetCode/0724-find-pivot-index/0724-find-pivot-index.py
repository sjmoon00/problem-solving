class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        N = len(nums)
        nums.append(0)
        nums = [0] + nums
        for i in range(1, N+1):
            left, right = sum(nums[:i]), sum(nums[i+1:])
            if left == right:
                return i-1
        return -1