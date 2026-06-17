'''
Constraints: 
- Up to 1000 bars

Thinking: 
- Water stored is width x height. Height = min(h[i], h[j]). Width = j - i
- Start with widest containers first (set j = len(h) - 1, i = 0)
    - If h[i+1] > h[j-1], set i = i+1. Else j = j-1
    - Track max amount stored over time
'''

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_area = -1

        while i < j: 
            # Compute current area
            width = j - i
            height = min(heights[j], heights[i])
            area = width * height
            if area > max_area:
                max_area = area

            # The bigger height stays. The smaller goes
            if heights[i] > heights[j]:
                j = j - 1
            else:
                i = i + 1

        return max_area
        