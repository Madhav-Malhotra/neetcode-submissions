'''
Constraints: 
- Only 26 types of tasks (A-Z)
- Up to 1000 instances of tasks

Thinking: 
- Best to do more frequent tasks first to leave room for cooldown
- Have a ready heap + blocked queue
    - Choose most frequent ready task first. 
    - Then move to blocked queue
    - On each iteration, check current cycle and unblock ready tasks if possible
'''

from collections import deque
from heapq import heappush, heappop

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count frequency
        freq = {}
        for t in tasks: 
            freq[t] = freq.get(t, 0) + 1
        
        # Prep blocked queue/ready heap
        cycle = 1
        blocked = deque()
        ready = []
        for f in freq.values():
            heappush(ready, -f)
        
        while blocked or ready: 
            print(f"Start. Cycle: {cycle}.")

            # Check if any tasks need to be unblocked
            if blocked: 
                cyc = blocked[0][0]
                if cyc == cycle:
                    f = blocked.popleft()[1]
                    print(f"Unblocked: {f}")
                    heappush(ready, f)

            # Run ready tasks if available
            if ready:
                f = heappop(ready)
                print(f"Ran: {f}.")
                # from -n UP to -1
                f += 1
                if f <= -1:
                    print(f"Next instance: {cycle+n+1}")
                    blocked.append((cycle+n+1, f))
                cycle += 1
            # Else skip time forward
            else:
                cycle = blocked[0][0]

        # Undo last increment
        return cycle - 1
