# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        num_nodes = 0

        def getNodes(root, maxPath):
            nonlocal num_nodes

            if not root:
                return
            elif root.val >= maxPath:
                num_nodes += 1
            maxPath = max(maxPath, root.val)
            getNodes(root.left, maxPath)
            getNodes(root.right, maxPath)

        getNodes(root, root.val)
        return num_nodes
        