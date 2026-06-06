class Solution:

    def encode(self, strs: List[str]) -> str:
        # Approach: introduce a prefix which specifies the length of each string
        # More time than a delimiter approach, but works for all characters

        return "".join([ str(len(s)) + ":" + s for s in strs ])

    def decode(self, s: str) -> List[str]:
        buffer = ""
        strs = []
        i = 0
        
        while i < len(s):
            # Length prefix extraction
            if s[i] != ":":
                buffer += s[i]
            # String extraction
            else: 
                l = int(buffer)
                strs.append(s[i+1:i+1+l])
                buffer = ""
                i = i+l

            i += 1

        return strs
