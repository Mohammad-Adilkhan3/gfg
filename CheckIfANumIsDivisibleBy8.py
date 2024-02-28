def is_divisible_by_eight(s):
    n = len(s)

    # If the length of the string is less than 3, we can convert it to an integer and check directly
    if n <= 3:
        return 1 if int(s) % 8 == 0 else -1
    
    # Otherwise, check if the last three digits are divisible by 8
    last_three_digits = int(s[n - 3:])
    return 1 if int(last_three_digits % 8 == 0) else -1

# Example usage:
num1 = "123456"
print(is_divisible_by_eight(num1))
# Output: 1

num2 = "987654"
print(is_divisible_by_eight(num2))
# Output: -1
