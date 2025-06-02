class Solution:
    def uniquePaths(self, grid):
        # code here 
        n = len(grid)
        m = len(grid[0])
        dp = [[0] * m for _ in range(n)]
        
        dp[0][0] = 1 if grid[0][0] != 1 else 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    continue
                
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
        
        return dp[-1][-1]