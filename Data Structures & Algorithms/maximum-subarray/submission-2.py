class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0]*2 for _ in range(n)]
        dp[-1][0] = dp[-1][1] = nums[-1]
        for i in range(n-2, -1, -1):
            dp[i][1] = max(dp[i+1][1] + nums[i], nums[i])
            dp[i][0] = max(dp[i+1][0], dp[i][1])
        return dp[0][0]
        