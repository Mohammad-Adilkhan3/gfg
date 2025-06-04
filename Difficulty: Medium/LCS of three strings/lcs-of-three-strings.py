class Solution:
    def lcsOf3(self,A, B, C):
        # Code here
        n1,n2,n3=len(A),len(B),len(C)
        dp = [[[0] * (n3 + 1) for _ in range(n2 + 1)] for _ in range(n1 + 1)]

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                for k in range(1, n3 + 1):
                    if A[i - 1] == B[j - 1] == C[k - 1]:
                        dp[i][j][k] = 1 + dp[i - 1][j - 1][k - 1]
                    else:
                        dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])
    
        return dp[n1][n2][n3]