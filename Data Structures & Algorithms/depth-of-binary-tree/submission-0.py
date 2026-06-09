# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max_height = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, 1)
        return self.max_height
        
    def dfs(self, root: Optional[TreeNode], height: int):
        if root is None:
            return
        
        # Update max height found
        if height > self.max_height:
            self.max_height = height

        # Continue recursion
        self.dfs(root.left, height + 1)
        self.dfs(root.right, height + 1)
