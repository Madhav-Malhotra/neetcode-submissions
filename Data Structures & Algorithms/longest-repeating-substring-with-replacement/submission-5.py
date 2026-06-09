'''
Constraints: 
- Up to 1000 chars and up to 1000 k
- Return type simplifies problem: just need len of longest substring, not actual substring

Thinking:
- In any window, we need to know what the highest frequency char is. 
    - It's the other chars which will get 'substituted'. 
    - If <= k chars subbed per window, window size fine to be counted.
    - Need a count dict to track frequency. 
- Expand window right, shrink from left
'''

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Validation
        if len(s) < 1: 
            return 0

        lo = 0
        hi = 0
        max_f = 1
        max_len = 1
        count = defaultdict(int)
        count[s[lo]] += 1

        while hi < len(s) - 1:
            # Update frequencies
            hi += 1
            count[s[hi]] += 1
            if count[s[hi]] > max_f:
                max_f = count[s[hi]]
            
            # If too many chars subbed, shrink window
            while hi - lo + 1 - max_f > k: 
                count[s[lo]] -= 1
                lo += 1
            
            max_len = max(max_len, hi - lo + 1)

        return max_len


        