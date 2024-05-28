def minimumCost(n, w, cost):
    # Create a dp array to store minimum cost for each weight from 0 to w
    dp = [float('inf')] * (w + 1)
    dp[0] = 0  # Base case: cost to buy 0 kg is 0

    # Fill the dp array
    for i in range(1, w + 1):
        for j in range(1, n + 1):
            if j <= i and cost[j - 1] != -1:
                dp[i] = min(dp[i], dp[i - j] + cost[j - 1])

    # If dp[w] is still infinity, it means we cannot buy exactly w kg
    return dp[w] if dp[w] != float('inf') else -1

# Example usage:
n1, w1 = 5, 5
cost1 = [20, 10, 4, 50, 100]
print(minimumCost(n1, w1, cost1))  # Output: 14

n2, w2 = 5, 5
cost2 = [-1, -1, 4, 3, -1]
print(minimumCost(n2, w2, cost2))  # Output: -1
