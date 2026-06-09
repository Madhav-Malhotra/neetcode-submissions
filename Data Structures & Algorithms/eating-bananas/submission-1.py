'''
Constraints: 
- h >= len(piles)
- Up to 1000 piles. O(n^2) technically feasible

Does the type of output simplify things? 
- Yes: just produce the number - don't need to return sequence of eating

Thinking: 
- One approach could just be to test k=1, k=2, and so on. 
    - But this could be EXTREMELY slow given each pile can have up to 10^9 bananas
- Is there a better starting point for k? Or a better increment? 
    - In general, I can't see one. Only for the edge case when len(piles) == h
    - Can we put a min or max bound on k instead? 
        - max(k) == max(piles) given h >= len(piles). min(k) == 1
        - This can let us do binary search on k
- Okay, let's say we have a specific k. How do we find the min number of hours to eat everything?
    - Does it matter the order in which we eat the piles? 
        - I don't think so: we can only ever subtract k bananas from every pile.
    - Thus, the time taken is sum([ceil(p/k) for p in piles])

Complexity: 
- No ancillary data structures. O(1) space complexity
- O(1) to figure out time for each of n piles for any k. Test log(n) vals for k. O(n log n) time complexity for n piles
    - But also have to find max(piles) once. O(n) + O(nlogn) = O(nlogn) complexity
'''
from math import ceil

class Solution:
    def eatingTime(self, piles: List[int], speed: int) -> int: 
        return sum([ceil(p/speed) for p in piles])

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)

        mid = 1
        time = 1
        while lo <= hi: 
            # Check time to eat for current guess
            mid = (lo + hi) >> 1
            time = self.eatingTime(piles, mid)
            print(f"lo: {lo}. hi: {hi}. mid: {mid}. time: {time}")

            # Eating too fast
            if time <= h: 
                hi = mid - 1
            # Eating too slow
            elif time > h:
                lo = mid + 1

        return lo