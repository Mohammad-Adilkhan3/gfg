def findMinCost(x, y, costX, costY):
    m = len(x)
    y = len(y)

    # Create a DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize the DP table
    for i in range(1, m + 1):
        dp[i][0] = i * costX
    for j in range(1, n + 1):
        dp[0][j] = j * costY

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + costX, dp[i][j - 1] + costY)

    # The answer is the minimum cost to make the entire strings x and y identical
    return dp[m][n]

# Example usage:
x1, y1 = "abcd", "acdb"
costX1, costY1 = 10, 20
print(findMinCost(x1, y1, costX1, costY1))  # Output: 30

x2, y2 = "ef", "gh"
costX2, costY2 = 10, 20
print(findMinCost(x2, y2, costX2, costY2))  # Output: 60
