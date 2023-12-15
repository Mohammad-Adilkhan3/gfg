def nthPoint(N):
    MOD = 1000000007
    
    # Initialize dp array to store the number of ways to reach each point
    dp = [0] * (N + 1)
    
    # Base cases
    dp[0] = 1
    dp[1] = 1
    
    # Fill the dp array using the recurrence relation
    for i in range(2, N + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD
    
    return dp[N]

# Example usage:
N1 = 4
print(nthPoint(N1))  # Output: 5

N2 = 5
print(nthPoint(N2))  # Output: 8
