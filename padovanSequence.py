def padovan(n):
    MOD = 10**9 + 7
    
    # Base cases
    if n == 0 or n == 1 or n == 2:
        return 1
    
    # Initial values
    P0, P1, P2 = 1, 1, 1
    
    # Compute Padovan values iteratively
    for i in range(3, n + 1):
        Pn = (P1 + P0) % MOD
        P0, P1, P2 = P1, P2, Pn
    
    return P2

# Example usage
n = 1000000
print(padovan(n))  # This will print the nth Padovan number modulo 10^9+7
