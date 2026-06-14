'''
Constraints: 
- O(log n) time complexity
- Up to 1000 numbers
- Don't know the rotation amount
- Unique elements

Thinking: 
- Do binary search, just need to remap the indices after rotation?
    - Can't remap indices since we don't know where the rotation amount is
- What are we trying to search for? Stop condition:
    - We want to find an index such that the number before it was larger than it
- Let's say we do binary search - how would we know whether to look higher or lower in indices?
    - We know any subarray is ascending. So if the start < end for the subarray, it isn't correct

Algorithm: 
- Cut the target array in half
    - If array has 2 els or less, return min(array)
    - If nums[left.start] < nums[left.end], repeat with right array.
    - Else repeat with left array. 
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1

        while (end - start) > 1:
            mid = (end + start) >> 1
            print(f"Start: {start}. End: {end}. Mid: {mid}")

            if nums[start] < nums[mid]:
                start = mid
            else: 
                end = mid

        # Edge case: no drop within array only at edges
        out = nums[end]
        if end == len(nums) - 1:
            out = min(out, nums[0])
        return out