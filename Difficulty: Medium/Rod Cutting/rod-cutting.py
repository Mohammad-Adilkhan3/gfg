#User function Template for python3

class Solution:
    def cutRod(self, price):
        #code here
        n = len(price)
        dp = [0]*(n+1)
        dp[0] = 0
        
        for i in range(1,n+1):
            # i = final length of the rod
            for j in range(i):
                # j = length of the rod for which dp is solved already
                dp[i] = max(dp[i],dp[j]+price[i-j-1])
        
        return dp[n]