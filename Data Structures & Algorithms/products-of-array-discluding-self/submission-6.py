class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result, first, second = [1]*len(nums), [1]*len(nums), [1]*len(nums)
        for i in range(1, len(nums)):
            first[i] = first[i-1] * nums[i-1]
        for j in range(len(nums) - 2, -1, -1):
            second[j] = second[j+1] * nums[j+1]
        for k in range(len(nums)):
            result[k] = first[k]*second[k]
        return result