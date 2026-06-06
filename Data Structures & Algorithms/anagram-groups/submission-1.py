from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = defaultdict(list)
        for s in strs: 
            out[tuple(sorted(s))].append(s)
        return list(out.values())