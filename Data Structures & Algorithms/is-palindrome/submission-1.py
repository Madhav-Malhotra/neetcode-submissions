'''
Constraints: 
- Must skip any characters that aren't alphanumeric (includes spaces)
- Up to 1000 chars

Options: 
- Two pointers iterating from start to end and end to start. 
    - O(1) space complexity. O(n) time complexity
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Init lo and hi pointers
        lo = 0
        hi = len(s) - 1

        # Loop and increment pointers
        while lo <= hi: 
            # Validation 
            if not s[lo].isalnum(): 
                lo += 1 
                continue
            if not s[hi].isalnum(): 
                hi -= 1
                continue

            # Check if current pointers okay, then increment
            if s[lo].lower() != s[hi].lower():
                return False
            lo += 1
            hi -= 1

        # No errors found
        return True
            