def fibonacci(n):
    MOD = 10**9 + 7
    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = (fib[i - 1] + fib[i - 2]) % MOD
    return fib

# Example usage:
n = 10
print(fibonacci(n))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
