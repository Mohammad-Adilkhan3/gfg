class Solution:
    def cntOnes(self, grid):
        # code here
        if not grid:
            return 0
    
        rows, cols = len(grid), len(grid[0])
    
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
      
        def dfs(row, col):
            stack = [(row, col)]
    
            while stack:
                r, c = stack.pop()
                grid[r][c] = 2  # Mark the cell as visited
    
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
    
                    
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        stack.append((nr, nc))
    
        
        for r in range(rows):
            if grid[r][0] == 1:
                dfs(r, 0)
            if grid[r][cols - 1] == 1:
                dfs(r, cols - 1)
    
        for c in range(cols):
            if grid[0][c] == 1:
                dfs(0, c)
            if grid[rows - 1][c] == 1:
                dfs(rows - 1, c)
    
       
        count = sum(row.count(1) for row in grid)
    
        return count
