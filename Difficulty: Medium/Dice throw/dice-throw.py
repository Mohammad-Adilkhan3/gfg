class Solution:
    def noOfWays(self, m,n,x):
        # code here
        dp = [[0] * (x + 1) for _ in range(n + 1)]
        dp[0][0] = 1  # 1 way to get sum 0 with 0 dice
    
        for dice in range(1, n + 1):
            for target_sum in range(1, x + 1):
                for face in range(1, m + 1):
                    if target_sum - face >= 0:
                        dp[dice][target_sum] += dp[dice - 1][target_sum - face]
    
        return dp[n][x]