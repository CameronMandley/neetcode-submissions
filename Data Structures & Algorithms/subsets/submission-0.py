class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path, index):
            nonlocal res
            nonlocal nums

            if index == len(nums):
                res += [path[:]]
                return
            
            # include num:
            path += [nums[index]]
            backtrack(path, index+1)
            path.pop()

            # no include num:
            backtrack(path, index+1)

        backtrack([], 0)
        return res
        

        