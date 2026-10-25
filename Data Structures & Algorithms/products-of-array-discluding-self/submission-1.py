class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)
        for i in range(1, len(nums)):
            output[i] = output[i-1]*nums[i-1]
        postfix = 1
        for j in range(len(nums) - 1, -1, -1):
            output[j] *= postfix
            postfix *= nums[j]
        return output
            
        