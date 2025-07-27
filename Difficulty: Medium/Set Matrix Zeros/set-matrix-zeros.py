class Solution:
    def setMatrixZeroes(self, mat):
        # code here
        n,m=len(mat),len(mat[0])
        
        fr=fc=False
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    if i==0:
                        fr=True
                    if j==0:
                        fc=True
                    mat[i][0]=mat[0][j]=0
        for i in range(1,n):
            for j in range(1,m):
                if mat[i][0]==0 or mat[0][j]==0:
                    mat[i][j]=0
                    
        if fr:
            for j in range(m):
                mat[0][j]=0
        if fc:
            for i in range(n):
                mat[i][0]=0
        return mat
                    