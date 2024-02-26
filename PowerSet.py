def AllPossibleStrings(s):
    n = len(s)
    result = []

    # Generate all subsequences using bitmask
    for i in range(1, 2 ** n):
        subsequence = ""
        for j in range(n):
            if (i >> j) & 1:
                subsequence += s[j]
        result.append(subsequence)

    # Sort the result lexicographically
    result.sort()

    return result

# Example usage:
s1 = "abc"
print(AllPossibleStrings(s1))
# Output: ['a', 'ab', 'abc', 'ac', 'b', 'bc', 'c']

s2 = "aa"
print(AllPossibleStrings(s2))
# Output: ['a', 'a', 'aa']
