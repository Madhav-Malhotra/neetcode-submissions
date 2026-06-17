'''
Constraints: 
- Unknown amount of rotations
- O(log n) search time
- Up to 1000 numbers
- **All numbers are unique**
- One or two strictly ascending sequences

Thinking: 
- Binary search for O(log n) search time
    - In the current lo-hi range, if nums[hi] <= nums[lo], there's a break in strictly asending sequence
    - To get around the break, do more extensive checks about mid vs endpoints. 
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            # Found number
            mid = (lo + hi) // 2

            if nums[mid] == target:
                return mid

            # Left half is strictly ascending
            if nums[lo] <= nums[mid]:
                # Target contained in left half
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else: 
                    lo = mid + 1
            # Right half is strictly ascending
            else: 
                # Target contained in right half
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else: 
                    hi = mid - 1

        # No number found
        return -1