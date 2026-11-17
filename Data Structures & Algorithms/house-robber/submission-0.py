class Solution:
    def rob(self, nums: List[int]) -> int:
        maxRob = [0]*(len(nums) + 2)
        for i in range(2, len(nums) + 2):
            maxRob[i] = max(maxRob[i-1], maxRob[i-2] + nums[i-2])
        return maxRob[-1]