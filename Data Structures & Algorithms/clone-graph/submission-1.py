"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

'''
Constraints: 
- All nodes connected. Undirected edges. 
- 1 indexed adjacency list
- Input is first node. Values 1 to n (AKA **unique values**)
- **No duplicate edges, no self loops**
- Up to 100 nodes. O(N^2) possible not preferable

Thinking:
Processing:
- Add first node to queue
- pop from queue. For each edge, update 1st.neighbours
    - Then, add all neighbours to queue.
Copying: 
- Need to create new nodes via hashmap from value to node instance (unique vals)
'''

from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Validation
        if node is None: 
            return None
        
        # Create map for new nodes
        out = {}
        q = deque([node])

        while q:
            # Setup node by val
            curr = q.popleft()
            if out.get(curr.val) is None: 
                out[curr.val] = Node(curr.val)

            # Add on neighbours
            for nbr in curr.neighbors: 
                if out.get(nbr.val) is None: 
                    out[nbr.val] = Node(nbr.val)
                    q.append(nbr)
                
                out[curr.val].neighbors.append(out[nbr.val])

        return out[node.val]
       