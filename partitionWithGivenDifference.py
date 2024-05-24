def countPartitions(n, d, arr):
    MOD = 10**9 + 7
    
    # Calculate the total sum of the array
    total_sum = sum(arr)
    
    # Calculate the target sum S1
    target_sum = (total_sum + d) // 2
    
    # Check feasibility conditions
    if (total_sum + d) % 2 != 0 or target_sum < 0:
        return 0
    
    # Initialize the DP array
    dp = [0] * (target_sum + 1)
    dp[0] = 1  # There's one way to get sum 0, which is using an empty subset
    
    # Fill the DP table
    for num in arr:
        for j in range(target_sum, num - 1, -1):
            dp[j] = (dp[j] + dp[j - num]) % MOD
    
    # The answer is the number of ways to achieve the target sum
    return dp[target_sum]

# Example usage:
n1, d1, arr1 = 4, 3, [5, 2, 6, 4]
print(countPartitions(n1, d1, arr1))  # Output: 1

n2, d2, arr2 = 4, 0, [1, 1, 1, 1]
print(countPartitions(n2, d2, arr2))  # Output: 6
