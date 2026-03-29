class Solution:
    def countPartitions(self, arr, d):
        # code here
        MOD = 10**9 + 7
        total_sum = sum(arr)
        target_sum = (total_sum + d) // 2
        if (total_sum + d) % 2 != 0 or target_sum < 0:
            return 0
        
        dp = [0] * (target_sum + 1)
        dp[0] = 1  
        
        for num in arr:
            for j in range(target_sum, num - 1, -1):
                dp[j] = (dp[j] + dp[j - num]) % MOD
        
        return dp[target_sum]
        
