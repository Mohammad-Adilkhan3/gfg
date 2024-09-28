def minCost(arr, k):
    n = len(arr)
    dp = [float('inf')] * n
    dp[0] = 0  # No cost to start at the first stone
    
    # Iterate over each stone
    for i in range(1, n):
        # Check possible jumps from stone i-k to i
        for j in range(1, min(k, i) + 1):
            dp[i] = min(dp[i], dp[i - j] + abs(arr[i] - arr[i - j]))
    
    return dp[n-1]

# Example usage:
arr1 = [10, 30, 40, 50, 20]
k1 = 3
print(minCost(arr1, k1))  # Output: 30

arr2 = [10, 20, 10]
k2 = 1
print(minCost(arr2, k2))  # Output: 20
