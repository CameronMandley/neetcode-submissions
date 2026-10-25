class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        res[0] =res[n-1] = 1
        suffix_product = 1
        for i in range(1, n):
            res[i] = nums[i-1]*res[i-1]
        for i in range(n-2, -1, -1):
            suffix_product = nums[i+1]*suffix_product
            res[i] = res[i]*suffix_product
        return res


        