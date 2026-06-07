'''
Constraints: 
- Can be upper OR lowercase (all ASCII characters)
- Up to 1000 chars. 

Does output help simplify? 
- Yes: just need to return length of longest substring, not what it is 

Thinking: 
- Grow window by right when all chars unique. Count max size
- Shrink window from left until all chars become unique again

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Validation
        if len(s) < 1: 
            return 0

        lo = 0
        hi = max_len = 1
        window = set(s[:hi])

        while hi < len(s): 
            # Duplicate char detected - shrink window  
            if s[hi] in window:
                window.remove(s[lo])
                lo += 1
            # Add new char to window
            else:
                window.add(s[hi])
                curr = hi - lo + 1
                if curr > max_len: 
                    max_len = curr
                hi += 1

        return max_len
