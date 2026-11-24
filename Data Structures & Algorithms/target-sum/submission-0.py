class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp[i][j]: the number of different ways to sum nums[i:] to 0 <= j <= target
        # dp[i][j] = (subtract the num) dp[i][j-i] + (add the num) dp[i][j+i]
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n+1)]
        dp[0][0] = 1

        for i in range(n):
            for total, count in dp[i].items():
                dp[i+1][total+nums[i]] += count
                dp[i+1][total-nums[i]] += count
        return dp[n][target]
        