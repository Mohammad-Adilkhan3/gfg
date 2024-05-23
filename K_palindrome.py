def kPalindrome(self, str, n, k):
        # code here
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for length in range(2, n+1): 
            for i in range(n-length+1):
                j = i + length - 1
                if str[i] == str[j]:
                    dp[i][j] = dp[i+1][j-1] if i+1 <= j-1 else 0
                else:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j-1])
        return 1 if dp[0][n-1] <= k else 0
