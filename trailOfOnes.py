def numberOfConsecutiveOnes(n):
    MOD = 10**9 + 7
    
    if n < 2:
        return 0
    
    # Initialize base cases
    A = [0] * (n + 1)
    B = [0] * (n + 1)
    
    A[0] = 1
    A[1] = 2
    power_of_2 = 4  # This represents 2^2 initially
    
    for i in range(2, n + 1):
        A[i] = (A[i-1] + A[i-2]) % MOD
        B[i] = (power_of_2 - A[i] + MOD) % MOD
        power_of_2 = (power_of_2 * 2) % MOD  # Increment power of 2 for next length
    
    return B[n]

# Example usage:
print(numberOfConsecutiveOnes(2))  # Output: 1
print(numberOfConsecutiveOnes(3))  # Output: 3
print(numberOfConsecutiveOnes(5))  # Output: 19
