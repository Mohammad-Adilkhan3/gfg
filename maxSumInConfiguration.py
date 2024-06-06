def max_sum_rotation(n, a):
    # Calculate initial sum S0 and the total sum of the array
    S0 = sum(i * a[i] for i in range(n))
    total_sum = sum(a)
    
    # Initialize the current sum to S0 and the maximum sum found
    current_sum = S0
    max_sum = S0
    
    # Compute the sum for each rotation using the relationship derived
    for i in range(1, n):
        current_sum = current_sum - total_sum + n * a[i - 1]
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Example usage:
n = 4
a = [8, 3, 1, 2]
print(max_sum_rotation(n, a))  # Output: 29

n = 3
a = [1, 2, 3]
print(max_sum_rotation(n, a))  # Output: 8
