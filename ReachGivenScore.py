def count(n):
    # Create a DP array to store the number of combinations for each score
    dp = [0] * (n + 1)

    # Initialize base case
    dp[0] = 1

    # Iterate through all possible scores
    for score in [3, 5, 10]:
        for i in range(score, n + 1):
            dp[i] += dp[i - score]

    return dp[n]

# Example usage:
print(count(10))  # Output: 2
print(count(20))  # Output: 4
