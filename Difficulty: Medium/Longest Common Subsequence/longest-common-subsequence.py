class Solution:
    def lcs(self, S1, S2):
        m = len(S1)
        n = len(S2)
        dp = [[0] * (n + 1) for x in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if S1[i - 1] == S2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j],
                                   dp[i][j - 1])
        return dp[m][n]

#{ 
 # Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s1 = str(input())  # Take first string as input
        s2 = str(input())  # Take second string as input
        ob = Solution()
        # Call the lcs function and print the result
        print(ob.lcs(s1, s2))
        print("~")

# } Driver Code Ends