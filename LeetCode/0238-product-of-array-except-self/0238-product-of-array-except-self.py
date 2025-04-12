class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        answer = [1] * N
        arr1 = [1] * N
        arr2 = [1] * N
        arr1[0] = nums[0]
        arr2[-1] = nums[-1]
        for i in range(1, N):
            arr1[i] = arr1[i-1] * nums[i]
            arr2[N-1-i] = arr2[N-i] * nums[N-1-i]
        for i in range(N):
            if i-1 >= 0:
                answer[i] *= arr1[i-1]
            if i+1 < N:
                answer[i] *= arr2[i+1]
        
        return answer