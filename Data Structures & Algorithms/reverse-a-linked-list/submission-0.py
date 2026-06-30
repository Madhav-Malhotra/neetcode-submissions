# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Options: 
- At minimum O(n) time complexity since we need to iterate through all elements
- Push elements onto a stack, then rewire nodes as you pop off. 
    - Requires two passes. Is it possible to do it in one? 
    - For each node, save next node and point next node back to current. Then repeat. 
    - Second approach better (single pass timewise and O(1) in place modification)
- head is optional so make sure to validate input
'''

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle empty list
        if head is None: 
            return

        # Iterate through list one at a time
        last = head
        curr = head.next

        while curr: 
            # Get next node
            next_node = curr.next
            # Set current node to point to last
            curr.next = last
            # Next iteration
            last = curr
            curr = next_node

        # last will end up at old tail. Update old head as new tail
        head.next = None
        return last