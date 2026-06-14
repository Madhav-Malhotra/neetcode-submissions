from heapq import heappush, heapreplace

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        
        for n in nums:
            if len(h) < k: 
                heappush(h, n)
            elif n > h[0]: 
                heapreplace(h, n)
        
        return h[0]