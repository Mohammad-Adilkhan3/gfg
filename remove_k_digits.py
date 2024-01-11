def removeKdigits(S, K):
    stack = []

    for digit in S:
        while K > 0 and stack and stack[-1] > digit:
            stack.pop()
            K -= 1
        stack.append(digit)

    # Remove remaining K digits from the end
    stack = stack[:-K] if K > 0 else stack

    # Remove leading zeros
    result = ''.join(stack).lstrip('0')

    # If result is empty, return '0'
    return result if result else '0'

# Example usage:
S1 = "149811"
K1 = 3
output1 = removeKdigits(S1, K1)
print("Output 1:", output1)

S2 = "1002991"
K2 = 3
output2 = removeKdigits(S2, K2)
print("Output 2:", output2)
