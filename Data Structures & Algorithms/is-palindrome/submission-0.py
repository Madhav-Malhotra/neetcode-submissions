class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Need to normalise string
        s = "".join(filter(lambda char : char.isalnum(), s)).lower()

        # Check position wise characters
        lo = 0
        hi = len(s) - 1
        while lo < hi:
            if s[lo] != s[hi]:
                return False
            
            lo += 1
            hi -= 1

        return True