class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)
        first = [1]*len(nums)
        second = [1]*len(nums)

        for i in range(1, len(nums)):
            first[i] = nums[i-1]*first[i-1]
        for i in range(len(nums) - 2, -1, -1):
            second[i] = nums[i+1]*second[i+1]
        for i in range(len(nums)):
            result[i] = first[i]*second[i]
        return result
        