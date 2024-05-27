def longestSubseq(n, a):
    # Initialize the dp array
    dp = [1] * n

    # Build the dp array
    for i in range(1, n):
        for j in range(i):
            if abs(a[i] - a[j]) == 1:
                dp[i] = max(dp[i], dp[j] + 1)

    # The length of the longest subsequence will be the maximum value in dp
    return max(dp)

# Example usage:
n1, a1 = 7, [10, 9, 4, 5, 4, 8, 6]
print(longestSubseq(n1, a1))  # Output: 3

n2, a2 = 5, [1, 2, 3, 4, 5]
print(longestSubseq(n2, a2))  # Output: 5

