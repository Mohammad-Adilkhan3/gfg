class Solution:
    def maxSum(self, n):
        # code here
        dp = [0] * (n + 1)

        for num in range(1, n + 1):
            dp[num] = max(num, dp[num // 2] + dp[num // 3] + dp[num // 4])
    
        return dp[n]