'''
Constraints: 
- Up to 1000 chars. O(N^2) possible not desirable

Thinking: 
- Need a fixed window size of len(s1) sliding from start to end of s2
- On each stride, reduce counter for first char, add counter for last char
- Compare to frequency of s1
'''

class Solution:
    def dictEqual(self, d1: dict[str, int], d2: dict[str, int]) -> bool:
        if d1.keys() != d2.keys():
            return False

        for k in d1.keys():
            if d1[k] != d2[k]:
                return False

        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Validation
        if len(s1) > len(s2):
            return False

        # Init counters
        s1_cnt = {}
        win_cnt = {}
        for i in range(len(s1)): 
            s1_cnt[s1[i]] = s1_cnt.get(s1[i], 0) + 1
            win_cnt[s2[i]] = win_cnt.get(s2[i], 0) + 1

        # Slide window through s2
        lo = 0
        hi = len(s1) - 1
        while hi < len(s2) - 1:
            if self.dictEqual(s1_cnt, win_cnt):
                return True

            # Slide + update frequency
            win_cnt[s2[lo]] -= 1
            if not win_cnt[s2[lo]]:
                del win_cnt[s2[lo]]
            lo += 1
            hi += 1
            win_cnt[s2[hi]] = win_cnt.get(s2[hi], 0) + 1

        return self.dictEqual(s1_cnt, win_cnt)
