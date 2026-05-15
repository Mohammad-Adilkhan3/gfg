class Solution:

    def optimalKeys(self, n: int) -> int:
        # code here
        dp = [0]*(n+1)
        for i in range(1, n+1):
            
            # press key1: A's till_now + 1
            dp[i] = dp[i-1] + 1
            
            for j in range(1, i-1): # this maintains i - j >= 2
                
                remaining_operations = i - j
                
                # now Ctrl+A and Ctrl+C is mandatory
                
                paste = i - j - 2 # this number of paste now we can perform
                
                # original + original * no_of_paste
                
                dp[i] = max(dp[i], dp[j] + dp[j]*paste)

        return dp[n]
