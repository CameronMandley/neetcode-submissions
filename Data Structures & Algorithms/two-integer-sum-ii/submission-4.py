class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            leftNum, rightNum = numbers[left], numbers[right]
            currSum = leftNum + rightNum
            if currSum < target:
                left += 1
            elif currSum > target:
                right -= 1
            else:
                return [left+1, right+1]
            
        