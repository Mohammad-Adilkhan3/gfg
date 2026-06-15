class Solution:
    def minimumCost(self, cost, w):
        # code here
        n=len(cost)
        dp = [float('inf')] * (w + 1)
        dp[0] = 0  
        for i in range(1, w + 1):
            for j in range(1, n + 1):
                if j <= i and cost[j - 1] != -1:
                    dp[i] = min(dp[i], dp[i - j] + cost[j - 1])
        return dp[w] if dp[w] != float('inf') else -1