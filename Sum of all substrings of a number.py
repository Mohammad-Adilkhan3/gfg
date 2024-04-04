def sumSubstrings(s):
    MOD = 10**9 + 7
    n = len(s)
    
    # Initialize variables to store the result and the multiplier
    result = 0
    multiplier = 1
    
    # Iterate through the string from right to left
    for i in range(n-1, -1, -1):
        # Calculate the contribution of the current digit to all substrings
        result = (result + int(s[i]) * multiplier * (i + 1)) % MOD
        
        # Update the multiplier for the next iteration
        multiplier = (multiplier * 10 + 1) % MOD
    
    return result

# Example usage:
s1 = "1234"
s2 = "421"

print("Sum of all possible sub-strings of", s1, ":", sumSubstrings(s1))
print("Sum of all possible sub-strings of", s2, ":", sumSubstrings(s2))
