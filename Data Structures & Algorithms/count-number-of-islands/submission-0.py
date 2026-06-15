'''
Constraints: 
- Vertical/horizontal edges only
- Max 100^2 cells

Thinking: 
- We can have a visited set of indices
- Iterate through the array by columns, then rows
    - For each visited node or 0, continue
    - For each 1, kick off DFS and add '1' nodes to visited set
'''

class Solution:
    visited = None
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    def numIslands(self, grid: List[List[str]]) -> int:
        self.visited = set()
        n_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) in self.visited or grid[i][j] == '0':
                    continue

                # Recurse in all directions, then increment
                self.find_linked_islands(grid, i, j)
                n_islands += 1

        return n_islands

    def find_linked_islands(self, grid: List[List[str]], i: int, j: int):
        '''
        Recursively visits all '1's and adds them to the set
        '''
        for dx,dy in self.directions: 
            coordx = i + dx
            coordy = j + dy
            
            # Skip coordinates outside array (guaranteed water)
            if coordx < 0 or coordx >= len(grid) or coordy < 0 or coordy >= len(grid[0]):
                continue
            
            # Skip already visited coordinates and 0
            if (coordx,coordy) in self.visited or grid[coordx][coordy] == "0":
                continue

            self.visited.add((coordx,coordy))
            self.find_linked_islands(grid, coordx, coordy)
            


                