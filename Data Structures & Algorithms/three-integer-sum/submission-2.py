'''
Constraints: 
- Indices must all be distinct. Output can be returned in any order
- Up to 10^3 nums. Positive and negative nums. 

Thinking: 
- Need to find all additions of pairs of twos. Then check if their negations exist.
- In theory, I can leverage information about the range of numbers to filter out 
  unlikely pairings. Though seems complicated.
- Problem is that I'm running into O(n^2) time complexity
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort to avoid duplicates
        nums = sorted(nums)
        seen = set()
        out = []

        for i in range(len(nums)):
            n = nums[i]
            print(f"Outer loop: {n}")

            # Will check numbers bigger than n after. Can't possibly get sum = 0
            if n > 0:
                break

            # n is negative. Find numbers larger than 0 to add onto it.
            lo = i+1
            hi = len(nums) - 1

            # 2 point search
            while lo < hi: 
                nl = nums[lo]
                nh = nums[hi]
                add = nl + nh + n
                if add > 0:
                    hi -= 1
                elif add < 0: 
                    lo += 1
                else:
                    # Save sol so we don't have duplicates
                    lst = [n,nl,nh]
                    key = "".join( [str(l) for l in lst] )
                    if key not in seen:
                        seen.add(key)
                        out.append(lst)
                    lo += 1

        return out

