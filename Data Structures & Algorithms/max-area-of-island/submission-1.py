class Solution:
    max_size = 0
    directions = [(-1,0), (1,0), (0,1), (0,-1)]

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0: 
                    continue

                self.dfs(grid, i, j, 1)
        
        return self.max_size

    def dfs(self, grid: List[List[int]], i: int, j: int, size: int) -> int:
        '''
        Iterate through island cells and update max_size
        '''

        # Update max_size if appropriate
        print(f"grid[{i}][{j}] = {grid[i][j]}. Size: {size}")
        if size > self.max_size: 
            self.max_size = size 

        # Sink the current cell to avoid revisiting
        grid[i][j] = 0

        # Iterate in other directions
        for dx,dy in self.directions: 
            inew = i + dx
            jnew = j + dy

            # Check that coords are within bounds
            if inew < 0 or inew >= len(grid) or jnew < 0 or jnew >= len(grid[0]):
                continue

            if grid[inew][jnew] == 0:
                continue

            size = self.dfs(grid, inew, jnew, size+1)

        return size