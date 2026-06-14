'''
Constraints: 
- Up to 1000 points and positive/negative vals

Thinking: 
- Obvious approach would be to compute every distance then find the min k distances
- To speed that up, we can compute one distance at a time and save the min k found so far
    - If len(heap) < k, add on the distance
    - Else if curr < heap[0], heapreplace current distance. Need a maxheap
'''

import math 
from heapq import heapreplace, heappush

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []

        for p in points: 
            dist = -1 * math.sqrt(p[0]**2 + p[1]**2)

            if len(h) < k: 
                heappush(h, (dist, p))
            elif h[0][0] < dist:
                heapreplace(h, (dist, p))
        
        return [p for d,p in h]