def evenOdd(s):
    from collections import Counter
    
    # Count frequency of each character
    freq = Counter(s)
    
    x = 0
    y = 0
    
    for char, count in freq.items():
        position = ord(char) - ord('a') + 1  # 1-based position of the character in the alphabet
        if position % 2 == 0:  # even position
            if count % 2 == 0:  # even frequency
                x += 1
        else:  # odd position
            if count % 2 != 0:  # odd frequency
                y += 1
    
    # Determine if the sum of x and y is even or odd
    if (x + y) % 2 == 0:
        return "EVEN"
    else:
        return "ODD"

# Example usage:
print(evenOdd("abbbcc"))  # Output: ODD
print(evenOdd("nobitaa"))  # Output: EVEN
