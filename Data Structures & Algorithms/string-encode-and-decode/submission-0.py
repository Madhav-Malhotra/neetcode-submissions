class Solution:

    def encode(self, strs: List[str]) -> str:
        # Approach: introduce a header which specifies the number of strings
        # Followed by the length of each string. 
        # More time than a delimiter approach, but works for all characters

        n = str(len(strs))
        lens = [str(len(s)) for s in strs]
        header = ":".join([n] + lens) + ":"
        out = header + "".join(strs)

        return out

    def extract_header(self,s: str) -> List[List[int], str]:
        # Helper vars
        num_strs = None
        lens = []
        i = -1
        buffer = ""

        while i < len(s) - 1:
            # Gather chars until special char reached
            i += 1
            char = s[i]
            if char != ":":
                buffer += char
                continue
            
            # Haven't gotten num_strs
            if num_strs is None: 
                num_strs = int(buffer)
                buffer = ""
                continue
            
            # Haven't gotten all lengths
            if len(lens) < num_strs:
                lens.append(int(buffer))
                buffer = ""

            # Just got last length
            if len(lens) == num_strs:
                break
        
        return [[num_strs] + lens, s[i+1:]]

    def decode(self, s: str) -> List[str]:
        lens, msg = self.extract_header(s)
        n_strs = lens[0]

        out = []
        start = 0
        for l in lens[1:]:
            out.append(msg[start:start+l])
            start += l

        return out
