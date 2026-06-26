'''
Constraints: 
- 10^5 numbers. O(n) solution preferred
- Positive and negative integers. 
- Just return a boolean (simplified return type)

Options: 
- Use a set of past numbers. 
    - O(n) space complexity. O(n) time complexity
- Sort in place as we walk through, lookup items with binary search
    - O(1) space complexity. O(n log n) time complexity
'''

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = set()

        for n in nums: 
            # Duplicate found - early stop
            if n in visited: 
                return True
            visited.add(n)

        return False