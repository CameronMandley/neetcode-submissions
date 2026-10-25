class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(len(output)):
                if j != i:
                    output[j] *= nums[i]
        return output
            
        