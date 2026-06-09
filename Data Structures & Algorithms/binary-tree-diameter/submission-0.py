# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Return type simplifies problem: don't need actual path - just longest path len
- Binary tree also simplifies problem since we know how many edges must be between nodes on two levels

Thinking: 
- Is it possible to iterate through all nodes O(n) time complexity + at each step know how far away every other node is? O(n) space complexity
    - Seems hard to do math on how far away every other node is depending on nearest common ancestor. 
- Brute force: pick every node as root and do DFS to find depth
    - O(n^2) computational complexity
- Could we use the distance to some anchor (likely root) to figure out distance to each other?
- Key insight: for any node, the longest path running through it is the height of the left subtree + the height of the right subtree
    - Can do dfs once to find the height of each node starting at the leaves 
    - Can track the max height found across dfs iterations
'''

class Solution:
    max_len = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.max_len

    def dfs(self, root: Optional[TreeNode]) -> int: 
        # Validation
        if root is None:
            return 0
        
        h_left, h_right = self.dfs(root.left), self.dfs(root.right)
        
        longest = h_left + h_right
        if longest > self.max_len:
            self.max_len = longest

        return max(h_left, h_right) + 1

