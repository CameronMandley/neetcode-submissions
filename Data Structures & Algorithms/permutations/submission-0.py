class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path, remaining):
            nonlocal res

            if not remaining:
                res.append(path[:])
            
            for i in range(len(remaining)):
                path.append(remaining[i])
                new_remaining = remaining[:i] + remaining[i+1:]
                backtrack(path, new_remaining)
                path.pop()
        backtrack([], nums)
        return res
        