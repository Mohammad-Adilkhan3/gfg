def minSteps(d):
    steps = 0
    total = 0
    while total < d or (total - d) % 2 != 0:
        steps += 1
        total += steps
    return steps

# Example usage:
print(minSteps(2))  # Output: 3
print(minSteps(10)) # Output: 4
