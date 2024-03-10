def removeDuplicates(s):
    seen_chars = set()
    result = ''
    
    for char in s:
        if char not in seen_chars:
            seen_chars.add(char)
            result += char
    
    return result

# Example usage:
input_str = "abacdb"
output_str = removeDuplicates(input_str)

print(output_str)  # Output: "abcd"
