'''
Constraints: 
- Each row non-decreasing
- Each row starts larger than last ends

Thinking: 
- The 2D doesn't really affect binary search. Just pretend it's a long vector
- Will need to map 1D coordinate to 2D to actually access data without making a copy
'''

class Solution:
    def map2D(self, idx1d: int, n_rows: int, n_cols: int) -> List[int]:
        row = idx1d // n_cols
        col = idx1d - (n_cols * row)
        return [row, col]

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Validation
        if len(matrix) < 1 or len(matrix[0]) < 1: 
            return False
        
        # Setup data
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        lo = 0
        hi = n_rows * n_cols - 1

        # Run binary search
        while lo <= hi: 
            mid = (lo + hi) >> 1
            r,c = self.map2D(mid, n_rows, n_cols)
            el = matrix[r][c]

            if el < target:
                lo = mid + 1
            elif el > target:
                hi = mid - 1
            else: 
                return True

        return False 
        