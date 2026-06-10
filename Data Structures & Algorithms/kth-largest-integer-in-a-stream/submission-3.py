'''
Constraints: 
- Can have duplicate elements
- kth largest element in sorted order, not numerically
- Stream always has at least k elements. 

Thinking: 
- We don't have all elements upfront to construct a static array. Heap is ideal
- We don't want to pop k times to find the kth largest element. 
    - Instead, maintain a heap with just the top k elements. 
    - Maintaining a min heap would give us quick access to the smallest of the top k elements (the kth largest)
'''

import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = nums[:k]
        self.k = k
        heapq.heapify(self.h)

        # Add remaining nums if not small
        for n in nums[k:]:
            if n > self.h[0]:
                heapq.heapreplace(self.h, n)

        print(f"Init: {self.h}")

    def add(self, val: int) -> int:
        # Validation
        if not self.h: 
            self.h = [val]

        if val > self.h[0]:
            if len(self.h) == self.k:
                heapq.heapreplace(self.h, val)
            else:
                heapq.heappush(self.h, val)

        print(f"Add: {self.h}")
        
        return self.h[0]
        
