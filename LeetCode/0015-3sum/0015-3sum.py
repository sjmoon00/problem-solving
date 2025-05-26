class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        answer = []
        for i in range(N-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, N-1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                print(s)
                if s > 0:
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    answer.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return answer