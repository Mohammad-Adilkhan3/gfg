def maxSum(n):
    # DP array to store calculated values
    dp = [0] * (n + 1)

    for num in range(1, n + 1):
        dp[num] = max(num, dp[num // 2] + dp[num // 3] + dp[num // 4])

    return dp[n]

# Example usage:
print(maxSum(12))  # Output: 13
print(maxSum(24))  # Output: 27
