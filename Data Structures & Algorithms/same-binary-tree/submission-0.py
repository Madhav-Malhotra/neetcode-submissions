# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Run BFS and check equality after - O(N) + O(N)
        queueP = deque([p] if p else [])
        queueQ = deque([q] if q else [])

        while queueP:
            nodeP = queueP.popleft()
            # While condition checks if P not empty. But Q could be empty
            try:
                nodeQ = queueQ.popleft()
            except IndexError:
                return False

            if (nodeP is None) ^ (nodeQ is None):
                return False
            if nodeP and nodeP.val != nodeQ.val:
                return False
            
            # Guaranteed same at this point
            if nodeP:
                queueP.append(nodeP.left)
                queueP.append(nodeP.right)
                queueQ.append(nodeQ.left)
                queueQ.append(nodeQ.right)

        # Ran out of nodes in P. Also in Q? 
        return len(queueQ) == 0