#stack approch
def longestValidParentheses(s: str) -> int:
    # Stack to keep track of indices of unmatched parentheses
    stack = [-1]
    max_len = 0

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)  # Push index of '(' onto the stack
        else:
            stack.pop()  # Pop the last '(' or invalid ')'
            if not stack:
                stack.append(i)  # Push index of unmatched ')'
            else:
                max_len = max(max_len, i - stack[-1])  # Calculate valid length

    return max_len

# Example Usage:
s1 = "((()"
s2 = ")()())"
print(longestValidParentheses(s1))  # Output: 2
print(longestValidParentheses(s2))  # Output: 4
//two pointer approch
left = right = 0
    max_len = 0

    # Left to right pass
    for char in s:
        if char == '(':
            left += 1
        else:
            right += 1
        if left == right:
            max_len = max(max_len, 2 * right)
        elif right > left:
            left = right = 0

    left = right = 0
    # Right to left pass
    for char in reversed(s):
        if char == '(':
            left += 1
        else:
            right += 1
        if left == right:
            max_len = max(max_len, 2 * left)
        elif left > right:
            left = right = 0

    return max_len
