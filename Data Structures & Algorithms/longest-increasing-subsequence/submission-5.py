class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0]*(max(nums)+1)
        min_num = min(nums)
        if min_num < 0:
            dp = [0]*(2*(max([abs(num) for num in nums]))+1)
            for i in range(len(nums)):
                nums[i] = nums[i] + abs(min_num)
        for num in nums:
            if num == 0:
                dp[num] = 1
                continue
            prev_dp = dp[:num]
            dp[num] = max(prev_dp) + 1
        return max(dp)
        