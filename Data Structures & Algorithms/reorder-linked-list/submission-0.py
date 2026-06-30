# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
[0, 1] -> [0, 1]
[0, 1, 2] -> [0, 2, 1] (end case is lo+1 == hi-1)
[0, 1, 2, 3] -> [0, 3, 1, 2] (end case is lo+1 > hi-1)

Options:
- At least O(n) time complexity since each node must be visited at least once. 
- Most likely O(n) space complexity (can't think of a way to do it in place with a singly linked list)
- Two pass solution: 
    - Traverse linked list and read values into array. O(n) time/space
    - Use two pointers to add nodes onto a new linked list. O(n) time/space
- Single pass?
    - I don't think we can do it without knowing the length of the linked list. 
    - And to figure that out, we need to do a first pass on the linked list.
- Need to not modify values and no return type. So I presume we're just updating pointers.
'''

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # First pass: Traverse LL and extract vals
        nodes = []
        curr = head
        while curr: 
            nodes.append(curr)
            curr = curr.next

        # Second pass: two pointer to reorder nodes
        lo = 0
        hi = len(nodes) - 1

        while lo <= hi: 
            # Edge case: lo == hi (tail reached)
            if lo == hi: 
                nodes[lo].next = None
            else:
                # Gather nodes with pointers to update
                lo_n = nodes[lo]
                lo_n1 = nodes[lo+1] if lo+1 < len(nodes) else None
                hi_n = nodes[hi]

                # Make updates
                lo_n.next = hi_n
                hi_n.next = lo_n1 if lo+1 != hi else None

            lo += 1
            hi -= 1

        # [] -> returns None
        # [0] -> [0,None]
        # [0,1] -> [0,1,None]
        # [0,1,2] -> [0,2,1,None]
        # [0,1,2,3] -> [0,3,1,2,None]