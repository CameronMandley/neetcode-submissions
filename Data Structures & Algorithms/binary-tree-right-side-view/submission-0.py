# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(root, length):
            nonlocal res

            if not root:
                return None
            if length == len(res):
                res += [root.val]
            dfs(root.right, length + 1)
            dfs(root.left, length + 1)
        dfs(root, 0)
        return res