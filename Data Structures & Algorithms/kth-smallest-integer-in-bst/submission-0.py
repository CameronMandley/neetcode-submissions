# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def createArray(root):
            if not root:
                return []
            else:
                return createArray(root.left) + [root.val] + createArray(root.right)
        array = createArray(root)
        return array[k-1]
        

        

        