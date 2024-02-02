def atoi(s):
    n = len(s)
    
    if n == 0:
        return -1

    sign = 1
    i = 0

    # Handle leading whitespaces
    while i < n and s[i] == ' ':
        i += 1

    # Handle sign character
    if i < n and (s[i] == '-' or s[i] == '+'):
        sign = -1 if s[i] == '-' else 1
        i += 1

    result = 0

    # Process the digits
    while i < n and s[i].isdigit():
        result = result * 10 + int(s[i])
        i += 1

    result *= sign

    # Check if the conversion is feasible
    if i < n:
        return -1

    # Check for integer overflow
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    return min(max(result, INT_MIN), INT_MAX)

# Example 1
s1 = "-123"
print(atoi(s1))  # Output: -123

# Example 2
s2 = "21a"
print(atoi(s2))  # Output: -1
