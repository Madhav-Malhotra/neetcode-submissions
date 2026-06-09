# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Return type: 
- Just true/false. Don't need to return/preserve exact height at each node

Thinking: 
- DFS down to the leaf nodes. Left/right height = 0 (no violation)
- As you bubble up, increase height. 
- If at any point, left vs. right subtree height differ by more than 1, return false
- Return true at the end
'''


class Solution:
    imbalanced = False

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
       self.dfs(root)
       return not self.imbalanced

    def dfs(self, root: Optional[TreeNode]) -> int: 
        '''
        At each level, return height (of left/right subtree - whichever is longer)
        '''
        if root is None:
            return 0
        
        # Do internal checks on whether subtree heights are imbalanced
        h_left = self.dfs(root.left)
        h_right = self.dfs(root.right)

        if abs(h_right - h_left) > 1:
            self.imbalanced = True

        # Return height for next level
        return max(h_left, h_right) + 1

'''
        1
    2       3
           4
'''
        
