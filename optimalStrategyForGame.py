def maximumAmount(arr, n):
    # Initialize a 2D array to store the maximum amount
    dp = [[0] * n for _ in range(n)]
    
    # Fill the diagonal elements with the values of coins
    for i in range(n):
        dp[i][i] = arr[i]
    
    # Iterate over the array in bottom-up manner
    for gap in range(1, n):
        for i in range(n - gap):
            j = i + gap
            if gap == 1:
                dp[i][j] = max(arr[i], arr[j])
            else:
                dp[i][j] = max(arr[i] + min(dp[i+2][j], dp[i+1][j-1]),
                               arr[j] + min(dp[i+1][j-1], dp[i][j-2]))
    
    # Return the maximum amount collected
    return dp[0][n-1]

# Example usage:
arr1 = [5, 3, 7, 10]
arr2 = [8, 15, 3, 7]

print("Maximum possible amount (Example 1):", maximumAmount(arr1, len(arr1)))
print("Maximum possible amount (Example 2):", maximumAmount(arr2, len(arr2)))
