class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            num1, num2 = numbers[i], numbers[j]
            if num1 + num2 == target:
                return [i+1, j+1]
            else:
                if num1 + num2 > target:
                    j -= 1
                else:
                    i += 1
        return False
        