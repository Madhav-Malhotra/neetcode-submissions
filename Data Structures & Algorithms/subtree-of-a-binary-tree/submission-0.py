# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Thinking: 
- Naive approach is to go through each node of tree and run DFS if its val == subroot.val
    - Worst case: every node has val of subroot. O(n^2)
- Can we do better? 
    - With extra space, we could store a BFS style array at each node, then compare arrays with the BFS of the subroot
    - What if we combine the naive approach with a preliminary first pass to set the height at each node? 
        - Then, we only do a full subtree check if the height + subtree root val are the same
        - Compute complexity: O(n) for subroot height + O(n) to DFS root + O(n) to compare subtree + main tree at max 2 matching nodes (binary tree)
        - Space complexity: O(n) overheard to track height at each node. 
'''

from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Validation
        if subRoot is None: 
            return True
        if root is None:
            return False
        
        h_sub = self.get_height(subRoot)

        # Run BFS trying to find matching nodes
        q = deque([root])
        while q: 
            node = q.popleft()
            h_node = self.get_height(node)

            # Can early stop when checking height of all root nodes. 
            # If height of parent < height subtree, don't bother checking children
            if h_node > h_sub: 
                q.append(node.left)
                q.append(node.right)
            elif h_node == h_sub:
                match = self.check_same(node, subRoot)
                if match: 
                    return True
                else: 
                    # Need to continue since up to 2 candidates with right height
                    continue
        
        # No match found in the end
        return False

    def get_height(self, root: Optional[TreeNode]) -> int: 
        '''
        Find height of input binary tree
        '''

        # Base case
        if root is None: 
            return 0

        # Else: height is max of left/right + 1
        h_left = self.get_height(root.left)
        h_right = self.get_height(root.right)
        return max(h_left, h_right) + 1

    def check_same(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool: 
        '''
        Check if input trees are the same
        '''
        # Base case
        if (subroot is None) ^ (root is None):
            return False
        if root is None and subroot is None:
            return True
        if root.val != subroot.val:
            return False

        # Check same children exist
        is_same = self.check_same(root.left, subroot.left)
        is_same = is_same and self.check_same(root.right, subroot.right)
        return is_same

        

