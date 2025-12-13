class Solution:
    def swapDiagonal(self, mat):
        # code here
        n,m=len(mat),len(mat[0])
        for i in range(n):
            for j in range(m):
                if i==j:
                    mat[i][j],mat[i][m-i-1]=mat[i][m-j-1],mat[i][j]
        return mat
    
