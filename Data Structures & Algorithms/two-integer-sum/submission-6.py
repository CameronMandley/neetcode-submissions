class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_nums = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in prev_nums:
                return [prev_nums[diff], i]
            else:
                prev_nums[nums[i]] = i
            
        