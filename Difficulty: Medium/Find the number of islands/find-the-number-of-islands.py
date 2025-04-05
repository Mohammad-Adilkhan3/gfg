#User function Template for python3

class Solution:
    def numIslands(self, grid):
        # code here
        if not grid:
            return 0
    
        n = len(grid)
        m = len(grid[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
    
        # All 8 directions
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0), (1, 1)]
    
        def dfs(x, y):
            visited[x][y] = True
            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x < n and 0 <= new_y < m and not visited[new_x][new_y] and grid[new_x][new_y] == 'L':
                    dfs(new_x, new_y)
    
        count = 0
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == 'L':
                    dfs(i, j)
                    count += 1
    
        return count
    

#{ 
 # Driver Code Starts
# Driver code
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input().strip())
        m = int(input().strip())
        grid = [input().strip().split() for _ in range(n)]

        obj = Solution()
        print(obj.numIslands(grid))
        print("~")

# } Driver Code Ends