# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Validation
        if root is None:
            return root
        
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)

        # Works even if values are None
        temp = root.left
        root.left = root.right
        root.right = temp

        return root