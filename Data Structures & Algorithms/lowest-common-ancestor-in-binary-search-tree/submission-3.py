'''
Constraints: 
- All values unique
- BST invariant (left child smaller, right child bigger)
- If p is a descendant of q, return q
- 100 nodes (O(N^2) possible)

Thinking: 
- How does BST invariant help? 
    - Let's say p < q. q could be a descendant of p's right subtree. Or q/p could have another common ancestor
    - How do we tell whether to search a subtree of one or look for a common ancestor?
    - What if we select the larger node and explore the left subtree until we reach leaves? 
        - If the smaller node is found, return the larger node as the ancestor
        - if the smaller node isn't found, we can't trace up since nodes aren't doubly linked
    - If the smaller node isn't found, recursively: 
        - Start at root. If p == root or q == root, return root. 
        - Start at the root. If max(p,q) < root, restart at root.left
        - Start at root. If min(p,q) > root, restart at root.right
        - Start at root. If neither of above apply, return root. 
- Can the recursive search encompass the case where one of the nodes is a descendant of the other? 

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # One node is a descendant of the other
        if root.val == p.val or root.val == q.val: 
            return root

        big = max(p.val, q.val)
        small = min(p.val, q.val)

        if root is not None and big < root.val: 
            return self.lowestCommonAncestor(root.left, p, q)
        elif root is not None and small > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root