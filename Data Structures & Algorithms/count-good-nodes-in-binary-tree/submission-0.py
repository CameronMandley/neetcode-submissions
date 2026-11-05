# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        num_nodes = 0


        def getNodes(root, max_path):
            nonlocal num_nodes

            if not root:
                return
            if root.val >= max_path:
                num_nodes += 1
                getNodes(root.left, max(root.val, max_path))
                getNodes(root.right, max(root.val, max_path))
            else:
                getNodes(root.left, max(root.val, max_path))
                getNodes(root.right, max(root.val, max_path))
        getNodes(root, root.val)
        return num_nodes
        