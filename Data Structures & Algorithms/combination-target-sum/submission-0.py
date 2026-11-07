class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(path, curr_sum, index):
            nonlocal res
            nonlocal nums
            
            if curr_sum == target:
                res += [path[:]]
                return

            if curr_sum > target or index == len(nums):
                return

            # case add num, stay curr num
            path += [nums[index]]
            backtrack(path, curr_sum+nums[index], index)
            path.pop()

            # case no add num, move to next num
            backtrack(path, curr_sum, index+1)
        backtrack([], 0, 0)
        return res

        