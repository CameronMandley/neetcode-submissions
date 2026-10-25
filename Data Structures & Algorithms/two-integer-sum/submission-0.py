class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            if diff in numDict:
                return sorted([numDict[diff], i])
            else:
                numDict[num] = i
            
        