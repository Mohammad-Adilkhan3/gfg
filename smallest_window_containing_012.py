def smallestSubstring(S):
    n = len(S)
    count = [0, 0, 0]
    start = 0
    min_len = float('inf')
    found = False

    for end in range(n):
        count[int(S[end])] += 1

        while all(count):
            found = True
            min_len = min(min_len, end - start + 1)
            count[int(S[start])] -= 1
            start += 1

    return min_len if found else -1

# Example usage:
S1 = "10212"
result1 = smallestSubstring(S1)
print("Example 1:", result1)

S2 = "12121"
result2 = smallestSubstring(S2)
print("Example 2:", result2)
