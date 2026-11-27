class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # define dp[i] = whether or not you can reach index i starting from index 0
        dp = [False]*len(nums)
        dp[0] = True
        for i in range(len(nums)-1): # i = 0
            if dp[i]: # True
                curr_jump = nums[i] # 1
                for j in range(0, min(curr_jump+1, len(nums) - i)): 
                    dp[i+j] = True # dp[0] = True
        return dp[-1]

        