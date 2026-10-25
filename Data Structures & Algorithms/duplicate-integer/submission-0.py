class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numDict = {}
        for num in nums:
            if num not in numDict:
                numDict[num] = 1
            else:
                return True
        return False
         