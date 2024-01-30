def LCSof3(A, B, C, n1, n2, n3):
    dp = [[[0] * (n3 + 1) for _ in range(n2 + 1)] for _ in range(n1 + 1)]

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            for k in range(1, n3 + 1):
                if A[i - 1] == B[j - 1] == C[k - 1]:
                    dp[i][j][k] = 1 + dp[i - 1][j - 1][k - 1]
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

    return dp[n1][n2][n3]

# Example 1
A1 = "geeks"
B1 = "geeksfor"
C1 = "geeksforgeeks"
n1 = len(A1)
n2 = len(B1)
n3 = len(C1)
print(LCSof3(A1, B1, C1, n1, n2, n3))  # Output: 5

# Example 2
A2 = "abcd"
B2 = "efgh"
C2 = "ijkl"
n4 = len(A2)
n5 = len(B2)
n6 = len(C2)
print(LCSof3(A2, B2, C2, n4, n5, n6))  # Output: 0
#The LCSof3 function uses dynamic programming to find the length of the longest common subsequence in three given strings A, B, and C. It builds a 3D array dp to store the length of the common subsequence at each position. The examples demonstrate the expected outputs.





