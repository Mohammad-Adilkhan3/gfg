class Solution:
	def isWordExist(self, mat, word):
		# Code here
		n = len(mat)
        m = len(mat[0])
        L = len(word)

        visited = [[False]*m for _ in range(n)]

        def dfs(i, j, idx):
            # If full word is matched
            if idx == L:
                return True

            # Boundary + mismatch + reuse check
            if i < 0 or i >= n or j < 0 or j >= m:
                return False
            if visited[i][j] or mat[i][j] != word[idx]:
                return False

            # Mark visited
            visited[i][j] = True

            # Explore 4 directions
            found = (
                dfs(i+1, j, idx+1) or
                dfs(i-1, j, idx+1) or
                dfs(i, j+1, idx+1) or
                dfs(i, j-1, idx+1)
            )

            # Backtrack
            visited[i][j] = False
            return found

        # Try starting DFS from every cell
        for i in range(n):
            for j in range(m):
                if mat[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False