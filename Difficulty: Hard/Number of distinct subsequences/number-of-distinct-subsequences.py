#User function Template for python3

class Solution:
    def distinctSubseq(self, S):
        # code here
        MOD = 10**9 + 7
        n = len(s)
    
       
        dp = [0] * (n + 1)
    
       
        dp[0] = 1
    
        
        last_index = {}
    
        
        for i in range(1, n + 1):
            dp[i] = (2 * dp[i - 1]) % MOD
    
            
            if s[i - 1] in last_index:
                dp[i] -= dp[last_index[s[i - 1]] - 1]
    
           
            last_index[s[i - 1]] = i
    
            dp[i] %= MOD
    
        
        return ((dp[n] - 1) % MOD)+1


