'''
Constraints:
- Only 20 stones. Not highly restrictive
- No shortcuts for return type - do need final weight. 
    - Barring fancy math possible here :D

Thinking: 
- Need to repeatedly find the two heaviest stones. 
- Min heap and take the root? Or max heap and pop twice? 
    - Max heap and pop twice. Will need to update an element anyways

'''

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1: 
            largest = heapq.heappop_max(stones)
            second = heapq.heappop_max(stones)
            if largest > second: 
                heapq.heappush_max(stones, largest - second)
        
        return stones[0] if len(stones) else 0