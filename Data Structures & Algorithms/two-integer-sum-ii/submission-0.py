'''
Constraints: 
- No hashtable. Need O(1) space. 
- Guaranteed 1 solution
- Presorted inputs
- Cannot have equal indices
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(numbers) - 1

        while lo < hi: 
            add = numbers[lo] + numbers[hi]

            if add < target: 
                lo += 1
            elif add > target: 
                hi -= 1
            else:
                # Need one indexed answer
                return [lo+1, hi+1]