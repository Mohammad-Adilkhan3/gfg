def search(text, pattern):
    result = []

    # Iterate through the text using a sliding window
    for i in range(len(text) - len(pattern) + 1):
        # Check if the substring of text matches the pattern
        if text[i:i + len(pattern)] == pattern:
            result.append(i + 1)  # Append the 1-based index to the result list

    return result

# Example usage:
text1 = "birthdayboy"
pattern1 = "birth"
print(search(text1, pattern1))
# Output: [1]

text2 = "geeksforgeeks"
pattern2 = "geek"
print(search(text2, pattern2))
# Output: [1, 9]
