# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode], path = 0) -> int:
        if not root:
            return path
        else:
            return max(self.maxDepth(root.left, path+1), self.maxDepth(root.right, path+1))

        